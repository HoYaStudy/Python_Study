###############################################################################
# @brief    Python3 - Iterator.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   2017.08.09 - Created.
###############################################################################

'''
'''


def myGenerator_Range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


if __name__ == '__main__':
    # Sequence ---------------------------------------------------------------#
    # zip()
    print("### zip() Iterator Study ###")
    english = 'Monday', 'Tuesday', 'Wednesday'
    french = 'Lundi', 'Mardi', 'Mercredi'
    for iter in list(zip(english, french)):
        print(iter)
    for iter in dict(zip(english, french)).items():
        print(iter)
    print('')

    # Generator --------------------------------------------------------------#
    print("### Generator Study ###")
    # Generator Comprehension
    numbers = (number for number in range(1, 6))
    print(numbers)
    for number in numbers:
        print(number)

    # range()
    for n in range(6):
        print(n)
    for n in range(5, -1, -1):
        print(n)

    # Generator Function
    for n in myGenerator_Range(1, 5):
        print(n)
