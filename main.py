"""
DNA Genome Processing Program

functionalities:

- Compute the reverse complement of a DNA sequence.
- Count the occurrences of a k-mer (including reverse complements) in a genome.
- Find the most frequent k-mers (including reverse complements) in a genome.

Functions:

- reverse_pattern(pattern): Computes the reverse complement of a DNA sequence.
- count_k_mer(genome, pattern): Counts the occurrences of a k-mer and its reverse complement in the genome.
- frequent_k_mer(genome, k): Finds the most frequent k-mers (including reverse complements) in the genome.
- read_genome_from_file(filename): Reads the genome string from a file.
- is_valid_dna_sequence(sequence): Checks if a sequence contains only valid DNA nucleotides (A, C, G, T).

Author: Muhammad Adra Prakoso
DAMN THIS WAS HARD
"""

def reverse_pattern(pattern):
    """
    Computes the reverse complement of a DNA sequence.

    Args:
        pattern (str): DNA sequence.

    Returns:
        str: Reverse complement of the input sequence.
    """
    # Define complement mapping
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement = ''
    # Iterate over the pattern in reverse order
    for nucleotide in pattern[::-1]:
        # Get the complement nucleotide
        if nucleotide in complement:
            reverse_complement += complement[nucleotide]
        else:
            # Handle invalid nucleotide
            reverse_complement += 'N'  # 'N' denotes any nucleotide
    return reverse_complement

def count_k_mer(genome, pattern):
    """
    Counts the occurrences of a k-mer and its reverse complement in the genome.

    Args:
        genome (str): Genome sequence.
        pattern (str): k-mer pattern to count.

    Returns:
        int: Number of occurrences of the pattern and its reverse complement.
    """
    pattern_length = len(pattern)
    reverse_complement = reverse_pattern(pattern)
    count = 0
    # Loop over genome to get substrings of length pattern_length
    for i in range(len(genome) - pattern_length + 1):
        substring = genome[i:i+pattern_length]
        # Check if substring matches pattern or reverse complement
        if substring == pattern or substring == reverse_complement:
            count += 1
    return count

def frequent_k_mer(genome, k):
    """
    Finds the most frequent k-mers (including reverse complements) in the genome.

    Args:
        genome (str): Genome sequence.
        k (int): Length of k-mer.

    Returns:
        list: List of most frequent k-mers.
    """
    k_mer_counts = {}
    genome_length = len(genome)
    # Generate all possible k-mers in the genome
    for i in range(genome_length - k + 1):
        k_mer = genome[i:i+k]
        reverse_k_mer = reverse_pattern(k_mer)
        # Canonical form: lexicographically smaller between k_mer and reverse_k_mer
        canonical_k_mer = min(k_mer, reverse_k_mer)
        # Count the canonical k-mer
        if canonical_k_mer in k_mer_counts:
            k_mer_counts[canonical_k_mer] += 1
        else:
            k_mer_counts[canonical_k_mer] = 1
    # Find the maximum count
    max_count = 0
    for count in k_mer_counts.values():
        if count > max_count:
            max_count = count
    # Collect all k-mers with the maximum count
    most_frequent_k_mers = []
    for k_mer in k_mer_counts:
        if k_mer_counts[k_mer] == max_count:
            most_frequent_k_mers.append(k_mer)
    return most_frequent_k_mers

def read_genome_from_file(filename):
    """
    Reads the genome string from a file.

    Args:
        filename (str): Path to the file containing the genome string.

    Returns:
        str: Genome sequence, or empty string if file not found or invalid content.
    """
    try:
        with open(filename, 'r') as f:
            genome = f.read()
            # Remove whitespace and newlines, convert to uppercase
            genome = ''.join(genome.split()).upper()
            if not is_valid_dna_sequence(genome):
                print("Invalid genome sequence in the file.")
                return ''
            return genome
    except FileNotFoundError:
        print("File not found.")
        return ''

def is_valid_dna_sequence(sequence):
    """
    Checks if a sequence contains only valid DNA nucleotides (A, C, G, T).

    Args:
        sequence (str): DNA sequence to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    valid_nucleotides = set('ACGT')
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False
    return True

def main():
    """
    Main function to run the program.
    """
    # Get the filename from user
    filename = input("Enter the filename containing the genome string: ")
    genome = read_genome_from_file(filename)
    if not genome:
        return
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Compute a reverse complement of a k-mer pattern")
        print("2. Count a k-mer pattern")
        print("3. Find most frequent k-mer patterns")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            pattern = input("Enter the k-mer pattern: ").upper()
            if not pattern or not is_valid_dna_sequence(pattern):
                print("Invalid pattern input.")
                continue
            reverse_comp = reverse_pattern(pattern)
            print("Reverse complement:", reverse_comp)
        elif choice == '2':
            pattern = input("Enter the k-mer pattern: ").upper()
            if not pattern or not is_valid_dna_sequence(pattern):
                print("Invalid pattern input.")
                continue
            count = count_k_mer(genome, pattern)
            print("Count:", count)
        elif choice == '3':
            k_input = input("Enter the value of k: ")
            if not k_input.isdigit():
                print("Invalid input.")
                continue
            k = int(k_input)
            if k <= 0 or k > len(genome):
                print("Invalid k value.")
                continue
            most_freq_k_mers = frequent_k_mer(genome, k)
            print("Most frequent k-mers:")
            for k_mer in most_freq_k_mers:
                print(k_mer)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
