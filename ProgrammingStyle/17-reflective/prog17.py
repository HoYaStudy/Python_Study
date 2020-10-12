#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path

ignores = set(
    open(os.path.join(Path.cwd(), "res/ignore-words.txt")).read().split(",")
    + list(string.ascii_lowercase)
)


def frequencies_imp(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


if len(sys.argv) > 1:
    extract_words_func = "lambda name: [x.lower() for x in re.split('[^a-zA-Z]+', open(name).read()) if len(x) >0 and x.lower() not in ignores]"
    frequencies_func = "lambda wl : frequencies_imp(wl)"
    sort_func = "lambda word_freq: sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)"
    filename = sys.argv[1]
else:
    extract_words_func = "lambda x: []"
    frequencies_func = "lambda x: []"
    sort_func = "lambda x: []"
    filename = os.path.basename(__file__)


exec(f"extract_words = {extract_words_func}")
exec(f"frequencies = {frequencies_func}")
exec(f"sort = {sort_func}")


word_freqs = locals()["sort"](
    locals()["frequencies"](locals()["extract_words"](filename))
)
for (w, c) in word_freqs[0:25]:
    print(f"{w} - {c}")
