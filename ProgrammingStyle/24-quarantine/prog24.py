#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


class WFQuarantine:
    def __init__(self, func):
        self._funcs = [func]

    def bind(self, func):
        self._funcs.append(func)
        return self

    def execute(self):
        def guard_callable(v):
            return v() if hasattr(v, "__call__") else v

        value = lambda: None
        for func in self._funcs:
            value = func(guard_callable(value))
        print(guard_callable(value))


def get_input(arg):
    def _f():
        return sys.argv[1]

    return _f


def extract_words(path):
    def _f():
        with open(path) as f:
            data = f.read()
        pattern = re.compile("[\W_]+")
        word_list = pattern.sub(" ", data).lower().split()
        return word_list

    return _f


def remove_ignore_words(word_list):
    def _f():
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            ignore_words = f.read().split(",")
        ignore_words.extend(list(string.ascii_lowercase))
        return [w for w in word_list if not w in ignore_words]

    return _f


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


def top25_freqs(word_freqs):
    top25 = ""
    for wf in word_freqs[:25]:
        top25 += f"{str(wf[0])} - {str(wf[1])}\n"
    return top25


WFQuarantine(get_input).bind(extract_words).bind(remove_ignore_words).bind(
    frequencies
).bind(sort).bind(top25_freqs).execute()
