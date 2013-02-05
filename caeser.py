#!/usr/bin/env python
# Humbug, Inc. interview question
"""Decrypt Caeser-ciphered text

This program accepts a filename as a parameter and prints a decrypted
version of the file to standard output.
"""

import sys

# For your reference, the approximate frequencies of occurences of various
# letters in English are:
ftable = [8.12, # A
1.49, # B
2.71, # C
4.32, # D
12.02,# E
2.30, # F
2.03, # G
5.92, # H
7.31, # I
0.10, # J
0.69, # K
3.98, # L
2.61, # M
6.95, # N
7.68, # O
1.82, # P
0.11, # Q
6.02, # R
6.28, # S
9.10, # T
2.88, # U
1.11, # V
2.09, # W
0.17, # X
2.11, # X
0.07] # Z


def alpha_to_int(letter):
    """Converts a letter to an integer in the (inclusive) range of 0-25"""
    return (ord(letter) & 31) - 1

def int_to_alpha(numb):
    """Converts an integer in the range of 0-25 into an uppercase letter."""
    return chr(numb + 65)

def decrypt_letter(c, offset):
    if 'A' <= c <= 'Z':
        return int_to_alpha((alpha_to_int(c) + offset) % 26)
    else:
        return c

def decrypt(data):
    """Given a string, returns the decrypted version of the text."""
    # Write your code here. You can create other functions and modify existing
    # code as needed.
    translations = []
    for offset in range(26):
        def f(c):
            return decrypt_letter(c, offset)

        text = ''.join(map(f, data))
        score = 0
        for c in text:
            if 'A' <= c <= 'Z':
                score += ftable[ord(c) - ord('A')]
        translations.append((score, text))
    best_translation = max(translations)[1]
    return best_translation

if len(sys.argv) != 2:
    sys.exit('please specify the file to decrypt as the first parameter')

with open(sys.argv[1],"r") as textfile:
    print decrypt(textfile.read())
