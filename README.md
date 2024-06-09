# TFCS-Helper
This repository contains to code for a calculator that can be used for analysing systems as taught in the summer course of 2024 in "Technical Foundations of Computer Science". 
## Error Detection
This class, ErrorDetection, is designed to calculate error detection and verification in digital communication systems. It contains methods for checksum calculation, error verification, parity bit calculation, and error detection.
### Static Methods
- `binary_addition`: Performs binary addition of two binary strings with a specified number of bits, handling overflow.
- `ones_complement`: Computes the one's complement of a binary string.
- `print_binary_addition`: Helper method to print binary addition operations neatly.
### Methods
- `calculate_checksum`: Calculates the checksum for a list of data blocks. It iterates through the blocks, performs binary addition, prints each step, and returns the one's complement of the final sum.
- `verify_data`: Verifies received data against a checksum. It follows a similar process to calculate_checksum, but additionally checks if the final one's complement sum matches the received checksum.
- `calculate_parity_bit`: Calculates the parity bit for a given data block based on the specified parity type ('even' or 'odd').
- `detect_error`: Compares the parity bits of sender and receiver data to detect errors. It prints relevant information and returns a boolean indicating error detection.

## System Analysis
This class, SystemAnalysis, provides all methods relevant in the course for analyzing systems, including calculation of Hamming distance, weighted mean, mean, harmonic mean, geometric mean, comparison of systems, Amdahl's law, conversion of truth tables to Boolean expressions, information entropy and information gain.
- `hamming_distance`: Computes the Hamming distance between two strings, along with the number of detectable and correctable errors.
- `weighted_mean`, `mean`, `harmonic_mean`, `geometric_mean`: Calculate different types of means for given data.
- `norm_geometric_mean`: Calculates the geometric mean of data with respect to a reference system's data.
- `comparison`: Compares two systems based on a specified metric.
- `amdahls_law`: Computes the speedup according to Amdahl's Law for parallel processing.
- `truth_table_to_expression`: Converts a truth table to Boolean expressions (minterm and maxterm) and realises a given function. 
- `calculate_entropy_and_information`: Calculates entropy and information gain based on probabilities of events.

Example usecases have been included in each file to get a better idea. 

