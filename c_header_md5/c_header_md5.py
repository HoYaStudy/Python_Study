#!/usr/bin/env  python3
###############################################################################
# @brief    Create MD5 hash to C header file.
# @author	llChameleoNll (hoya128@gmail.com)
# @version	v1.0
# @note
#   2017.05.23 - Created
###############################################################################

# Import Module --------------------------------------------------------------#
import sys
import os
import hashlib
import re


# Global Function ------------------------------------------------------------#
def usage():
    """This function prints a usage message"""
    print("Usage: python3 c_header_md5.py <dir>")


def searchDirectory(_dirname):
    """This function searches header file from input directory"""
    for (path, dirnames, filenames) in os.walk(_dirname):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == ".h":
                fullname = os.path.join(path, filename)
                md5 = makeMD5(fullname)
                updateMD5(fullname, md5)

                if os.path.isfile(fullname + ".tmp"):
                    os.remove(fullname + ".tmp")


def makeMD5(_filename):
    """This function makes MD5 hash of input file"""
    # Make File for MD5
    with open(_filename, 'r') as rfp, open(_filename + ".tmp", 'w') as wfp:
        while True:
            line = rfp.readline()
            if not line:
                break

            if ("#ifndef" in line or "#define" in line) \
                    and (line[-3:-1] == "__"):
                p = re.compile('\w{32}')
                if p.match(line[-35:-3]):
                    line = line[:-35] + line[-2:]
            wfp.write(line)

    # Calculate MD5
    md5 = hashlib.md5()
    with open(_filename + ".tmp", 'rb') as fp:
        while True:
            buf = fp.read(8192)
            if not buf:
                break
            md5.update(buf)

    return md5.hexdigest()


def updateMD5(_filename, _md5):
    """This function update MD5 hash to input file"""
    with open(_filename, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break

            if "#ifndef" in line and line[-3:-1] == "__":
                p = re.compile('\w{32}')
                if _md5 == line[-35:-3]:
                    print("  " + _filename + ": Unchanged")
                elif p.match(line[-35:-3]):
                    print("  " + _filename + ": Modified")
                    addMD5(_filename, _md5)
                else:
                    print("  " + _filename + ": Added")
                    addMD5(_filename, _md5)


def addMD5(_filename, _md5):
    """This function adds MD5 to input file"""
    with open(_filename + ".tmp", 'r') as rfp, open(_filename, 'w') as wfp:
        while True:
            line = rfp.readline()
            if not line:
                break

            if ("#ifndef" in line or "#define" in line) \
                    and (line[-3:-1] == "__"):
                mline = line[:-3] + "_" + _md5 + line[-3:]
                wfp.writelines(mline)
            else:
                wfp.writelines(line)


# Main Function --------------------------------------------------------------#
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1 or argc > 2:
        usage()
        sys.exit(1)

    searchDirectory(sys.argv[1])
