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


def has_letter(s):
    if "'" in s: return False
    for c in s:
        if c != '?': return True
    return False

def translate(s, dct):
    text = ''
    for c in s:
        if 'A' <= c <= 'Z':
            text += dct.get(c, '?')
        elif c == "'":
            text += "'"
        else:
            text += ' '
    return text

def load_words():
    fn = '/usr/share/dict/words'
    result = []
    for line in open(fn):
        result.append(line.strip().upper())
    return result

def make_score_dict(words, target_letters):
    result = {}
    for word in words:
        w = ''
        score = 0
        for c in word:
            if c in target_letters:
                score += 1.0
                w += c
            else:
                w += '?'
        if score > 0:
            result[w] = result.get(w, 0) + score * score
    return result

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(data):
    """Given a string, returns the decrypted version of the text."""
    valid_words = load_words()
    dct = {}
    dct['F'] = 'A'
    dct['G'] = 'B'
    dct['H'] = 'C'
    dct['I'] = 'D'
    dct['K'] = 'F'
    dct['L'] = 'G'
    dct['M'] = 'H'
    dct['Q'] = 'L'
    dct['C'] = 'X'

    target_letters = dct.values()
    for target_letter in LETTERS:
        if target_letter in target_letters:
            continue
        target_letters.append(target_letter)
        score_dict = make_score_dict(valid_words, target_letters)
        print target_letters
        guesses = []
        for code_letter in LETTERS:
            if code_letter in dct:
                continue
            dct[code_letter] = target_letter
            text = translate(data, dct)
            data_words = filter(has_letter, text.split())
            score = 0
            for word in data_words:
                word_score = score_dict.get(word, -1000)
                score += word_score
            guess = (score, code_letter)
            guesses.append(guess)
            del dct[code_letter]
            print code_letter, score

        print '\n' * 5
        print '--------'
        guesses.sort(reverse=True)
        code_letter = guesses[0][1]
        dct[code_letter] = target_letter
        print dct
        print translate(data, dct)
        print code_letter, target_letter
        if (ord(code_letter) - ord('A') + 21) % 26 != ord(target_letter) - ord('A'):
            raise Exception('fail')

if len(sys.argv) != 2:
    sys.exit('please specify the file to decrypt as the first parameter')

with open(sys.argv[1],"r") as textfile:
    decrypt(textfile.read())
