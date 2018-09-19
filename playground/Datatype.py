###############################################################################
# @brief    Python3 - Datatype.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.07.19 - Created.
###############################################################################

if __name__ == '__main__':
    # default datatype -------------------------------------------------------#
    # Boolean
    print(True, type(True))
    print(False, type(False))
    print()

    # Integer
    print(0b10, type(0b10))   # binary
    print(0o10, type(0o10))   # octal
    print(10, type(10))       # decimal
    print(0x10, type(0x10))   # hexadecimal
    googol = 10 ** 100
    print(googol)   # Not Overflow!!
    print()

    # Float
    print(3.14, type(3.14))
    print()

    # String
    print('hello', type('hello'))
    print()

    # Type Casting -----------------------------------------------------------#
    print('True        ->', int(True))          # bool to int
    print('False       ->', int(False))         # bool to int
    print('1.414       ->', int(1.414))         # float to int
    print('1.0e4       ->', int(1.0e4))         # float to int
    print('3 + 4.0     ->', 3 + 4.0)            # float to int
    print("'59'        ->", int('59'))          # str to int
    print("'-23'       ->", int('-23'))         # str to int
#    print(int(''))           # Error
#    print(int('3.14'))       # Error
#    print(int('1.0e4'))      # Error
    print('True + 2    ->', int(True + 2))      # mixed to int
    print('False + 4.1 ->', int(False + 4.1))   # mixed to int
#    print(int('5 bottles'))  # Error
    print()

    print('True        ->', float(True))        # bool to float
    print('False       ->', float(False))       # bool to float
    print("'2.818'     ->", float('2.818'))     # str to float
    print("'-2.236'    ->", float('-2.236'))    # str to float
    print("'1.0e4'     ->", float('1.0e4'))     # str to float
    print()

    print('True        ->', str(True))          # bool to str
    print('False       ->', str(False))         # bool to str
    print('-3          ->', str(-3))            # int to str
    print('6.25        ->', str(6.25))          # float to str
    print('1.0e3       ->', str(1.0e3))         # float to str
