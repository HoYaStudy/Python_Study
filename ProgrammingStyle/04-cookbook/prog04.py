#!/usr/bin/python3

import os
import sys
import string
from pathlib import Path


data = []
words = []
word_freqs = []


def read_file(path):
    global data
    with open(path) as f:
        data = data + list(f.read())


def filter_chars_and_normalize():
    global data
    for i in range(len(data)):
        if not data[i].isalnum():
            data[i] = ' '
        else:
            data[i] = data[i].lower()


def scan():
    global data
    global words
    data_str = ''.join(data)
    words = words + data_str.split()


def remove_ignore_words():
    global words
    with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
        ignore_words = f.read().split(',')
    ignore_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in ignore_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)


def frequencies():
    global words
    global word_freqs
    for w in words:
        keys = [wf[0] for wf in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])


def sort():
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)


read_file(sys.argv[1])
filter_chars_and_normalize()
scan()
remove_ignore_words()
frequencies()
sort()

for wf in word_freqs[0:25]:
    print(f'{wf[0]} - {wf[1]}')
