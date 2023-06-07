# BCH-Error-Correction

This repository contains a Python implementation of the BCH (Bose–Chaudhuri–Hocquenghem) error correction code. This was for my Cryptography module during my third year of University.

## Features

The script can:

- Generate a BCH code from a six-digit input using the `BCHGenerator` function. The function calculates four parity digits and appends them to the input to create a ten-digit BCH code.
- Decode a ten-digit BCH code using the `BCHDecoder` function. The function calculates four syndromes from the input code and uses them to correct one or two errors in the code. If there are more than two errors, it returns an error message.

## Usage

To use the script, call the `BCHGenerator` function with a six-digit input to generate a BCH code, or call the `BCHDecoder` function with a ten-digit BCH code to decode it.
