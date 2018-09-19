###############################################################################
# @brief    Python3 - List type.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.07.19 - Created.
###############################################################################

'''
List is an one of sequence type.
List is Mutable.
'''

if __name__ == '__main__':
    # Create List ------------------------------------------------------------#
    # [] method
    emptyList = []
    weekdayList = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    nameList1 = ['Kim', 'Lee', 'Park', 'Kim']    # Duplication is OK.
    nameList2 = ['Kirara', 'Mikami', 'Mari']

    # Type Constructor - list() function
    emptyList = list()
    stringList = list('cat')    # ['c', 'a', 't']
    print(stringList)

    # Comprehension
    numberList = [number for number in range(1, 6)]
    print(numberList)

    numberList = [number for number in range(1, 6) if number % 2 == 1]
    print(numberList)

    rows = range(1, 4)
    cols = range(1, 3)
    cells = [(row, col) for row in rows for col in cols]
    print(cells)

    # from Tuple
    testTuple = ('red', 'green', 'blue')
    testList = list(testTuple)
    print(testList)

    # from string
    birthday = '1982/01/28'
    testList = birthday.split('/')
    print(testList)

    # Extend List
    nameList = []
    nameList += nameList1
    print(nameList)

    nameList.extend(nameList2)
    print(nameList)

    # Nested List
    nestedList = [nameList1, nameList2]
    print(nestedList)

    # Get Item from List -----------------------------------------------------#
    # [index]
    print(weekdayList[0], weekdayList[3], weekdayList[-1])
    print(nestedList[1][0])

    # slice
    print(weekdayList[1:3])
    print(weekdayList[::-2])

    # Set Item to List -------------------------------------------------------#
    nameList[3] = 'Choi'
    print(nameList)

    # Add Item to List -------------------------------------------------------#
    # append()
    nameList1.append('Kang')
    print(nameList1)
    nameList = []
    nameList += nameList1
    nameList.append(nameList2)
    print(nameList)

    # insert
    nameList1.insert(2, 'Song')
    print(nameList1)

    # Remove Item from List --------------------------------------------------#
    # del
    del nameList1[4]
    print(nameList1)

    # remove()
    nameList1.remove('Kang')
    print(nameList1)

    # pop()
    item = nameList1.pop()
    print(item, nameList1)

    # Etc. -------------------------------------------------------------------#
    # index
    print(nameList1.index('Kim'))

    # in
    print('Park' in nameList1)

    # count
    print(nameList1.count('Lee'))

    # join
    print(', '.join(nameList1))

    # sort
    sortedList = sorted(nameList2)
    print(nameList2)
    print(sortedList)
    nameList2.sort()
    print(nameList2)
    nameList2.sort(reverse=True)
    print(nameList2)

    # len
    print(len(nameList1))

    # copy
    copiedList1 = nameList1         # same as nameList1
    copiedList2 = nameList1.copy()  # different
    copiedList3 = list(nameList1)   # different
    copiedList4 = nameList1[:]      # different
    nameList1[0] = 'choi'
    print(copiedList1)
    print(copiedList2)
    print(copiedList3)
    print(copiedList4)
