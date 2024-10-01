# DNA Genome Processing Program

## Overview

---

## Introduction to DNA

### DNA Structure

DNA molecules are composed of two strands that form a double helix structure.

### Nucleotides and Pairing

DNA is made up of smaller units called **nucleotides**, each consisting of:
- **phosphate group**
- **deoxyribose sugar**
- **nitrogenous base**

There are four types of bases in DNA:
1. **Adenine (A)**
2. **Cytosine (C)**
3. **Guanine (G)**
4. **Thymine (T)**

**Base Pairing Rules:**
- **Adenine (A)** with **Thymine (T)**
- **Cytosine (C)** with **Guanine (G)**

These complementary base pairs form the rungs of the DNA double helix.

### Reverse Complement

The **reverse complement** of a DNA sequence is formed by:
1. **Reversing** the original sequence.
2. **Replacing** each nucleotide with its complement based on base pairing rules.

**Example:**
- **Original Sequence:** `ACGT`
- **Reversed:** `TGCA`
- **Complemented:** `ACGT`
- **Reverse Complement:** `ACGT`

### K-mers

A **k-mer** is a substring of length *k* extracted from a DNA sequence.

**Example:**
- **Sequence:** `ACGTAC`
- **2-mers:** `AC`, `CG`, `GT`, `TA`, `AC`

### Lexicographical Order and Canonical k-mers

**Lexicographical Order** ia a fancy way of saying alphabetical order of component elements, similar to dictionary ordering.

A **canonical k-mer** is the lexicographically smaller string between a k-mer and its reverse complement. This standardization ensures that each k-mer pair (original and reverse complement) is represented uniquely.

**Example:**
- **k-mer:** `AGC`
- **Reverse Complement:** `GCT`
- **Canonical Form:** `AGC` (since `A` < `G`)

---

## Project Features

### 1. Reverse Complement of a k-mer Pattern

**Function:** `reverse_pattern(pattern)`

**Description:** Computes the reverse complement of a given DNA sequence (k-mer).

**Usage:**
```python
reverse_comp = reverse_pattern("AGC")
print(reverse_comp)  # Outputs: GCT
```

### 2. Counting the Occurrences of a K-MER

**Function:** `count_k_mer(genome, pattern)`

**Description:** Counts how many times a specific k-mer and its reverse complement appear in the genome sequence.

**Usage:**
```python
count = count_k_mer(genome_sequence, "AGC")
print(count)  # Outputs the number of occurrences
```

### 3. Most Frequent K-MERs

**Function:** `frequent_k_mer(genome, k)`

**Description:** Identifies the k-mers with the highest occurrence frequency within the genome.

**Usage:**
```python
most_freq = frequent_k_mer(genome_sequence, 3)
print(most_freq)  # Outputs a list of the most frequent 3-mers
```

### 4. Main Program

**Description:** A menu-based interface that allows users to interactively choose between computing reverse complements, counting k-mers, finding the most frequent k-mers, or exiting the program.

### 5. Input Validation

**Description:** Ensures that user inputs are valid, such as checking for valid DNA nucleotides, appropriate k-mer lengths, and correct file formats. Invalid inputs prompt user-friendly error messages and request re-entry.

---

## Code Structure

### Functions

1. **`reverse_pattern(pattern)`**
   - **Purpose:** Computes the reverse complement of a DNA sequence.
   - **Inputs:** `pattern` (str) - DNA sequence.
   - **Returns:** Reverse complement (str).

2. **`count_k_mer(genome, pattern)`**
   - **Purpose:** Counts occurrences of a k-mer and its reverse complement in the genome.
   - **Inputs:** 
     - `genome` (str) - Genome sequence.
     - `pattern` (str) - k-mer pattern.
   - **Returns:** Count (int).

3. **`frequent_k_mer(genome, k)`**
   - **Purpose:** Finds the most frequent k-mers in the genome.
   - **Inputs:** 
     - `genome` (str) - Genome sequence.
     - `k` (int) - Length of k-mer.
   - **Returns:** List of most frequent k-mers (list).

4. **`read_genome_from_file(filename)`**
   - **Purpose:** Reads genome sequence from a file.
   - **Inputs:** `filename` (str) - Path to genome file.
   - **Returns:** Genome sequence (str).

5. **`is_valid_dna_sequence(sequence)`**
   - **Purpose:** Validates that the sequence contains only A, C, G, T.
   - **Inputs:** `sequence` (str) - DNA sequence.
   - **Returns:** Boolean indicating validity.

### Main Program Flow

1. **Input Genome File:**
   - Prompts user to enter the filename.
   - Reads and validates the genome sequence.

2. **Display Menu:**
   - Presents options to compute reverse complements, count k-mers, find frequent k-mers, or exit.

3. **Handle User Choices:**
   - Based on user selection, performs the corresponding function.
   - Ensures all inputs are validated before processing.

4. **Loop Until Exit:**
   - Continues to display the menu after each operation until the user chooses to exit.

---

## Examples

### Example 1: Computing Reverse Complement

- **Input k-mer:** `AGC`
- **Reverse Complement:** `GCT`

### Example 2: Counting k-mer Occurrences

- **Genome Sequence:** `ACGTACGTAC`
- **k-mer Pattern:** `ACG`
- **Occurrences:** `2` (positions 0-2 and 4-6)

### Example 3: Finding Most Frequent k-mers

- **Genome Sequence:** `ACGTACGTAC`
- **k = 3`
- **Most Frequent k-mers:** `ACG`, `CGT`, `GTA`, `TAC` (each appearing twice)