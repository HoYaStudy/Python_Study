#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


class WordFrequencyFramework:
    _load_event_handlers = []
    _dowork_event_handlers = []
    _end_event_handlers = []

    def register_for_load_event(self, handler):
        self._load_event_handlers.append(handler)

    def register_for_dowork_event(self, handler):
        self._dowork_event_handlers.append(handler)

    def register_for_end_event(self, handler):
        self._end_event_handlers.append(handler)

    def run(self, path):
        for h in self._load_event_handlers:
            h(path)
        for h in self._dowork_event_handlers:
            h()
        for h in self._end_event_handlers:
            h()


class IgnoreWordFilter:
    _ignore_words = []

    def __init__(self, wfapp):
        wfapp.register_for_load_event(self.__load)

    def __load(self, not_used):
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(",")
        self._ignore_words.extend(list(string.ascii_lowercase))

    def is_ignore_word(self, word):
        return word in self._ignore_words


class DataStorage:
    _data = ""
    _ignore_word_filter = None
    _word_event_handlers = []

    def __init__(self, wfapp, ignore_word_filter):
        self._ignore_word_filter = ignore_word_filter
        wfapp.register_for_load_event(self.__load)
        wfapp.register_for_dowork_event(self.__produce_words)

    def __load(self, path):
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def __produce_words(self):
        data_str = "".join(self._data)
        for w in data_str.split():
            if not self._ignore_word_filter.is_ignore_word(w):
                for h in self._word_event_handlers:
                    h(w)

    def register_for_word_event(self, handler):
        self._word_event_handlers.append(handler)


class WordFrequencyCounter:
    _word_freqs = {}

    def __init__(self, wfapp, data_storage):
        data_storage.register_for_word_event(self.__increment_count)
        wfapp.register_for_end_event(self.__print_freqs)

    def __increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def __print_freqs(self):
        word_freqs = sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )
        for (w, c) in word_freqs[0:25]:
            print(f"{w} - {c}")


wfapp = WordFrequencyFramework()
ignore_word_filter = IgnoreWordFilter(wfapp)
data_storage = DataStorage(wfapp, ignore_word_filter)
word_freq_counter = WordFrequencyCounter(wfapp, data_storage)
wfapp.run(sys.argv[1])