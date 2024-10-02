"""
- Compute the reverse complement of a DNA sequence
- Count the occurrences of a k-mer (including reverse complements)
- Find the most frequent k-mers (including reverse complements)

Funcs:

- reverse_pattern(pattern): Computes the reverse complement of a DNA sequence
- count_k_mer(genome, pattern): Counts the occurrences of a k-mer and its reverse complement
- frequent_k_mer(genome, k): Finds the most frequent k-mers (including reverse complements)
- read_genome_from_file(filename): Reads the genome string from a file
- is_valid_dna_sequence(sequence): Checks if a sequence contains only valid DNA nucleotides (A, C, G, T)

Muhammad Adra Prakoso - KKI - VIN
"""

def reverse_pattern_dict(pattern):
    """
    Computes the reverse complement of a DNA sequence, uses dict to map nucleotides to complements (Key-Value Pair)

    Args:
        pattern (str): DNA sequence

    Returns:
        str: Reverse complement of the input sequence
    """
    # Define a dictionary to map each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Initialize an empty string to store the reverse complement
    reverse_complement = ''

    # Iterate over the pattern in reverse order using slicing
    for nucleotide in pattern[::-1]:
        # Check if the nucleotide is valid (exists in the complement dictionary)
        if nucleotide in complement:
            # Append the complement nucleotide to the reverse_complement string
            reverse_complement += complement[nucleotide]
        else:
            # Append 'N' to denote any invalid nucleotide
            reverse_complement += 'N'  # 'N' denotes any nucleotide

    # Returns reverse complement string
    return reverse_complement

def reverse_pattern_args(pattern):
    """
    Same function but uses arguments instead of dict, less efficient
    """
    # Initialize an empty string to store the reverse complement
    reverse_complement = ''

    # Iterate over the pattern in reverse order using slicing
    for nucleotide in pattern[::-1]:
        # Determine the complement nucleotide using conditional statements
        if nucleotide == 'A':
            complement_nuc = 'T'
        elif nucleotide == 'T':
            complement_nuc = 'A'
        elif nucleotide == 'C':
            complement_nuc = 'G'
        elif nucleotide == 'G':
            complement_nuc = 'C'
        else:
            # Append 'N' to denote any invalid nucleotide
            complement_nuc = 'N'  # 'N' denotes any nucleotide

        # Append the complement nucleotide to the reverse_complement string
        reverse_complement += complement_nuc

    # Return the complete reverse complement string
    return reverse_complement


def count_k_mer(genome, pattern):
    """
    Counts the occurrences of k-mer and reverse complements

    This function iterates over the genome string to extract all possible substrings
    (k-mers) of pattern length
    `range(len(genome) - pattern_length + 1)` determines number of valid
    starting positions for k-mers. This ensures that each extracted substring is
    exactly length `pattern_length` without exceeding the bounds of genome string

    Args:
        genome (str): The genome sequence to search within
        pattern (str): The k-mer pattern to count in the genome

    Returns:
        int: The total number of occurrences of the pattern and its reverse complement in the genome
    """
    # Determine length of the pattern
    pattern_length = len(pattern)

    # Compute reverse complement of the pattern
    reverse_complement = reverse_pattern_dict(pattern)

    # Initialize a counter for occurrences
    count = 0

    # Iterate over genome to extract all possible k-mers
    for i in range(len(genome) - pattern_length + 1):
        # Extract current k-mer substring
        substring = genome[i:i + pattern_length]

        # Check if substring matches the pattern or its reverse complement
        if substring == pattern or substring == reverse_complement:
            count += 1  # Increment the counter if a match is found

    # Return the total count of matches
    return count

def min_k_mer(k_mer1, k_mer2):
    """
    Going off template, but I need to make another function
    determines the lexicographically smaller k-mer between two k-mers

    Args:
        k_mer1 (str): First k-mer.
        k_mer2 (str): Second k-mer (usually the reverse complement)

    Returns:
        str: Lexicographically smaller k-mer
    """
    # Compare each character of the two k-mers
    for a, b in zip(k_mer1, k_mer2):
        if a < b:
            return k_mer1
        elif a > b:
            return k_mer2
    # If all characters are equal, return either
    return k_mer1

def frequent_k_mer(genome, k):
    """
    Finds the most frequent k-mers (including reverse complements) in the genome

    Args:
        genome (str): Genome sequence
        k (int): Length of k-mer

    Returns:
        list: List of most frequent k-mers
    """
    # Initialize two empty lists:
    # - unique_k_mers: stores unique canonical k-mers
    # - counts: stores the corresponding counts for each unique k-mer
    unique_k_mers = []
    counts = []

    # Determine the length of the genome string
    genome_length = len(genome)

    # Loop over the genome to extract all possible k-mers
    for i in range(genome_length - k + 1):
        # Extract the k-mer starting at position i
        k_mer = genome[i:i+k]

        # Compute the reverse complement of the k-mer
        reverse_k_mer = reverse_pattern_dict(k_mer)

        # Determine the canonical form of k-mer by choosing the lexicographically smaller one
        canonical_k_mer = min_k_mer(k_mer, reverse_k_mer)

        # Flag to check if the canonical_k_mer is already in unique_k_mers
        # Before checking for the existence of the current canonical_k_mer in the unique_k_mers list, the flag is set to False
        # Assuming that the k-mer has not been found yet
        found = False

        # Iterate over the unique_k_mers to find if canonical_k_mer already exists
        for j in range(len(unique_k_mers)):
            # By using the same index, j, we iterate unique_k_mers and counts in parallel, ensuring that counts[j] reflects
            # The number of times unique_k_mers[j] has been encountered
            if unique_k_mers[j] == canonical_k_mer:
                # If found, increment the count, [j] accesses the count corresponding to the k-mer at index
                counts[j] += 1
                found = True
                break  # Exit the loop once found

        # If canonical_k_mer was not found in unique_k_mers, add it and initialize its count to 1
        if not found:
            unique_k_mers.append(canonical_k_mer)
            counts.append(1)

    # Initialize a variable to keep track of the maximum count found
    max_count = 0

    # Iterate over all counts to find the maximum count, remember that counts is the counts list
    for count in counts:
        if count > max_count:
            max_count = count

    # Initialize an empty list to store the most frequent k-mers
    most_frequent_k_mers = []

    # Iterate over the unique_k_mers and their counts to collect k-mers with the maximum count
    for k in range(len(unique_k_mers)):
        if counts[k] == max_count:
            most_frequent_k_mers.append(unique_k_mers[k])

    # Return the list of most frequent k-mers
    return most_frequent_k_mers

def read_genome_from_file(filename):
    """
    Reads genome string from a file

    Args:
        filename (str): Path to file containing genome string

    Returns:
        str: Genome sequence, or empty string if file not found or invalid content
    """
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as f:
            # Read the entire content of the file
            genome = f.read()

            # Remove all whitespace characters (including spaces and newlines) and convert to uppercase
            genome = ''.join(genome.split()).upper()

            # Validate the genome sequence to ensure it contains only valid nucleotides
            if not is_valid_dna_sequence(genome):
                # If invalid, print an error message and return an empty string
                print("Invalid genome sequence in the file.")
                return ''

            # If valid, return the cleaned genome sequence
            return genome
    except FileNotFoundError:
        # If the file is not found, print an error message and return an empty string
        print("File not found.")
        return ''

def is_valid_dna_sequence(sequence):
    """
    Checks if a sequence contains only valid DNA nucleotides (A, C, G, T)

    Args:
        sequence (str): DNA sequence to validate

    Returns:
        bool: True if valid, False otherwise
    """
    # Define a set of valid nucleotides for quick lookup
    valid_nucleotides = set('ACGT')

    # Iterate over each nucleotide in the sequence
    for nucl in sequence:
        # If the nucleotide is not in the set of valid nucleotides, return False
        if nucl not in valid_nucleotides:
            return False

    # If all nucleotides are valid, return True
    return True

def main():
    # Prompt the user to enter the filename containing the genome string
    filename = input("Enter the genome filename: ")

    # Attempt to read the genome from the specified file
    genome = read_genome_from_file(filename)

    # If the genome is empty (due to file not found or invalid content), exit the program
    if not genome:
        return

    # Enter an infinite loop to display the menu repeatedly until the user chooses to exit
    while True:
        # Display the menu options to the user
        print("\nMenu:")
        print("1. Compute the reverse complement of a k-mer pattern")
        print("2. Count k-mer pattern")
        print("3. Find most frequent k-mer patterns")
        print("4. Exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-4): ")

        # Handle the user's choice using conditional statements
        if choice == '1':
            # Option 1: Compute reverse complement of a k-mer pattern
            pattern = input("Enter the k-mer pattern: ").upper()  # Read the pattern and convert to uppercase

            # Validate the pattern input to ensure it's not empty and contains only valid nucleotides
            if not pattern or not is_valid_dna_sequence(pattern):
                print("Invalid pattern input.")
                continue  # Restart the loop to display the menu again

            # Compute the reverse complement using the reverse_pattern function
            reverse_comp = reverse_pattern_dict(pattern)

            # Display the reverse complement to the user
            print("Reverse complement:", reverse_comp)

        elif choice == '2':
            # Option 2: Count the occurrences of a k-mer pattern
            pattern = input("Enter the k-mer pattern: ").upper()  # Read the pattern and convert to uppercase

            # Validate the pattern input
            if not pattern or not is_valid_dna_sequence(pattern):
                print("Invalid pattern input.")
                continue  # restart the loop

            # Count the occurrences using the count_k_mer function
            count = count_k_mer(genome, pattern)

            # Display the count to the user
            print("Count:", count)

        elif choice == '3':
            # Option 3: Find the most frequent k-mer patterns
            k_input = input("Enter the value of k: ")  # Prompt the user to enter the value of k

            # Check if the input for k is a digit
            if not k_input.isdigit():
                print("Invalid input.")
                continue  # restart the loop

            # Convert the input to an integer
            k = int(k_input)

            # Validate the value of k to ensure it's positive and does not exceed the genome length
            if k <= 0 or k > len(genome):
                print("Invalid k value.")
                continue  # restart the loop

            # Find the most frequent k-mers using the frequent_k_mer function
            most_freq_k_mers = frequent_k_mer(genome, k)

            # Display the most frequent k-mers to the user
            print("Most frequent k-mers:")
            for k_mer in most_freq_k_mers:
                print(k_mer)

        elif choice == '4':
            # Option 4: Exit the program
            print("Exiting the program.")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
