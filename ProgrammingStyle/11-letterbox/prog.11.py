#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


class DataStorageMangager:
    def dispatch(self, message):
        if message[0] == "init":
            return self._init(message[1])
        elif message[0] == "words":
            return self._words()
        else:
            raise Exception(f"Message not understood {message[0]}")

    def _init(self, path):
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def _words(self):
        data_str = "".join(self._data)
        return data_str.split()


class IgnoreWordManager:
    _ignore_words = []

    def dispatch(self, message):
        if message[0] == "init":
            return self._init()
        elif message[0] == "is_ignore_word":
            return self._is_ignore_word(message[1])
        else:
            raise Exception(f"Message not understood {message[0]}")

    def _init(self):
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(",")
        self._ignore_words.extend(list(string.ascii_lowercase))

    def _is_ignore_word(self, word):
        return word in self._ignore_words


class WordFrequencyManager:
    _word_freqs = {}

    def dispatch(self, message):
        if message[0] == "increment_count":
            return self._increment_count(message[1])
        elif message[0] == "sorted":
            return self._sorted()
        else:
            raise Exception(f"Message not understood {message[0]}")

    def _increment_count(self, word):
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def _sorted(self):
        return sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )


class WordFrequencyController:
    def dispatch(self, message):
        if message[0] == "init":
            return self._init(message[1])
        elif message[0] == "run":
            return self._run()
        else:
            raise Exception(f"Message not understood {message[0]}")

    def _init(self, path):
        self._storage_manager = DataStorageMangager()
        self._ignore_word_manager = IgnoreWordManager()
        self._word_freq_manager = WordFrequencyManager()
        self._storage_manager.dispatch(["init", path])
        self._ignore_word_manager.dispatch(["init"])

    def _run(self):
        for w in self._storage_manager.dispatch(["words"]):
            if not self._ignore_word_manager.dispatch(["is_ignore_word", w]):
                self._word_freq_manager.dispatch(["increment_count", w])

        word_freqs = self._word_freq_manager.dispatch(["sorted"])
        for (w, c) in word_freqs[0:25]:
            print(f"{w} - {c}")


wfcontroller = WordFrequencyController()
wfcontroller.dispatch(["init", sys.argv[1]])
wfcontroller.dispatch(["run"])
