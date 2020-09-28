#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


class WFTheOne:
    def __init__(self, v):
        self._value = v

    def bind(self, func):
        self._value = func(self._value)
        return self

    def printme(self):
        print(self._value)


def read_file(path):
    with open(path) as f:
        data = f.read()
    return data


def filter_chars(str_data):
    pattern = re.compile("[\W_]+")
    return pattern.sub(" ", str_data)


def normalize(str_data):
    return str_data.lower()


def scan(str_data):
    return str_data.split()


def remove_ignore_words(word_list):
    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]


def frequencies(word_list):
    word_freq = {}
    for w in word_list:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    return word_freq


def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def top25_freqs(word_freqs):
    top25 = ""
    for wf in word_freqs[0:25]:
        top25 += f"{str(wf[0])} - {str(wf[1])}\n"
    return top25


WFTheOne(sys.argv[1])\
    .bind(read_file)\
    .bind(filter_chars)\
    .bind(normalize)\
    .bind(scan)\
    .bind(remove_ignore_words)\
    .bind(frequencies)\
    .bind(sort)\
    .bind(top25_freqs)\
    .printme()
