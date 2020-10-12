import os
import re
from pathlib import Path


def extract_words(path):
    words = re.findall("[a-z]{2,}", open(path).read().lower())
    ignorewords = set(
        open(os.path.join(Path.cwd(), "res/ignore-words.txt")).read().split(",")
    )
    return [w for w in words if w not in ignorewords]