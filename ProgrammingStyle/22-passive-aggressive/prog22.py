#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


def extract_words(path):
    assert type(path) is str, "Error: Need a string"
    assert path, "Error: Empty string"

    with open(path) as f:
        data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", data).lower().split()
    return word_list


def remove_ignore_words(word_list):
    assert type(word_list) is list, "Error: Not a list"

    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    assert type(word_list) is list, "Error: Not a list"
    assert word_list != [], "Error: Empty list"

    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freqs):
    assert type(word_freqs) is dict, "Error: Not a dictionary"
    assert word_freqs != {}, "Error: Empty dictionary"

    return sorted(word_freqs.items(), key=operator.itemgetter(1), reverse=True)


try:
    assert len(sys.argv) > 1, "Error: Need an input file"
    word_freqs = sort(frequencies(remove_ignore_words(extract_words(sys.argv[1]))))
    assert len(word_freqs) > 25, "Error: Less than 25 words"
    for wf in word_freqs[0:25]:
        print(f"{wf[0]} - {wf[1]}")
except Exception as e:
    print(f"Something wrong: {e}")
