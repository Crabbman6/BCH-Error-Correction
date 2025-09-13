# Python Implementation of a BCH Error-Correcting Code

[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)

This repository contains a Python implementation of a **Bose–Chaudhuri–Hocquenghem (BCH)** code, a powerful type of error-correcting code used to ensure data integrity. This specific implementation is a `(10,6)` code over the Galois Field GF(11), capable of detecting and correcting up to two errors in a transmitted codeword.

This project was developed as a practical exercise for my university Cryptography module, demonstrating the application of finite field arithmetic to solve real-world data transmission problems.

## ✅ Features

* **Encoder (`BCHGenerator`)**: Encodes a 6-digit message into a 10-digit BCH codeword by calculating and appending 4 parity-check digits.
* **Decoder (`BCHDecoder`)**: Takes a 10-digit codeword and performs error checking.
* **Single-Error Correction**: Successfully identifies and corrects any single-digit error in the codeword.
* **Double-Error Correction**: Successfully identifies and corrects any two-digit errors in the codeword.
* **Error Detection**: Reports when three or more errors are present and cannot be corrected.

---

## ⚙️ How It Works

The script operates using the principles of finite field arithmetic to achieve error correction.

1.  **Encoding**: The `BCHGenerator` takes the 6 message digits ($d_0$ to $d_5$) and calculates 4 parity digits ($d_6$ to $d_9$) using a predefined generator polynomial over GF(11). This ensures the resulting 10-digit codeword satisfies a set of linear equations.

2.  **Syndrome Calculation**: When the `BCHDecoder` receives a (potentially corrupted) codeword, it calculates four **syndromes** ($s_1, s_2, s_3, s_4$). If the codeword is error-free, all syndromes will be zero. Non-zero syndromes indicate the presence of errors.

3.  **Error Location and Correction**: If errors are detected, the script uses the syndrome values to solve a system of equations (based on Peterson's Algorithm) to find the **positions** ($i, j$) and **magnitudes** ($a, b$) of the errors. The original codeword is then restored by subtracting the error magnitudes at the identified positions.

---

## 🚀 Setup & Installation

To use this script, clone the repository and ensure you have Python 3 installed.

```bash
# Clone the repository
git clone [https://github.com/Crabbman6/BCH-Error-Correction.git](https://github.com/Crabbman6/BCH-Error-Correction.git)

# Navigate to the directory
cd BCH-Error-Correction
```
For clarity, the main Python file is named Cryptography Practical 3 Final.py.

## 💡 Usage Examples

You can import the BCHGenerator and BCHDecoder functions to use them in your own scripts.

(Note: The examples below assume you have renamed the file to bch_functions.py for easier importing.)

1. Generating a Codeword

```
from bch_functions import BCHGenerator, BCHDecoder

# Original 6-digit message
original_message = "123456"

# Generate the 10-digit codeword
encoded_word = BCHGenerator(original_message)

print(f"Original Message: {original_message}")
print(f"Encoded Codeword: {encoded_word}")

# Expected Output:
# Encoder Input: 123456
# Original Message: 123456
# Encoded Codeword: 1234565217
```

2. Correcting a Single Error

Here, we take the valid codeword 1234565217, introduce an error (change the 3rd digit from 3 to 9), and watch the decoder fix it.

```
# Introduce a single error
corrupted_word_1_error = "1294565217"

# Decode and correct the message
corrected_word = BCHDecoder(corrupted_word_1_error)

print(f"\nCorrupted (1 Error): {corrupted_word_1_error}")
print(f"Decoder Output is: {corrected_word}")

# Expected Output:
# Decoder Input: 1294565217
# s1, s2, s3, s4: [5, 4, 2, 7]
# P, Q, R: [0, 0, 0]
#
# Single Error...
# errorMagnitude (a): 5
# errorPosition (i): 3
# Corrupted (1 Error): 1294565217
# Decoder Output is: 1234565217
```

3. Correcting Two Errors

Here, we introduce two errors (change the 2nd digit to 1 and the 5th digit to 8) and the decoder fixes both.

```
# Introduce two errors
corrupted_word_2_errors = "1134865217"

# Decode and correct the message
corrected_word_2 = BCHDecoder(corrupted_word_2_errors)

print(f"\nCorrupted (2 Errors): {corrupted_word_2_errors}")
print(f"Decoder Output is: {corrected_word_2}")

# Expected Output:
# Decoder Input: 1134865217
# s1, s2, s3, s4: [10, 3, 1, 4]
# P, Q, R: [1, 5, 6]
#
# Two Errors...
# i,j: [5, 2]
# a,b: [3, 1]
# Corrupted (2 Errors): 1134865217
# Decoder Output is: 1234565217
```

4. Detecting More Than Two Errors

When three or more errors are present, the algorithm correctly identifies that the message is unrecoverable.

```
# Introduce three errors
uncorrectable_word = "9885980731"

# Attempt to decode
result = BCHDecoder(uncorrectable_word)

print(f"\nUncorrectable Word: {uncorrectable_word}")
print(f"Decoder Output is: {result}")

# Expected Output:
# Decoder Input: 9885980731
# s1, s2, s3, s4: [5, 8, 9, 8]
# P, Q, R: [9, 8, 7]
#
# Uncorrectable Word: 9885980731
# Decoder Output is: No square root, therefore more than two errors...
```

🛠️ Technologies Used

  Python 3: The sole language used for the logic and implementation.
  No external libraries are required.
