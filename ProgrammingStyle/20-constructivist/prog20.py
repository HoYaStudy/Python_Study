#!/usr/bin/python3

import os
import sys
import re
import string
import inspect
import operator
from pathlib import Path


def extract_words(path):
    if type(path) is not str or not path:
        return []

    try:
        with open(path) as f:
            str_data = f.read()
    except IOError as e:
        print(f"I/O error({e.errno}) when opening {path}: {e.strerror}")
        return []

    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    return word_list


def remove_ignore_words(word_list):
    if type(word_list) is not list:
        return []

    try:
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            ignore_words = f.read().split(",")
    except IOError as e:
        print(f"I/O error({e.errno}) when opening igrnore-words.txt: {e.strerror}")
        return word_list

    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    if type(word_list) is not list or word_list == []:
        return {}

    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    if type(word_freq) is not dict or word_freq == {}:
        return []
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


filename = (
    sys.argv[1] if len(sys.argv) > 1 else os.path.join(Path.cwd(), "res/input.txt")
)
word_freqs = sort(frequencies(remove_ignore_words(extract_words(filename))))
for wf in word_freqs[0:25]:
    print(f"{wf[0]} - {wf[1]}")
