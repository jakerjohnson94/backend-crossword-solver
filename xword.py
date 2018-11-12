#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jake Johnson"

# YOUR HELPER FUNCTION GOES HERE


def find_possible_words(test_word, words):
    result = []
    trash = []
    for word in words:
        for index, letter in enumerate(test_word):
            if len(word) == len(test_word):
                if word[index] == letter or letter == ' ':
                    result.append(word)
                else:
                    trash.append(word)
    return sorted(list(set([x for x in result if x not in trash])))


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    for word in find_possible_words(test_word, words):
        print(word)


if __name__ == '__main__':
    main()
