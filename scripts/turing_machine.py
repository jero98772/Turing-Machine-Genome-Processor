class TuringMachine:
    def __init__(self, tape_length=30000):
        self.tape = [0] * tape_length  # Memory tape initialized with zeros
        self.pointer = 0  # Memory pointer starts at the first block
        self.instruction_pointer = 0  # Instruction pointer starts at the first instruction
        self.loop_stack = []  # Stack to manage loop positions
        self.program = ""  # Program instructions will be stored here

    def load_program(self, program):
        self.program = program

    def run(self):
        while self.instruction_pointer < len(self.program):
            command = self.program[self.instruction_pointer]

            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.tape[self.pointer] += 1
            elif command == '-':
                self.tape[self.pointer] -= 1
            elif command == '[':
                if self.tape[self.pointer] == 0:
                    # Jump to the instruction after the matching ']'
                    open_brackets = 1
                    while open_brackets != 0:
                        self.instruction_pointer += 1
                        if self.program[self.instruction_pointer] == '[':
                            open_brackets += 1
                        elif self.program[self.instruction_pointer] == ']':
                            open_brackets -= 1
                else:
                    self.loop_stack.append(self.instruction_pointer)
            elif command == ']':
                if self.tape[self.pointer] != 0:
                    self.instruction_pointer = self.loop_stack[-1]  # Jump back to the matching '['
                else:
                    self.loop_stack.pop()

            self.instruction_pointer += 1

    def get_tape(self):
        return self.tape

    def get_pointer(self):
        return self.pointer


# Example usage
tm = TuringMachine()

# Load a simple Brainfuck-like program to increment the first block to 10
program = "++++++++++[>++++++++<-]"  # This will set the first cell to 10
tm.load_program(program)

# Run the Turing machine
tm.run()

# Output the value at the first block of the tape
print("Tape after processing:", tm.get_tape()[:10])  # Print first 10 blocks for brevity
print("Pointer position:", tm.get_pointer())

