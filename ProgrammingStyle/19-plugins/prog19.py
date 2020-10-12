#!/usr/bin/python3

import os
import sys
import importlib.machinery
import configparser
from pathlib import Path


def load_plugins():
    config = configparser.ConfigParser()
    config.read(os.path.join(Path.cwd(), "19-plugins/config.ini"))
    words_plugin = config.get("Plugins", "words")
    frequencies_plugin = config.get("Plugins", "frequencies")
    global wfwords, wffreqs
    wfwords = importlib.machinery.SourcelessFileLoader(
        "wfwords", os.path.join(Path.cwd(), "19-plugins", words_plugin)
    ).load_module()
    wffreqs = importlib.machinery.SourcelessFileLoader(
        "wffreqs", os.path.join(Path.cwd(), "19-plugins", frequencies_plugin)
    ).load_module()


load_plugins()
word_freqs = wffreqs.top25(wfwords.extract_words(sys.argv[1]))
for (w, c) in word_freqs:
    print(f"{w} - {c}")
