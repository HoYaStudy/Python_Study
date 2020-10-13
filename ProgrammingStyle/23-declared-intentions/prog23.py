#!/usr/bin/python3

import os
import sys
import re
import string
import inspect
import operator
from pathlib import Path


class AcceptTypes:
    def __init__(self, *args):
        self._args = args

    def __call__(self, f):
        def wrapped_f(*args):
            for i in range(len(self._args)):
                if type(args[i]) != self._args[i]:
                    raise TypeError(
                        f"Expecting {str(self._args[i])} got {str(type(args[i]))}"
                    )
            return f(*args)

        return wrapped_f


@AcceptTypes(str)
def extract_words(path):
    with open(path) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


@AcceptTypes(list)
def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


@AcceptTypes(dict)
def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


word_freqs = sort(frequencies(extract_words(sys.argv[1])))
for (w, c) in word_freqs[:25]:
    print(f"{w} - {c}")
