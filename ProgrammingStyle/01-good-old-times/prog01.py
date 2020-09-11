#!/usr/bin/python3

import os
import sys
import string
from pathlib import Path


data = []
with open(os.path.join(Path.cwd(), 'res/ignore-words.txt')) as f:
    data = [f.read(1024).split(',')]

data.append([])     # read line from input file
data.append(None)   # index of the start of word
data.append(0)      # index on characters
data.append(False)  # flag indicating if word was found
data.append('')     # current checking word
data.append('')     # number of current checking word (####)
data.append(0)      # frequency

if not os.path.exists(os.path.join(Path.cwd(), 'output')):
    os.mkdir('output')
with open(os.path.join(Path.cwd(), 'output/output.txt'), 'wb+') as fo:
    with open(os.path.join(Path.cwd(), sys.argv[1])) as fi:
        while True:
            data[1] = [fi.readline()]
            if data[1] == ['']:
                break
            if data[1][0][len(data[1][0]) - 1] != '\n':
                data[1][0] = data[1][0] + '\n'
            data[2] = None
            data[3] = 0

            for c in data[1][0]:
                if data[2] == None:
                    if c.isalnum():
                        data[2] = data[3]
                else:
                    if not c.isalnum():
                        data[4] = False
                        data[5] = data[1][0][data[2]:data[3]].lower()
                        if len(data[5]) >= 2 and data[5] not in data[0]:
                            while True:
                                data[6] = str(fo.readline().strip(), 'utf-8')
                                if data[6] == '':
                                    break
                                data[7] = int(data[6].split(',')[1])
                                data[6] = data[6].split(',')[0].strip()
                                if data[5] == data[6]:
                                    data[7] += 1
                                    data[4] = True
                                    break
                            if not data[4]:
                                fo.seek(0, 1)
                                fo.write(bytes(f'{data[5]:>20},{1:04}\n', 'utf-8'))
                            else:
                                fo.seek(-26, 1)
                                fo.write(bytes(f'{data[5]:>20},{data[7]:04}\n', 'utf-8'))
                            fo.seek(0, 0)
                        data[2] = None
                data[3] += 1
    fo.flush()

    del data[:]
    data = data + [[]] * (25 - len(data))
    data.append('')
    data.append(0)

    while True:
        data[25] = str(fo.readline().strip(), 'utf-8')
        if data[25] == '':
            break
        data[26] = int(data[25].split(',')[1])
        data[25] = data[25].split(',')[0].strip()
        for i in range(25):
            if data[i] == [] or data[i][1] < data[26]:
                data.insert(i, [data[25], data[26]])
                del data[26]
                break

    for result in data[0:25]:
        if len(result) == 2:
            print(f'{result[0]} - {result[1]}')