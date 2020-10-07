#!/usr/bin/python3

import os
import sys
import re
import string
import inspect
import operator
from pathlib import Path


def read_ignore_words():
    if inspect.stack()[1][3] != "extract_words":
        return None

    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return ignore_words


def extract_words(path):
    with open(locals()["path"]) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    ignore_words = read_ignore_words()
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    word_freqs = {}
    for w in locals()["word_list"]:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    return sorted(
        locals()["word_freq"].items(), key=operator.itemgetter(1), reverse=True
    )


def main():
    word_freqs = sort(frequencies(extract_words(sys.argv[1])))
    for (w, c) in word_freqs[0:25]:
        print(f"{w} - {c}")


if __name__ == "__main__":
    main()