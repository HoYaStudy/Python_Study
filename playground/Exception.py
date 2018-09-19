###############################################################################
# @brief    Python3 - Namespace.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.09 - Created.
###############################################################################

'''
'''


class userException(Exception):
    pass


if __name__ == '__main__':
    print("### Exception Handling Study ###")
    testList = [1, 2, 3, 4, 5]
    try:
        testList[7]
    except:
        print('Out of range. Must be 0 ~', len(testList) - 1)

    while True:
        value = input('Input position [q to quit]: ')
        if value == 'q':
            break
        try:
            pos = int(value)
            print(testList[pos])
        except IndexError as err:
            print('Bad index: ', pos)
        except Exception as other:
            print('Something wrong: ', other)

    try:
        raise userException('ERROR')
    except userException as err:
        print(err)

    testList = ['a', 'b', 'C', 'd', 'e']
    for c in testList:
        if c.isupper():
            raise userException(c)

