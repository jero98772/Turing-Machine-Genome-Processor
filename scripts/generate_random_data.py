import random

def generate_sequence(length, seq_type='DNA'):
    """Generates a random DNA or RNA sequence.
    
    Args:
        length (int): Length of the sequence to generate.
        seq_type (str): Type of sequence to generate, 'DNA' or 'RNA'.
                        Defaults to 'DNA'.
    
    Returns:
        str: A randomly generated DNA or RNA sequence.
    """
    if seq_type == 'DNA':
        bases = 'ATGC'
    elif seq_type == 'RNA':
        bases = 'AUGC'
    else:
        raise ValueError("seq_type must be either 'DNA' or 'RNA'")
    
    return ''.join(random.choice(bases) for _ in range(length))

# Example usage:
dna_seq = generate_sequence(500000, 'DNA')
rna_seq = generate_sequence(500000, 'RNA')

#print(f">Random DNA sequence\n {dna_seq}")
print(f">Random RNA sequence\n{rna_seq}")
