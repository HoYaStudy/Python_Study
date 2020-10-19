#!/usr/bin/python3

import sys
import re
import operator
import collections
from pathlib import Path


class WordFrequenciesModel:
    freqs = {}
    ignore_words = set(
        open(Path.joinpath(Path.cwd(), "res/ignore-words.txt")).read().split(",")
    )

    def __init__(self, path):
        self.update(path)

    def update(self, path):
        try:
            words = re.findall("[a-z]{2,}", open(path).read().lower())
            self.freqs = collections.Counter(
                w for w in words if w not in self.ignore_words
            )
        except IOError:
            print("File not found")
            self.freqs = ()


class WordFrequenciesView:
    def __init__(self, model):
        self._model = model

    def render(self):
        sorted_freqs = sorted(
            self._model.freqs.items(), key=operator.itemgetter(1), reverse=True
        )
        for (w, c) in sorted_freqs[:25]:
            print(f"{w} - {c}")


class WordFrequenciesController:
    def __init__(self, model, view):
        self._model, self._view = model, view
        view.render()

    def run(self):
        # while True:
        #     print("Next file: ")
        #     sys.stdout.flush()
        #     filename = sys.stdin.readline().strip()
        #     self._model.update(filename)
        #     self._view.render()
        pass


m = WordFrequenciesModel(sys.argv[1])
v = WordFrequenciesView(m)
c = WordFrequenciesController(m, v)
c.run()