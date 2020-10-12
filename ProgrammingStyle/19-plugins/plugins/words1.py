import os
import re
import string
from pathlib import Path


def extract_words(path):
    with open(path) as f:
        str_data = f.read()
    pattern = re.compile("[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
        ignore_words = f.read().split(",")
    ignore_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in ignore_words]