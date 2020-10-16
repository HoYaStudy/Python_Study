#!/usr/bin/python3

import sys
import re
import string
import operator
from pathlib import Path
from functools import reduce


def read_file(path):
    with open(path) as f:
        data = f.read()
    return data


def partition(data_str, nlines):
    lines = data_str.split("\n")
    for i in range(0, len(lines), nlines):
        yield "\n".join(lines[i : i + nlines])


def split_words(data_str):
    def _scan(str_data):
        pattern = re.compile("[\W_]+")
        return pattern.sub(" ", str_data).lower().split()

    def _remove_ignore_words(word_list):
        with open(Path.joinpath(Path.cwd(), "res/ignore-words.txt")) as f:
            ignore_words = f.read().split(",")
        ignore_words.extend(list(string.ascii_lowercase))
        return [w for w in word_list if not w in ignore_words]

    result = []
    words = _remove_ignore_words(_scan(data_str))
    for w in words:
        result.append((w, 1))
    return result


def count_words(pairs_list_1, pairs_list_2):
    mapping = {}
    for pl in [pairs_list_1, pairs_list_2]:
        for p in pl:
            if p[0] in mapping:
                mapping[p[0]] += p[1]
            else:
                mapping[p[0]] = p[1]
    return mapping.items()


def sort(word_freq):
    return sorted(word_freq, key=operator.itemgetter(1), reverse=True)


splits = map(split_words, partition(read_file(sys.argv[1]), 200))
word_freqs = sort(reduce(count_words, splits))
for (w, f) in word_freqs[:25]:
    print(f"{w} - {f}")
