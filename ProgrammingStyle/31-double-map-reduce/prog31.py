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


def regroup(pairs_list):
    mapping = {}
    for pairs in pairs_list:
        for p in pairs:
            if p[0] in mapping:
                mapping[p[0]].append(p)
            else:
                mapping[p[0]] = [p]
    return mapping


def count_words(mapping):
    def add(x, y):
        return x + y

    return (mapping[0], reduce(add, (pair[1] for pair in mapping[1])))


def sort(word_freq):
    return sorted(word_freq, key=operator.itemgetter(1), reverse=True)


splits = map(split_words, partition(read_file(sys.argv[1]), 200))
splits_per_word = regroup(splits)
word_freqs = sort(map(count_words, splits_per_word.items()))
for (w, c) in word_freqs[:25]:
    print(f"{w} - {c}")
