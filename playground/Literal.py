###############################################################################
# @brief    Python3 - Literal.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.07.28 - Created.
###############################################################################

'''
Integer
- Don't start with 0 in Integer.
String
- String is Immutable.
'''


if __name__ == '__main__':
    # Integer ----------------------------------------------------------------#
    positive = +123   # same as 123
    negative = -123

    # String -----------------------------------------------------------------#
    strLiteral = 'hello'
    strLiteral = "world"

    strLiteral = "I'm HoYa."
    strLiteral = 'I\'m HoYa.'
    strLiteral = 'He say, "Melong"'
    strLiteral = "He say, \"Melong\""

    strLiteral = 'hello' + ' world'
    print(strLiteral)
    strLiteral = 'hey ' * 3
    print(strLiteral)
    strLiteral = "hello " "world"
    print(strLiteral)

    cnt = 5
    strLiteral = ''
    strLiteral += 'He is '
    strLiteral += str(cnt)
    strLiteral += ' years old.'
    print(strLiteral)

    strLiteral = '''Line 1,
 Line 2,
  Line 3'''
    print(strLiteral)
    strLiteral = """
  Line 11,
    Line 12,
     Line 13
  """
    print(strLiteral)

    string = 'abcdefghijklmnopqrstuvwxyz'
    print(string[3])
    print(string[-2])
#    string[50]         # Error
#    string[0] = 'A'    # Error

    # slice [start:end:step]
    print(string[:])
    print(string[5:])
    print(string[:7])
    print(string[10:15])
    print(string[10:20:2])
    print(string[::3])
    print(string[::-1])

    print(len(string))

    new_string = string.replace('a', 'A')
    print(new_string)

    string = 'a,b,c,d,e'
    new_string = string.split(',')
    print(new_string)

    string = 'ab cd ef gh ij'
    new_string = string.split()
    print(new_string)
    new_string = ', '.join(new_string)
    print(new_string)

    string = 'Lorem ipsum dolor sit amet'
    string.startswith('Lorem')  # True
    string.endswith('ipsum')    # False
    string.find('dolor')        # 12
    string.rfind('sit')         # 18
    string.count('or')          # 2
    string.isalnum()            # True

    string = 'lorem ipsum dolor sit amet...'
    new_string = string.strip('.')
    print(new_string)
    new_string = string.capitalize()
    print(new_string)
    new_string = string.title()
    print(new_string)
    new_string = string.upper()
    print(new_string)
    new_string = string.lower()
    print(new_string)
    new_string = string.swapcase()
    print(new_string)
    new_string = string.center(50)
    print(new_string)
    new_string = string.ljust(30)
    print(new_string)
    new_string = string.rjust(40)
    print(new_string)

    string = 'apple banana apple orange apple grape'
    new_string = string.replace('apple', 'melon')
    print(new_string)
    new_string = string.replace('apple', 'melon', 2)
    print(new_string)
