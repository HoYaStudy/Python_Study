#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


def read_file(path):
    with open(path) as f:
        data = f.read()
    return data


def filter_chars_and_normalize(data):
    pattern = re.compile('[\W_]+')
    return pattern.sub(' ', data).lower()


def scan(data):
    return data.split()


def remove_ignore_words(word_list):
    with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
        ignore_words = f.read().split(',')
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


def sort(word_freqs):
    return sorted(word_freqs.items(), key=operator.itemgetter(1), reverse=True)


def print_all(word_freqs):
    if len(word_freqs) > 0:
        print(f'{word_freqs[0][0]} - {word_freqs[0][1]}')
        print_all(word_freqs[1:])


print_all(sort(frequencies(remove_ignore_words(scan(filter_chars_and_normalize(read_file(sys.argv[1]))))))[0:25])