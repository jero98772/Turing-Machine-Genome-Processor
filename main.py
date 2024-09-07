import argparse

def read_fasta(file_path):
    """
    Reads a FASTA file and returns a dictionary with headers as keys and sequences as values.
    
    Args:
        file_path (str): Path to the FASTA file.

    Returns:
        dict: A dictionary where the keys are sequence headers and the values are sequences.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        header = None
        sequence = []

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    # Save the previous sequence
                    sequences[header] = ''.join(sequence)
                # Start a new sequence
                header = line[1:]
                sequence = []
            else:
                # Continue building the sequence
                sequence.append(line)
        
        if header:
            # Save the last sequence
            sequences[header] = ''.join(sequence)
    
    return sequences
class TuringMachine:
    def __init__(self, tape_length=30000):
        self.tape = [0] * tape_length  # Memory tape initialized with zeros
        self.pointer = 0  # Memory pointer starts at the first block
        self.instruction_pointer = 0  # Instruction pointer starts at the first instruction
        self.loop_stack = []  # Stack to manage loop positions
        self.program = ""  # Program instructions will be stored here
        self.codon_start=["atg","aug"]
        self.codon_stop=["uaa","taa","uag","tag","uga","tga"]
        self.tape_length=tape_length
    def load_program(self, program):
        self.program = program

    def run(self):
        open_kmrs=False
        while self.instruction_pointer < len(self.program):
            kmers3=None
            if 1<self.instruction_pointer<len(self.program)-1:
                kmers3 = str(self.program[self.instruction_pointer-1:self.instruction_pointer+2]).lower()
            command = self.program[self.instruction_pointer]
            #print(kmers3)
            #print(self.codon_start,self.codon_stop)
            #print(str(kmers3).lower() in self.codon_start)
            if kmers3 in self.codon_start:
                #print("kmer_o")
                open_kmrs=True
                if self.tape[self.pointer] == 0:
                    # Jump to the instruction after the matching 'codon stop'
                    open_brackets = 1
                    while open_brackets != 0:
                        kmers3 = str(self.program[self.instruction_pointer:self.instruction_pointer+3]).lower()
                        #print(self.instruction_pointer,kmers3,self.codon_stop,open_brackets)
                        self.instruction_pointer += 1
                        if kmers3 in self.codon_start:
                            open_brackets += 1
                        elif kmers3 in self.codon_stop:
                            open_brackets -= 1
                        if self.instruction_pointer>len(self.program):
                            print("not found stop codon, End the program")
                            print(self.get_tape())
                            exit()
                else:
                    self.loop_stack.append(self.instruction_pointer)
            elif kmers3 in self.codon_stop and open_kmrs:
                open_kmrs=False
                #print("kmer_c")
                if self.tape[self.pointer] != 0 and len(self.loop_stack)!=0:
                    self.instruction_pointer = self.loop_stack[-1]  # Jump back to the matching 'codon stop'
                else:
                    if len(self.loop_stack)!=0:
                        self.loop_stack.pop()

            elif command.lower() == 'a':
                self.pointer = (self.pointer+1)%self.tape_length
            elif command.lower() == 't' or command.lower() == 'u' :
                self.pointer = (self.pointer+1)%self.tape_length
            elif command.lower() == 'c':
                self.tape[self.pointer] += 1
            elif command.lower() == 'g':
                self.tape[self.pointer] -= 1
            self.instruction_pointer += 1

    def get_tape(self):
        return self.tape

    def get_pointer(self):
        return self.pointer



def main():
    # Argument parsing
    tape_length=100
    parser = argparse.ArgumentParser(description="Run a Turing Machine with a FASTA file as input.")
    parser.add_argument("fasta_file", help="Path to the FASTA file.")
    args = parser.parse_args()

    # Read the FASTA file
    fasta_sequences = read_fasta(args.fasta_file)
    #print(fasta_sequences)
    # Combine all sequences in the FASTA file into one program
    program = "".join(fasta_sequences.values())

    # Initialize and run the Turing machine
    tm = TuringMachine(tape_length)
    tm.load_program(program)
    tm.run()

    # Output results
    print("Tape after processing:", tm.get_tape()[:tape_length])  # Print first 10 blocks for brevity
    print("Pointer position:", tm.get_pointer())

if __name__ == "__main__":
    main()
