###############################################################################
#   @brief      Caesar Cipher algorithm
#   @author     llHoYall <hoya128@gmail.com>
#   @version    v1.0
#   @note
#       - 2018.09.19    Created.
###############################################################################

SHIFT = 1


def encrypt(raw):
    ret = ''
    for char in raw:
        ret += chr(ord(char) + SHIFT)
    return ret


def decrypt(raw):
    ret = ''
    for char in raw:
        ret += chr(ord(char) - SHIFT)
    return ret


if __name__ == '__main__':
    raw = input('input: ')
    encrypted = encrypt(raw)
    print('Encrypted: ' + encrypted)
    decrypted = decrypt(encrypted)
    print('Decrypted: ' + decrypted)
