#!/usr/bin/python3

import os
import sys
import string
from pathlib import Path


word_freqs = []


with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
    ignore_words = f.read().split(',')
ignore_words.extend(list(string.ascii_lowercase))


for line in open(sys.argv[1]):
    start_index = None
    i = 0
    for c in line:
        if start_index == None:
            if c.isalnum():
                start_index = i
        else:
            if not c.isalnum():
                found = False
                word = line[start_index:i].lower()
                if word not in ignore_words:
                    pair_index = 0
                    for pair in word_freqs:
                        if word == pair[0]:
                            pair[1] += 1
                            found = True
                            break
                        pair_index += 1
                    if not found:
                        word_freqs.append([word, 1])
                    elif len(word_freqs) > 1:
                        for n in reversed(range(pair_index)):
                            if word_freqs[pair_index][1] > word_freqs[n][1]:
                                word_freqs[n], word_freqs[pair_index] = word_freqs[pair_index], word_freqs[n]
                                pair_index = n
                start_index = None
        i += 1


for wf in word_freqs[0:25]:
    print(f"{wf[0]} - {wf[1]}")