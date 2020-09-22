#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


def read_file(path, func):
    with open(path) as f:
        data = f.read()
    func(data, normalize)


def filter_chars(str_data, func):
    pattern = re.compile('[\W_]+')
    func(pattern.sub(' ', str_data), scan)


def normalize(str_data, func):
    func(str_data.lower(), remove_ignore_words)


def scan(str_data, func):
    func(str_data.split(), frequencies)


def remove_ignore_words(word_list, func):
    with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
        ignore_words = f.read().split(',')
    ignore_words.extend(list(string.ascii_lowercase))
    func([w for w in word_list if not w in ignore_words], sort)


def frequencies(word_list, func):
    wf = {}
    for w in word_list:
        if w in wf:
            wf[w] += 1
        else:
            wf[w] = 1
    func(wf, print_text)


def sort(wf, func):
    func(sorted(wf.items(), key=operator.itemgetter(1), reverse=True), no_op)


def print_text(word_freqs, func):
    for (w, c) in word_freqs[0:25]:
        print(f'{w} - {c}')
    func(None)


def no_op(func):
    return


read_file(sys.argv[1], filter_chars)
