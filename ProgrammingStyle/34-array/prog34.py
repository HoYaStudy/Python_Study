#!/usr/bin/python3

import os
import sys
import numpy as np
from pathlib import Path


characters = np.array([' '] + list(open(sys.argv[1]).read()) + [' '])
characters[~np.char.isalpha(characters)] = ' '
characters = np.char.lower(characters)

space = np.where(characters == ' ')
space2 = np.repeat(space, 2)
word_indexes = np.reshape(space2[1:-1], (-1, 2))
word_indexes = word_indexes[np.where(word_indexes[:, 1] - word_indexes[:, 0] > 2)]

tokenized_words = list(map(lambda r: characters[r[0]:r[1]], word_indexes))
words = np.array(list(map(lambda w: ''.join(w).strip(), tokenized_words)))

ignore_words = np.array(list(set(open(os.path.join(Path.cwd(), 'res/ignore-words.txt')).read().split(','))))
filtered_words = words[~np.isin(words, ignore_words)]

word, freqs = np.unique(filtered_words, axis=0, return_counts=True)
sorted_word_freqs = sorted(zip(word, freqs), key=lambda t: t[1], reverse=True)

for w, f in sorted_word_freqs[:25]:
    print(f'{w} - {f}')