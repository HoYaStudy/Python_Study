import http.client
import json
import pickle
import random
from pathlib import Path


class CLotto:
    _mFilename = "WonNumberLists.data"

    def GetWonNumber(self, _index):
        dataset = self._MakeDataset(_index + 1)
        pool = self._MakePool(dataset, _index + 1, 1)
        print(pool)

    def DrawNumber1(self, _index, _count):
        dataset = self._MakeDataset(_index)
        pool3 = self._MakePool(dataset, _index, 3)
        poolN = []
        for i in range(1, 46):
            if i not in pool3:
                poolN.append(i)
        pool3 = list(set(pool3))
        numLists = []
        i = 0
        while i < _count:
            numList = []
            j = 0
            check = {'even': 0, 'odd': 0,
                     '1': 0, '10': 0, '20': 0, '30': 0, '40': 0}
            while j < 6:
                if j < 2:
                    number = random.choice(pool3)
                else:
                    number = random.choice(poolN)
                if self._CheckDuplicate(number, numList):
                    continue
                if self._CheckEvenOdd(number, check):
                    continue
                if self._CheckNumber(number, check):
                    continue
                numList.append(number)
                j += 1
            numList.sort()
            numLists.append(numList)
            i += 1
        return numLists

    def DrawNumber2(self, _index, _count):
<<<<<<< Updated upstream
        dataset = self._MakeDataset(_index)
        pool5 = self._MakePool(dataset, _index, 5)
=======
        dataset = self.MakeDataset(_index)
        pool3 = self._MakePool(dataset, _index, 3)
>>>>>>> Stashed changes
        pool10 = self._MakePool(dataset, _index, 10)
        numLists = []
        i = 0
        while i < _count:
            numList = []
            j = 0
            check = {'even': 0, 'odd': 0,
                     '1': 0, '10': 0, '20': 0, '30': 0, '40': 0}
            while j < 6:
                if j < 3:
                    number = random.choice(pool5)
                else:
                    number = random.choice(pool10)
                if self._CheckDuplicate(number, numList):
                    continue
                if self._CheckEvenOdd(number, check):
                    continue
                if self._CheckNumber(number, check):
                    continue
                numList.append(number)
                j += 1
            numList.sort()
            numLists.append(numList)
            i += 1
        return numLists

    def DrawNumber3(self, _index, _count):
        dataset = self._MakeDataset(_index)
        pool3 = self._MakePool(dataset, _index, 3)
        pool3 = list(set(pool3))
        pool45 = [x for x in range(1, 46)]
        numLists = []
        i = 0
        for i in range(_count):
            pool = []
            for j in range(10):
                numList = []
                check = {'even': 0, 'odd': 0,
                         '1': 0, '10': 0, '20': 0, '30': 0, '40': 0}
                for k in range(6):
                    if k < 3:
                        number = self._GetNumber(pool3, numList, check)
                    else:
                        number = self._GetNumber(pool45, numList, check)
                    numList.append(number)
                pool.extend(numList)
            numList = []
            check = {'even': 0, 'odd': 0,
                     '1': 0, '10': 0, '20': 0, '30': 0, '40': 0}
            for k in range(6):
                numList.append(self._GetNumber(pool, numList, check))
            numList.sort()
            numLists.append(numList)
        return numLists

    def _GetWonNumber(self, _index):
        conn = http.client.HTTPConnection("www.nlotto.co.kr")
        conn.request("GET", "/common.do?method=getLottoNumber&drwNo="
                     + str(_index))
        rsp = conn.getresponse()
        json_data = rsp.read()
        conn.close()

        dict_data = json.loads(json_data.decode('utf-8'))
        return dict_data

    def _SaveDataset(self, _data):
        with open(self._mFilename, "wb") as f:
            pickle.dump(_data, f)

    def _LoadDataset(self):
        with open(self._mFilename, "rb") as f:
            dataset = pickle.load(f)
        return dataset

    def _MakeDataset(self, _index):
        dataset = []
        datalen = 0

        if Path(self._mFilename).is_file():
            dataset = self._LoadDataset()
            datalen = len(dataset)

        datalen += 1
        if datalen < _index:
            for i in range(datalen, _index):
                dataset.append(self._GetWonNumber(i))
            self._SaveDataset(dataset)
        return dataset

    def _MakePool(self, _dataset, _index, _range):
        pool = []
        for i in range(_index, _index - _range, -1):
            pool.append(_dataset[i - 2]['drwtNo1'])
            pool.append(_dataset[i - 2]['drwtNo2'])
            pool.append(_dataset[i - 2]['drwtNo3'])
            pool.append(_dataset[i - 2]['drwtNo4'])
            pool.append(_dataset[i - 2]['drwtNo5'])
            pool.append(_dataset[i - 2]['drwtNo6'])
        return pool

    def _CheckDuplicate(self, _number, _numList):
        if _number in _numList:
            return True
        return False

    def _CheckEvenOdd(self, _number, _check):
        if _number % 2 == 0:
            if _check['even'] > 3:
                return True
            _check['even'] += 1
        else:
            if _check['odd'] > 3:
                return True
            _check['odd'] += 1
        return False

    def _CheckNumber(self, _number, _check):
        if 0 < _number < 10:
            if _check['1'] > 2:
                return True
            _check['1'] += 1
        elif 10 <= _number < 20:
            if _check['10'] > 2:
                return True
            _check['10'] += 1
        elif 20 <= _number < 30:
            if _check['20'] > 2:
                return True
            _check['20'] += 1
        elif 30 <= _number < 40:
            if _check['30'] > 2:
                return True
            _check['30'] += 1
        elif 40 <= _number < 46:
            if _check['40'] > 2:
                return True
        return False

    def _GetNumber(self, _pool, _list, _check):
        while True:
            number = random.choice(_pool)
            if self._CheckDuplicate(number, _list):
                continue
            if self._CheckEvenOdd(number, _check):
                continue
            if self._CheckNumber(number, _check):
                continue
            break
        return number
