###############################################################################
# @brief    Python3 - Tuple type.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.08 - Created.
###############################################################################

'''
Tuple is an one of sequence type.
Tuple is Immutable.
Tuple use for key of dictionary.
Function arguments are passed by tuple.
'''

if __name__ == '__main__':
    # Create Tuple -----------------------------------------------------------#
    # () method
    emptyTuple = ()
    weekdayList = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')

    # Literal
    weekdayList = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'

    # from List
    testList = ['red', 'green', 'blue']
    testTuple = tuple(testList)
    print(testTuple)

    # Get Item from Tuple ----------------------------------------------------#
    # unpacking
    d1, d2, d3, d4, d5 = weekdayList
    print(d1, d2, d3, d4, d5)

    # [index]
    print(weekdayList[2])
