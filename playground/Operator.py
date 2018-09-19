###############################################################################
# @brief    Python3 - Operator.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.07.18 - Created.
###############################################################################

'''
These are all False.
- null
- 0     (Integer)
- 0.0   (Floating Point)
- ''    (Empty String)
- []    (Empty List)
- ()    (Empty Tuple)
- {}    (Empty Dictionary)
- set() (Empty Set)
'''

if __name__ == '__main__':
    # Addition
    addition = 1 + 2
    print(addition)
    addition += 2
    print(addition)
    print()

    # Subtraction
    subtraction = 5 - 3
    print(subtraction)
    subtraction -= 1
    print(subtraction)
    print()

    # Multiplication
    multiplication = 4 * 6
    print(multiplication)
    multiplication *= 2
    print(multiplication)
    print()

    # Power
    power = 4 ** 2
    print(power)
    power **= 2
    print(power)
    print()

    # True Division
    true_division = 8 / 3
    print(true_division)
    true_division /= 2
    print(true_division)
    print()

    # Floor Division
    floor_division = 9 // 3
    print(floor_division)
    floor_division //= 3
    print(floor_division)
    print()

    # Remainder
    remainder = 11 % 6
    print(remainder)
    remainder %= 3
    print(remainder)
    print()

    # quotient, remainder
    print(divmod(9, 5))
    print()

    # Comparison
    print('Hello' == 'Hi')
    print('Hello' != 'World')
    print(1 < 3)
    print(7 <= 3)
    print(3 > 6)
    print(7 >= 5)
    print(2 in range(5))

    # Logical
    print(True and False)
    print(True or False)
    print(not True)
