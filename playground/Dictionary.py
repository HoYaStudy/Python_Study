###############################################################################
# @brief    Python3 - Dictionary type.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.08 - Created.
###############################################################################

'''
Dictionary is unordered.
Dictionary is Mutable.
Dictionary has key-value pair.
Dictionary key must be unique.
'''

if __name__ == '__main__':
    # Create Dictionary ------------------------------------------------------#
    # {} method
    emptyDict = {}
    testDict = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    print(testDict)

    # dict() function
    testDict = dict([
        ['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']
    ])
    print(testDict)

    # Comprehension
    word = 'letters'
    letter_counts = {letter: word.count(letter) for letter in set(word)}
    print(letter_counts)

    # from Tuple
    testTuple = ('ab', 'cd', 'ef')      # possible only 2 characters
    testDict = dict(testTuple)
    print(testDict)

    # from List
    testList = ['ab', 'cd', 'ef']       # possible only 2 characters
    testDict = dict(testList)
    print(testDict)
    testList = [['r', 'red'], ['g', 'green'], ['b', 'blue']]
    testDict = dict(testList)
    print(testDict)

    # from Mixed type
    test = (['r', 'red'], ['g', 'green'], ['b', 'blue'])
    testDict = dict(test)
    print(testDict)
    test = [('r', 'red'), ('g', 'green'), ('b', 'blue')]
    testDict = dict(test)
    print(testDict)

    # Get Item from Dictionary -----------------------------------------------#
    testDict = {"key1": "value1", "key2": "value2", "key3": "value3"}

    # [key]
    print(testDict['key2'])

    # get()
    print(testDict.get('key3'))

    # keys()
    print(testDict.keys())

    # values()
    print(testDict.values())

    # items()
    print(testDict.items())

    # Set Item to Dictionary -------------------------------------------------#
    testDict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    testDict['key1'] = 'value11'
    print(testDict)

    # Add Item to Dictionary -------------------------------------------------#
    # update()
    testDict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
    testDict2 = {"key4": "value4", "key5": "value5"}
    testDict1.update(testDict2)
    print(testDict1)
    testDict3 = {"key2": "value22", "key6": "value6"}
    testDict1.update(testDict3)
    print(testDict1)

    # Remove Item from Dictionary --------------------------------------------#
    testDict = {"key1": "value1", "key2": "value2", "key3": "value3"}

    # del
    del testDict['key1']
    print(testDict)

    # clear()
    testDict.clear()
    print(testDict)

    # Etc. -------------------------------------------------------------------#
    testDict = {"key1": "value1", "key2": "value2", "key3": "value3"}

    # in
    print('key2' in testDict)

    # copy
    copiedDict1 = testDict          # same as testDict
    copiedDict2 = testDict.copy()   # different
    testDict['key2'] = 'value22'
    print(copiedDict1)
    print(copiedDict2)
