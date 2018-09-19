###############################################################################
# @brief    Python3 - Namespace.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.09 - Created.
###############################################################################

'''
'''

fruit = 'apple'


def func1():
    fruit = 'peach'
    print('locals: ', locals())


def func2():
    global fruit
    fruit = 'banana'
    print('locals: ', locals())


if __name__ == '__main__':
    print('globals: ', globals())
    func1()
    func2()
    print('globals: ', globals())
