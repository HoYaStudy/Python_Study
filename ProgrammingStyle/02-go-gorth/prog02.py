#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


stack = []
heap = {}


def read_file():
    with open(stack.pop()) as f:
        stack.append([f.read()])


def filter_chars():
    stack.append(re.compile('[\W_]+'))
    stack.append([stack.pop().sub(' ', stack.pop()[0]).lower()])


def scan():
    stack.extend(stack.pop()[0].split())


def remove_ignore_words():
    with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
        stack.append(f.read().split(','))
    stack[-1].extend(list(string.ascii_lowercase))
    heap['ignore_words'] = stack.pop()
    heap['words'] = []
    while len(stack) > 0:
        if stack[-1] in heap['ignore_words']:
            stack.pop()
        else:
            heap['words'].append(stack.pop())
    stack.extend(heap['words'])
    del heap['ignore_words']
    del heap['words']


def frequencies():
    heap['word_freqs'] = {}
    while len(stack) > 0:
        if stack[-1] in heap['word_freqs']:
            stack.append(heap['word_freqs'][stack[-1]])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(1)
        heap['word_freqs'][stack.pop()] = stack.pop()
    stack.append(heap['word_freqs'])
    del heap['word_freqs']


def sort():
    stack.extend(sorted(stack.pop().items(), key=operator.itemgetter(1)))


stack.append(sys.argv[1])
read_file()
filter_chars()
scan()
remove_ignore_words()
frequencies()
sort()

stack.append(0)
while stack[-1] < 25 and len(stack) > 1:
    heap['i'] = stack.pop()
    (w, f) = stack.pop()
    print(f'{w} - {f}')
    stack.append(heap['i'])
    stack.append(1)
    stack.append(stack.pop() + stack.pop())