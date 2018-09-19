###############################################################################
# @brief    Python3 - doctest module.
# @version  v1.0
# @author   llChameleoNll <hoya128@gmail.com>
# @note
#   - 2017.08.23    Created.
###############################################################################

# Import Module --------------------------------------------------------------#
import doctest


# Test Suite Class Definition ------------------------------------------------#
def testToUpper(_in):
    """
    >>> testToUpper('test')
    'TEST'
    """
    return _in.upper()


# Main -----------------------------------------------------------------------#
if __name__ == '__main__':
    doctest.testmod()
