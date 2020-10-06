#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


data_storage_obj = {
    "data": [],
    "init": lambda path: extract_words(data_storage_obj, path),
    "words": lambda: data_storage_obj["data"],
}

ignore_words_obj = {
    "ignore_words": [],
    "init": lambda: load_ignore_words(ignore_words_obj),
    "is_ignore_word": lambda word: word in ignore_words_obj["ignore_words"],
}

word_freqs_obj = {
    "freqs": {},
    "increment_count": lambda w: increment_count(word_freqs_obj, w),
    "sorted": lambda: sorted(
        word_freqs_obj["freqs"].items(), key=operator.itemgetter(1), reverse=True
    ),
}


def extract_words(obj, path):
    with open(path) as f:
        obj["data"] = f.read()
    pattern = re.compile("[\W_]+")
    data_str = "".join(pattern.sub(" ", obj["data"]).lower())
    obj["data"] = data_str.split()


def load_ignore_words(obj):
    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        obj["ignore_words"] = f.read().split(",")
    obj["ignore_words"].extend(list(string.ascii_lowercase))


def increment_count(obj, w):
    obj["freqs"][w] = 1 if w not in obj["freqs"] else obj["freqs"][w] + 1


data_storage_obj["init"](sys.argv[1])
ignore_words_obj["init"]()

for w in data_storage_obj["words"]():
    if not ignore_words_obj["is_ignore_word"](w):
        word_freqs_obj["increment_count"](w)

word_freqs = word_freqs_obj["sorted"]()
for (w, c) in word_freqs[0:25]:
    print(f"{w} - {c}")
