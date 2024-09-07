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

# Example usage
file_path = 'a.fasta'
fasta_sequences = read_fasta(file_path)
for header, sequence in fasta_sequences.items():
    #print(f"Header: {header}")
    print(f"Sequence: {sequence}\n")
print("h")