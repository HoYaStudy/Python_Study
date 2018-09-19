###############################################################################
# @brief    Python3 - Collections.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.10 - Created.
###############################################################################

'''
'''

from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import deque


if __name__ == '__main__':
    # Named Tuple ------------------------------------------------------------#
    print("### Named Tuple Study ###")
    testTuple = namedtuple('Name', 'attr1 attr2')

    tuple1 = testTuple('data1', 'data2')
    print(tuple1)
    print(tuple1.attr1, tuple1.attr2)

    testDict = {'attr1': 'data3', 'attr2': 'data4'}
    tuple2 = testTuple(**testDict)
    print(tuple2)

    tuple3 = tuple2._replace(attr2='data6', attr1='data5')
    print(tuple3)
    print('')

    # {Dictionary}.setdefault() ----------------------------------------------#
    # Get if exist, Set if not exist.
    print("### {Dictionary}.setdefault() Study ###")
    testDict = {'key1': 'value1', 'key2': 'value2'}

    dict1 = testDict.setdefault('key3', 'value3')
    print(dict1)

    dict2 = testDict.setdefault('key2', 'value4')
    print(dict2)
    print('')

    # Default Dictionary -----------------------------------------------------#
    print("### Default Dictionary Study ###")
    # default 0
    dict3 = defaultdict(int)
    dict3['key1'] = 'value1'
    dict3['key2']
    print(dict3)

    # counter
    dict4 = defaultdict(int)
    for data in ['data1', 'data2', 'data1']:
        dict4[data] += 1
    for data, count in dict4.items():
        print(data, count)

    # default 'value0'
    dict4 = defaultdict(lambda: 'value0')
    dict4['key1']
    print(dict4)
    print('')

    # Ordered Dictionary -----------------------------------------------------#
    print("### Ordered Dictionary ###")
    testDict = OrderedDict([('key1', 'value1'),
                            ('key2', 'value2'),
                            ('key3', 'value3')])
    print(testDict)
    print('')

    # Counter ----------------------------------------------------------------#
    print("### Counter Study ###")
    testList1 = ['item1', 'item2', 'item1', 'item1']
    testCounter1 = Counter(testList1)
    print(testCounter1)

    testList2 = ['item2', 'item2', 'item3']
    testCounter2 = Counter(testList2)
    print(testCounter2)

    print(testCounter1 + testCounter2)
    print(testCounter1 - testCounter2)
    print(testCounter1 & testCounter2)
    print(testCounter1 | testCounter2)
    print('')

    # Deque ------------------------------------------------------------------#
    # Bidirectional stack & queue
    print("### Deque Study ###")

    def palindrome(word):
        dq = deque(word)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True

    print(palindrome(''))
    print(palindrome('a'))
    print(palindrome('racecar'))
    print(palindrome('test'))
