#!/usr/bin/python3

import sys
import string
import operator
from pathlib import Path


def characters(filename):
    for line in open(filename):
        for c in line:
            yield c


def all_words(filename):
    start_char = True
    for c in characters(filename):
        if start_char == True:
            word = ""
            if c.isalnum():
                word = c.lower()
                start_char = False
            else:
                pass
        else:
            if c.isalnum():
                word += c.lower()
            else:
                start_char = True
                yield word


def non_ignore_words(filename):
    ignore_words = set(
        open(Path.joinpath(Path.cwd(), "res/ignore-words.txt")).read().split(",")
        + list(string.ascii_lowercase)
    )
    for w in all_words(filename):
        if not w in ignore_words:
            yield w


def count_and_sort(filename):
    freqs, i = {}, 1
    for w in non_ignore_words(filename):
        freqs[w] = 1 if w not in freqs else freqs[w] + 1
    yield sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)


for word_freqs in count_and_sort(sys.argv[1]):
    for (w, c) in word_freqs[:25]:
        print(f"{w} - {c}")
