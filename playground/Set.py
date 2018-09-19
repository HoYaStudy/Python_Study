###############################################################################
# @brief    Python3 - Set type.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.08 - Created.
###############################################################################

'''
Set is unordered.
Set item must be unique.
'''

if __name__ == '__main__':
    # Create Set -------------------------------------------------------------#
    # {} method
    testSet = {1, 3, 5, 7, 9}
    print(testSet)

    # set() function
    emptySet = set()
    print(emptySet)

    # Comprehension
    testSet = {number for number in range(1, 6) if number % 2 == 1}
    print(testSet)

    # from String
    testSet = set('hello')
    print(testSet)

    # from Tuple
    testSet = set(('red', 'green', 'blue'))
    print(testSet)

    # from List
    testSet = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
    print(testSet)

    # from Dictionary
    testSet = set({'r': 'red', 'g': 'green', 'b': 'blue'})
    print(testSet)

    # Etc. -------------------------------------------------------------------#
    # in
    drinks = {
        'martini': {'vodka', 'vermouth'},
        'black russian': {'vodka', 'kahlua'},
        'white russian': {'cream', 'kahlua', 'vodka'},
        'manhaattan': {'rye', 'vermouth', 'bitters'},
        'screwdriver': {'orange juice', 'vodka'}
    }
    for name, contents in drinks.items():
        if 'vodka' in contents:
            print(name)
    for name, contents in drinks.items():
        if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
            print(name)
    for name, contents in drinks.items():
        if contents & {'vermouth', 'orange juice'}:
            print(name)

    # &, intersection()
    a = {1, 2}
    b = {2, 3}
    print(a & b)
    print(a.intersection(b))

    # |, union()
    print(a | b)
    print(a.union(b))

    # -, difference()
    print(a - b)
    print(a.difference(b))

    # ^, symmetric_difference()
    print(a ^ b)
    print(a.symmetric_difference(b))

    # <=, issubset()
    print(a <= b)
    print(a.issubset(b))

    # >=, issuperset()
    print(a >= b)
    print(a.issuperset(b))

    # < (proper subset), > (proper superset)
    print(a < b)
    print(a > b)
