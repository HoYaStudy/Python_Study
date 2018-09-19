###############################################################################
# @brief    Python3 - Regular Expression.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.11 - Created.
###############################################################################

'''
. : one character except '\n'
* : previous character is more than 0
? : previous character is 0 or 1

\d : integer
\D : none integer
\w : alphabet
\W : none alphabet
\s : white space character
\S : none white space character
\b : word boundary
\B : none word boundary

Pattern Specifier
- abc               literal abc
- (expr)            expr
- expr1 | expr2     expr1 or expr2
- .                 all character except \n
- ^                 start of string
- $                 end of string
prev?               0 or 1 prev
prev*               0ȸ �̻��� �ִ� prev
prev*?              0ȸ �̻��� �ּ� prev
prev+               1ȸ �̻��� �ִ� prev
prev+?              1ȸ �̻��� �ּ� prev
prev{m}             mȸ prev
prev{m, n}          m~nȸ�� �ִ� prev
prev{m, n}?         m~nȸ�� �ּ� prev
[abc]               a or b or c
[^abc]              not a or b or c
prev(?=next)        �ڿ� next�� ���� prev
prev(?!next)        �ڿ� next�� ���� ������ prev
(?<=prev)next       �տ� prev�� ���� next
(?<!prev)next       �տ� prev�� ���� ������ next
'''

import re
import string


if __name__ == '__main__':
    print("### Regular Expression Study ###")
    source = 'Test String'

    # Match() ----------------------------------------------------------------#
    # Only start of source
    pattern = 'Test'
    ret = re.match(pattern, source)
    if ret:
        print('Matched: {}'.format(ret.group()))

    pattern = re.compile('Str')
    ret = pattern.match(source)
    if ret:
        print('Matched: {}'.format(ret.group()))

    # Search() ---------------------------------------------------------------#
    # Wherever
    ret = re.search('Str', source)
    if ret:
        print('Searched: {}'.format(ret.group()))

    # findall() --------------------------------------------------------------#
    # return list
    ret = re.findall('t', source)
    print(ret)
    print('Found', len(ret), 'matched')

    # split() ----------------------------------------------------------------#
    ret = re.split('t', source)
    print('Splitted:', ret)

    # sub() ------------------------------------------------------------------#
    ret = re.sub('t', '*', source)
    print('Substituted:', ret)

    # Special Character ------------------------------------------------------#
    printable = string.printable
    print(re.findall('\d', printable))
    print(re.findall('\w', printable))
    print(re.findall('\s', printable))

    unicode = 'abc' + '-/*' + '\u00ea' + '\u0115'
    print(re.findall('\w', unicode))
