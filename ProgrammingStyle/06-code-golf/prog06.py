#!/usr/bin/python3

import os
import sys
import re
import collections
from pathlib import Path

ignore_words = open(os.path.join(Path.cwd(), 'res/ignore-words.txt')).read().split(',')
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
freqs = collections.Counter(w for w in words if w not in ignore_words)
for (w, c) in freqs.most_common(25):
    print(f'{w} - {c}')
