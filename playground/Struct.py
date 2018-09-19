###############################################################################
# @brief    Python3 - Struct modue.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
<   little endian
>   big endian

x   pad byte
b   signed char
B   unsigned char
h   signed short
H   unsigned Short
i   signed int
I   unsigned int
l   signed long
L   unsigned long
q   signed long long
Q   unsigned long long
f   float
d   double
p   char[] (count + characters)
s   char[] (characters)
'''
import struct


if __name__ == '__main__':
    data = 154
    struct.pack('>L', data)
