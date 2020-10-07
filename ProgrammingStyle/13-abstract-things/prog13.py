#!/usr/bin/python3

import os
import sys
import abc
import re
import string
import operator
from pathlib import Path


class IDataStorage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def words(self):
        pass


class IIgnoreWordFilter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_ignore_word(self, word):
        pass


class IWordFrequencyCounter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def increment_count(self, word):
        pass

    @abc.abstractmethod
    def sorted(self):
        pass


class DataStorageManager:
    _data = ""

    def __init__(self, path):
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()
        self._data = "".join(self._data).split()

    def words(self):
        return self._data


class IgnoreWordManager:
    _ignore_words = []

    def __init__(self):
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(",")
        self._ignore_words.extend(list(string.ascii_lowercase))

    def is_ignore_word(self, word):
        return word in self._ignore_words


class WordFrequencyManager:
    _word_freqs = {}

    def increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def sorted(self):
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )


IDataStorage.register(DataStorageManager)
IIgnoreWordFilter.register(IgnoreWordManager)
IWordFrequencyCounter.register(WordFrequencyManager)


class WordFrequencyController:
    def __init__(self, path):
        self._storage = DataStorageManager(path)
        self._ignore_word_manager = IgnoreWordManager()
        self._word_freq_counter = WordFrequencyManager()

    def run(self):
        for w in self._storage.words():
            if not self._ignore_word_manager.is_ignore_word(w):
                self._word_freq_counter.increment_count(w)

        word_freqs = self._word_freq_counter.sorted()
        for (w, c) in word_freqs[0:25]:
            print(f"{w} - {c}")


WordFrequencyController(sys.argv[1]).run()