###############################################################################
# @brief    Python3 - Pickle module.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
'''

import pickle


class TestClass():
    def __str__(self):
        return 'HoYa'


if __name__ == '__main__':
    obj1 = TestClass()
    print(obj1)

    pickled = pickle.dumps(obj1)
    print(pickled)

    obj2 = pickle.loads(pickled)
    print(obj2)
