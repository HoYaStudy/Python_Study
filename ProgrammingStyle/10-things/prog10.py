#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path
from abc import ABCMeta


class WFExercise():
    __metaclass__ = ABCMeta

    def info(self):
        return self.__class__.__name__


class DataStorageManager(WFExercise):
    def __init__(self, path):
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile('[\W_]+')
        self._data = pattern.sub(' ', self._data).lower()

    def words(self):
        return self._data.split()

    def info(self):
        return super(DataStorageManager, self).info() + ": My major data structure is a " + self._data.__class__.__name__


class IgnoreWordManager(WFExercise):
    def __init__(self):
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(',')
        self._ignore_words.extend(list(string.ascii_lowercase))

    def is_ignore_word(self, word):
        return word in self._ignore_words

    def info(self):
        return super(IgnoreWordManager, self).info() + ": My major data structure is a " + self._ignore_words.__class__.__name__


class WordFrequencyManager(WFExercise):
    def __init__(self):
        self._word_freqs = {}

    def increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def sorted(self):
        return sorted(self._word_freqs.items(), key=operator.itemgetter(1), reverse=True)

    def info(self):
        return super(WordFrequencyManager, self).info() + ": My major data structure is a " + self._word_freqs.__class__.__name__


class WordFrequencyController(WFExercise):
    def __init__(self, path):
        self._storage_manager = DataStorageManager(path)
        self._ignore_word_manager = IgnoreWordManager()
        self._word_freq_manager = WordFrequencyManager()

    def run(self):
        for w in self._storage_manager.words():
            if not self._ignore_word_manager.is_ignore_word(w):
                self._word_freq_manager.increment_count(w)
        word_freqs = self._word_freq_manager.sorted()
        for (w, c) in word_freqs[0:25]:
            print(f'{w} - {c}')


WordFrequencyController(sys.argv[1]).run()