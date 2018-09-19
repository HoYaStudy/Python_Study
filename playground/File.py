###############################################################################
# @brief    Python3 - File.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
Open
    r   read
    w   write create or overwrite
    x   write when file not found
    a   append

    t   text type
    b   binary type

Seek
    seek(offset, origin)
    origin 0    Start position (os.SEEK_SET)
    origin 1    Current position (os.SEEK_CUR1)
    origin 2    End position (os.SEEK_END)
'''

if __name__ == '__main__':
    # Open & Close -----------------------------------------------------------#
    print("### File Open/Close Study ###")
    fp = open('file.txt', 'rb')
    fp.close()

    # Automatically close when end or error
    with open('file.txt', 'wt') as fp:
        fp.write('Test')

    # Write ------------------------------------------------------------------#
    print("### File Write Study ###")
    fp = open('file.txt', 'wt')
    str = 'Test File - Line 1'
    print(str, file=fp)             # with new line
    fp.write('Test File - Line 2')  # without new line
    fp.close()

    # Read -------------------------------------------------------------------#
    # Read whole file
    print("### File Read Study ###")
    fp = open('file.txt', 'rt')
    print(fp.read())
    fp.close()
    print('')

    # Read wanted
    fp = open('file.txt', 'rt')
    print(fp.read(3))
    fp.close()
    print('')

    # Read one lines
    fp = open('file.txt', 'rt')
    while True:
        fbuf = fp.readline()
        print(fbuf)
        if not fbuf:
            break
    fp.close()

    # Read whole lines to list
    fp = open('file.txt', 'rt')
    print(fp.readlines())
    fp.close()

    # Seek -------------------------------------------------------------------#
    bdata = bytes(range(0, 255))
    fp = open('file.txt', 'wb')
    fp.write(bdata)
    fp.close()

    fp = open('file.txt', 'rb')
    print(fp.tell())
    fp.seek(127)
    print(fp.tell())
