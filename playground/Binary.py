###############################################################################
# @brief    Python3 - Binary Data.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.17 - Created.
###############################################################################

'''
Byte is immutable.
Byte array is mutable.
'''

if __name__ == '__main__':
    testList = [1, 2, 3, 255]
    testBytes = bytes(testList)
    testByteArray = bytearray(testList)
    print(testBytes)
    print(testByteArray)
