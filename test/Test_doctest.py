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
if __name__ == "__main__":
    doctest.testmod()
