###############################################################################
# @brief    Python3 - Flow Control.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.09 - Created.
###############################################################################

'''
if ... elif ... else
while ... else
for
'''

if __name__ == '__main__':
    # if ---------------------------------------------------------------------#
    if True:
        print("Statement 1")
    elif False:
        print("Statement 2")
    else:
        print("Statement 3")

    # while ------------------------------------------------------------------#
    loop = 0
    while loop <= 7:
        loop += 1
        if loop == 1:
            continue
        elif loop == 5:
            break
        print(loop)

    oddNumber = [1, 3, 5]
    loop = 0
    while loop < len(oddNumber):
        number = oddNumber[loop]
        if number % 2 == 0:
            break
        loop += 1
    else:
        print("There is no break")

    # for --------------------------------------------------------------------#
    weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    for day in weekday:
        print(day)
        for letter in day:
            print(letter)

    color = {'r': 'red', 'g': 'green', 'b': 'blue'}
    for c in color:
        print(c)
    for c in color.values():
        print(c)
    for c in color.items():
        print(c)
    for c1, c2 in color.items():
        print(c1, c2)

    for i in range(7):
        if i == 2:
            continue
        elif i == 5:
            break
        print(i)
    else:
        print("There is no break")

    list1 = ['a1', 'a2', 'a3']
    list2 = ['b1', 'b2', 'b3']
    list3 = ['c1', 'c2', 'c3']
    list4 = ['d1', 'd2', 'd3', 'd4']
    for l1, l2, l3, l4 in zip(list1, list2, list3, list4):
        print(l1, l2, l3, l4)
