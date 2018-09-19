###############################################################################
# @brief    Python3 - OS module.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
'''

import os
import shutil
import glob
import subprocess

if __name__ == '__main__':
    # OS module --------------------------------------------------------------#
    # exists()
    print(os.path.exists('~/hWorkspace'))

    # isfile()
    print(os.path.isfile('OS.py'))

    # isdir()
    print(os.path.isdir('OS.py'))

    # isabs()
    print(os.path.isabs('.'))

    # rename(), remove()
    fp = open('from.txt', 'wt')
    fp.close()
    os.rename('from.txt', 'to.txt')
    os.remove('to.txt')

    # link(), islink()
    fp = open('from.txt', 'wt')
    fp.close()
    os.link('from.txt', 'to.txt')
    print(os.path.isfile('to.txt'))
    print(os.path.islink('to.txt'))
    os.remove('from.txt')
    os.remove('to.txt')

    # symlink(), realpath()
    fp = open('from.txt', 'wt')
    fp.close()
    os.symlink('from.txt', 'to.txt')
    print(os.path.islink('to.txt'))
    print(os.path.realpath('to.txt'))
    os.remove('from.txt')
    os.remove('to.txt')

    # chmod()
    fp = open('file.txt', 'wt')
    fp.close()
    os.chmod('file.txt', 0o400)
    os.remove('file.txt')

    # chown(), getuid(), getgid()
    fp = open('file.txt', 'wt')
    fp.close()
    uid = os.getuid()
    gid = os.getgid()
    os.chown('file.txt', uid, gid)
    os.remove('file.txt')

    # getpid(), getcwd()
    print(os.getpid())
    print(os.getcwd())

    # abspath()
    print(os.path.abspath('.'))

    # mkdir(), rmdir()
    os.mkdir('test_dir')
    print(os.path.exists('test_dir'))
    os.rmdir('test_dir')
    print(os.path.exists('test_dir'))

    # listdir()
    print(os.listdir('.'))

    # chdir()
    os.mkdir('test_dir')
    os.chdir('test_dir')
    print(os.listdir('.'))
    os.chdir('..')
    os.rmdir('test_dir')

    # ShUtil module ----------------------------------------------------------#
    # copy()
    fp = open('from.txt', 'wt')
    fp.close()
    shutil.copy('from.txt', 'to.txt')
    os.remove('from.txt')
    os.remove('to.txt')

    # move()
    fp = open('from.txt', 'wt')
    fp.close()
    shutil.move('from.txt', 'to.txt')
    os.remove('to.txt')

    # Glob module ------------------------------------------------------------#
    print(glob.glob('C*'))
    print(glob.glob('??'))
    print(glob.glob('B??????py'))
    print(glob.glob('[DIN]*py'))

    # SubProcess module ------------------------------------------------------#
    # getoutput()
    print(subprocess.getoutput('date'))
    print(subprocess.getoutput('date -u | wc'))

    # check_output()
    print(subprocess.check_output(['date', '-u']))

    # getstatusoutput()
    print(subprocess.getstatusoutput('date'))

    # call - Save status code only
    print(subprocess.call('date'))
    print(subprocess.call('date -u', shell=True))       # with argument
    print(subprocess.call(['date', '-u']))              # with argument
