#!/usr/bin/python3

import os
import sys
import re
import string
import sqlite3
from pathlib import Path


def create_db_schema(db):
    c = db.cursor()
    c.execute("""CREATE TABLE documents (id INTEGER PRIMARY KEY AUTOINCREMENT, name)""")
    c.execute("""CREATE TABLE words (id, doc_id, value)""")
    c.execute("""CREATE TABLE characters (id, word_id, value)""")
    db.commit()
    c.close()


def load_file_into_database(path, db):
    def _extract_words(path):
        with open(path) as f:
            str_data = f.read()
        pattern = re.compile("[\W_]+")
        word_list = pattern.sub(" ", str_data).lower().split()
        with open(os.path.join(Path.cwd(), "res/ignore-words.txt")) as f:
            ignore_words = f.read().split(",")
        ignore_words.extend(list(string.ascii_lowercase))
        return [w for w in word_list if not w in ignore_words]

    words = _extract_words(path)

    c = db.cursor()
    c.execute("INSERT INTO documents (name) VALUES (?)", (path,))
    c.execute("SELECT id from documents WHERE name=?", (path,))
    doc_id = c.fetchone()[0]

    c.execute("SELECT MAX(id) FROM words")
    row = c.fetchone()
    word_id = row[0]
    if word_id == None:
        word_id = 0
    for w in words:
        c.execute("INSERT INTO words VALUES (?, ?, ?)", (word_id, doc_id, w))
        char_id = 0
        for char in w:
            c.execute(
                "INSERT INTO characters VALUES (?, ?, ?)", (char_id, word_id, char)
            )
            char_id += 1
        word_id += 1
    db.commit()
    c.close()


if not os.path.isfile("wf.db"):
    with sqlite3.connect("wf.db") as db:
        create_db_schema(db)
        load_file_into_database(sys.argv[1], db)

with sqlite3.connect("wf.db") as db:
    c = db.cursor()
    c.execute("SELECT value, COUNT(*) as C FROM words GROUP BY value ORDER BY C DESC")
    for i in range(25):
        row = c.fetchone()
        if row != None:
            print(f"{row[0]} - {str(row[1])}")
