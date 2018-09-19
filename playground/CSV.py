###############################################################################
# @brief    Python3 - CSV module.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.18 - Created.
###############################################################################

'''
reader() & writer()
    row => \n (new line)
    col => , (comma)
'''

import csv

if __name__ == '__main__':
    # List and CSV
    testList = [
        ['item11', 'item12'],
        ['item21', 'item22'],
        ['item31', 'item32']
    ]

    with open('csvfile', 'wt') as fp:
        csvout = csv.writer(fp)
        csvout.writerows(testList)

    with open('csvfile', 'rt') as fp:
        csvin = csv.reader(fp)
        testList = [row for row in csvin]
    print(testList)

    with open('csvfile', 'rt') as fp:
        csvin = csv.DictReader(fp, fieldnames=['first', 'last'])
        testList = [row for row in csvin]
    print(testList)

    testList = [
        {'first': 'value11', 'last': 'value12'},
        {'first': 'value21', 'last': 'value22'},
        {'first': 'value31', 'last': 'value32'},
    ]
    with open('csvfile', 'wt') as fp:
        csvout = csv.DictWriter(fp, ['first', 'last'])
        csvout.writeheader()
        csvout.writerows(testList)

    with open('csvfile', 'rt') as fp:
        csvin = csv.DictReader(fp)
        testList = [row for row in csvin]
    print(testList)
