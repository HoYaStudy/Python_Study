#!/usr/bin/python3

import os
import sys
import re
import operator
import itertools
from pathlib import Path

all_words = [(), None]
ignore_words = [(), None]
non_ignore_words = [
    (),
    lambda: list(map(lambda w: w if w not in ignore_words[0] else "", all_words[0])),
]
unique_words = [(), lambda: set([w for w in non_ignore_words[0] if w != ""])]
counts = [
    (),
    lambda: list(
        map(
            lambda w, word_list: word_list.count(w),
            unique_words[0],
            itertools.repeat(non_ignore_words[0], len(unique_words[0])),
        )
    ),
]
sorted_data = [
    (),
    lambda: sorted(
        zip(list(unique_words[0]), list(counts[0])),
        key=operator.itemgetter(1),
        reverse=True,
    ),
]
all_columns = [
    all_words,
    ignore_words,
    non_ignore_words,
    unique_words,
    counts,
    sorted_data,
]


def update():
    global all_columns
    for c in all_columns:
        if c[1] != None:
            c[0] = c[1]()


all_words[0] = re.findall("[a-z]{2,}", open(sys.argv[1]).read().lower())
ignore_words[0] = set(
    open(os.path.join(Path.cwd(), "res/ignore-words.txt")).read().split(",")
)
update()

for (w, c) in sorted_data[0][:25]:
    print(f"{w} - {c}")
