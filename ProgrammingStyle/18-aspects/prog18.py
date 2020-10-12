#!/usr/bin/python3

import os
import sys
import re
import time
import string
import operator
from pathlib import Path


def extract_words(path):
    with open(path) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def profile(f):
    def profilewrapper(*args, **kwargs):
        start_time = time.time()
        ret_value = f(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{f.__name__} took {elapsed} secs")
        return ret_value

    return profilewrapper


tracked_functions = [extract_words, frequencies, sort]
for func in tracked_functions:
    globals()[func.__name__] = profile(func)

word_freqs = sort(frequencies(extract_words(sys.argv[1])))
for (w, c) in word_freqs[0:25]:
    print(f"{w} - {c}")
