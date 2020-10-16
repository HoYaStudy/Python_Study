#!/usr/bin/python3

import sys
import re
import string
import operator
from pathlib import Path
from threading import Thread
from queue import Queue


class ActiveWFObject(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = str(type(self))
        self.queue = Queue()
        self._stop_me = False
        self.start()

    def run(self):
        while not self._stop_me:
            message = self.queue.get()
            self._dispatch(message)
            if message[0] == "die":
                self._stop_me = True


def send(receiver, message):
    receiver.queue.put(message)


class WordFrequencyManager(ActiveWFObject):
    _word_freqs = {}

    def _dispatch(self, message):
        if message[0] == "word":
            self._increment_count(message[1:])
        elif message[0] == "top25":
            self._top25(message[1:])

    def _increment_count(self, message):
        word = message[0]
        if word in self._word_freqs:
            self._word_freqs[word] += 1
        else:
            self._word_freqs[word] = 1

    def _top25(self, message):
        recipient = message[0]
        freqs_sorted = sorted(
            self._word_freqs.items(), key=operator.itemgetter(1), reverse=True
        )
        send(recipient, ["top25", freqs_sorted])


class IgnoreWordManager(ActiveWFObject):
    _ignore_words = []

    def _dispatch(self, message):
        if message[0] == "init":
            self._init(message[1:])
        elif message[0] == "filter":
            return self._filter(message[1:])
        else:
            send(self._word_freqs_manager, message)

    def _init(self, message):
        with open(Path.joinpath(Path.cwd(), "res/ignore-words.txt")) as f:
            self._ignore_words = f.read().split(",")
        self._ignore_words.extend(list(string.ascii_lowercase))
        self._word_freqs_manager = message[0]

    def _filter(self, message):
        word = message[0]
        if word not in self._ignore_words:
            send(self._word_freqs_manager, ["word", word])


class DataStorageManager(ActiveWFObject):
    _data = ""

    def _dispatch(self, message):
        if message[0] == "init":
            self._init(message[1:])
        elif message[0] == "send_word_freqs":
            self._process_words(message[1:])
        else:
            send(self._ignore_word_manager, message)

    def _init(self, message):
        path = message[0]
        self._ignore_word_manager = message[1]
        with open(path) as f:
            self._data = f.read()
        pattern = re.compile("[\W_]+")
        self._data = pattern.sub(" ", self._data).lower()

    def _process_words(self, message):
        recipient = message[0]
        data_str = "".join(self._data)
        words = data_str.split()
        for w in words:
            send(self._ignore_word_manager, ["filter", w])
        send(self._ignore_word_manager, ["top25", recipient])


class WordFrequencyController(ActiveWFObject):
    def _dispatch(self, message):
        if message[0] == "run":
            self._run(message[1:])
        elif message[0] == "top25":
            self._display(message[1:])
        else:
            raise Exception(f"Message not understood {message[0]}")

    def _run(self, message):
        self._storage_manager = message[0]
        send(self._storage_manager, ["send_word_freqs", self])

    def _display(self, message):
        word_freqs = message[0]
        for (w, f) in word_freqs[:25]:
            print(f"{w} - {f}")
        send(self._storage_manager, ["die"])
        self._stop_me = True


word_freq_manager = WordFrequencyManager()

ignore_word_manager = IgnoreWordManager()
send(ignore_word_manager, ["init", word_freq_manager])

storage_manager = DataStorageManager()
send(storage_manager, ["init", sys.argv[1], ignore_word_manager])

wfcontroller = WordFrequencyController()
send(wfcontroller, ["run", storage_manager])

[
    t.join()
    for t in [word_freq_manager, ignore_word_manager, storage_manager, wfcontroller]
]
