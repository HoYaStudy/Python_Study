###############################################################################
# @brief    Python3 - Input/Output.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.07.18 - Created.
###############################################################################

'''
Formatting
 - %s : string
 - %d : decimal
 - %x : jexadecimal
 - %o : octal
 - %f : floating point
 - %e : exponent notation
 - %g : general format
 - %% : literal %
'''

if __name__ == '__main__':
    # Input ------------------------------------------------------------------#
    print("### Input Study ###")
    user_input = input("Input integer data: ")
    print(user_input)
    print()

    # Output -----------------------------------------------------------------#
    print("### Output Study ###")
    print('Hello World')
    print("I'm HoYa.")
    print('"Nice to meet you!"')
    print(7, 'Hello', 'World')
    print('7 ' 'Hello ' 'World')
    print('7 ' + 'Hello ' + 'World')
    print('Hey ' * 3)
    print('This\tis\n test string. \", \', \\.')
    print('')

    # Formatting - OLD version
    print('%s' % 'Hello World!')
    print('%d%%' % 100)
    print('%f' % 3.14)
    print('%10d' % 7)               # right alignment
    print('%-10d' % 7)              # left alignment
    print('%10.4d' % 7)             # limit number of ciphers
    print('%*.*d' % (10, 4, 7))     # same as above

    # Formatting - NEW version
    print('{}, {}, {}'.format('test', 100, 3.14))
    print('{2}, {0}, {1}'.format('test', 100, 3.14))
    print('{v1}, {v2}, {v3}'.format(v1='test', v2=100, v3=3.14))

    testDict = {'k1': 'test', 'k2': 100, 'k3': 3.14}
    print('{0[k1]} {0[k2]} {0[k3]} {1}'.format(testDict, 'other'))
    print('{n:d} {f:f} {s:s}'.format(s='test', n=100, f=3.14))
    print('{0:<10d} {1:<10f} {2:<10s}'.format(100, 3.14, 'test'))   # right
    print('{0:>10d} {1:>10f} {2:>10s}'.format(100, 3.14, 'test'))   # left
    print('{0:^10d} {1:^10f} {2:^10s}'.format(100, 3.14, 'test'))   # center
    print('{0:#^20s}'.format(' TEST '))

    # Separator and End String
    print('Test1', end='')
    print('Test2')
    print('Test1', 'Test2', 'Test3', sep=':')
