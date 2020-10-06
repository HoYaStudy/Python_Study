#!/usr/bin/python3

import os
import sys
import re
import operator
from pathlib import Path


RECURSION_LIMIT = 9500
sys.setrecursionlimit(RECURSION_LIMIT + 10)


def count(word_list, ignore_words, word_freqs):
    if word_list == []:
        return
    else:
        word = word_list[0]
        if word not in ignore_words:
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
        count(word_list[1:], ignore_words, word_freqs)


def wf_print(word_freqs):
    if word_freqs == []:
        return
    else:
        (w, c) = word_freqs[0]
        print(f'{w} - {c}')
        wf_print(word_freqs[1:])


ignore_words = set(open(os.path.join(Path.cwd(), 'res/ignore-words.txt')).read().split(','))
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
word_freqs = {}

for i in range(0, len(words), RECURSION_LIMIT):
    count(words[i:i + RECURSION_LIMIT], ignore_words, word_freqs)

wf_print(sorted(word_freqs.items(), key=operator.itemgetter(1), reverse=True)[:25])
