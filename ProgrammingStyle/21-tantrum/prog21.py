#!/usr/bin/python3

import os
import sys
import re
import string
import operator
import traceback
from pathlib import Path


def extract_words(path):
    assert type(path) is str, "Error: Not a string"
    assert path, "Error: Empty string"

    try:
        with open(path) as f:
            str_data = f.read()
    except IOError as e:
        print(f"I/O errro({e.errno}) when opening {path}: {e.strerror}")
        raise e

    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    return word_list


def remove_ignore_words(word_list):
    assert type(word_list) is list, "Error: Not a list"

    try:
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            ignore_words = f.read().split(",")
    except IOError as e:
        print(f"I/O error({e.errno}) when opening ignore_words.txt: {e.strerror}")
        raise e

    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    assert type(word_list) is list, "Error: not a list"
    assert word_list != [], "Error: Empty list"

    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    assert type(word_freq) is dict, "Error: Not a dictionary"
    assert word_freq != {}, "Error: Empty dictionary"

    try:
        return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
    except Exception as e:
        print(f"sorted threw {e.errno}: {e.strerror}")
        raise e


try:
    assert len(sys.argv) > 1, "Error: Need an input file"
    word_freqs = sort(frequencies(remove_ignore_words(extract_words(sys.argv[1]))))
    assert type(word_freqs) is list, "Error: Not a list"
    assert len(word_freqs) > 25, "Error: Less than 25 words"
    for (w, c) in word_freqs[0:25]:
        print(f"{w} - {c}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()