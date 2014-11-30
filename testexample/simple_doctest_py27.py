# encoding=utf-8
#-------------------------------------------------------------------------------
# Description:
# Author:      ccat
# Created:     30/Nov/2014
#-------------------------------------------------------------------------------

def doctestTarget(a=1,b=1):
    """
    >>> doctestTarget(2,2)
    4
    >>> doctestTarget(a=2,b=2.5)
    5.0
    """
    return a*b


if __name__ == "__main__":
    import doctest
    doctest.testmod()


