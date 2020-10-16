#!/usr/bin/python3

import sys
import re
import string
import operator
from pathlib import Path
from threading import Thread
from queue import Queue, Empty

word_space = Queue()
freq_space = Queue()

ignore_words = set(
    open(Path.joinpath(Path.cwd(), "res/ignore-words.txt")).read().split(",")
)


def process_words():
    word_freqs = {}
    while True:
        try:
            word = word_space.get(timeout=1)
        except Empty:
            break
        if not word in ignore_words:
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
    freq_space.put(word_freqs)


for word in re.findall("[a-z]{2,}", open(sys.argv[1]).read().lower()):
    word_space.put(word)

workers = []
for i in range(5):
    workers.append(Thread(target=process_words))
[t.start() for t in workers]

[t.join() for t in workers]

word_freqs = {}
while not freq_space.empty():
    freqs = freq_space.get()
    for (k, v) in freqs.items():
        if k in word_freqs:
            count = sum(item[k] for item in [freqs, word_freqs])
        else:
            count = freqs[k]
        word_freqs[k] = count

for (w, f) in sorted(word_freqs.items(), key=operator.itemgetter(1), reverse=True)[:25]:
    print(f"{w} - {f}")
