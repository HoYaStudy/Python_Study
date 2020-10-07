#!/usr/bin/python3

import os
import sys
import re
import string
import operator
from pathlib import Path


class EventManager:
    def __init__(self):
        self._subscriptions = {}

    def subscribe(self, event_type, handler):
        if event_type in self._subscriptions:
            self._subscriptions[event_type].append(handler)
        else:
            self._subscriptions[event_type] = [handler]

    def publish(self, event):
        event_type = event[0]
        if event_type in self._subscriptions:
            for h in self._subscriptions[event_type]:
                h(event)


class DataStorage:
    def __init__(self, event_manager):
        self._event_manager = event_manager
        self._event_manager.subscribe("load", self.load)
        self._event_manager.subscribe("start", self.produce_words)

    def load(self, event):
        path = event[1]
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def produce_words(self, event):
        data_str = "".join(self._data)
        for w in data_str.split():
            self._event_manager.publish(("word", w))
        self._event_manager.publish(("eof", None))


class IgnoreWordFilter:
    def __init__(self, event_manager):
        self._ignore_words = []
        self._event_manager = event_manager
        self._event_manager.subscribe("load", self.load)
        self._event_manager.subscribe("word", self.is_ignore_word)

    def load(self, event):
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(",")
        self._ignore_words.extend(list(string.ascii_lowercase))

    def is_ignore_word(self, event):
        word = event[1]
        if word not in self._ignore_words:
            self._event_manager.publish(("valid_word", word))


class WordFrequencyCounter:
    def __init__(self, event_manager):
        self._word_freqs = {}
        self._event_manager = event_manager
        self._event_manager.subscribe("valid_word", self.increment_count)
        self._event_manager.subscribe("print", self.print_freqs)

    def increment_count(self, event):
        word = event[1]
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def print_freqs(self, event):
        word_freqs = sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )
        for (w, c) in word_freqs[0:25]:
            print(f"{w} - {c}")


class WordFrequencyApplication:
    def __init__(self, event_manager):
        self._event_manager = event_manager
        self._event_manager.subscribe("run", self.run)
        self._event_manager.subscribe("eof", self.stop)

    def run(self, event):
        path = event[1]
        self._event_manager.publish(("load", path))
        self._event_manager.publish(("start", None))

    def stop(self, event):
        self._event_manager.publish(("print", None))


em = EventManager()
DataStorage(em)
IgnoreWordFilter(em)
WordFrequencyCounter(em)
WordFrequencyApplication(em)
em.publish(("run", sys.argv[1]))
