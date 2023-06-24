#!/usr/bin/python3
def islower(c):
    """Function that checks for lowercase character
    Args:
        c: char to be checked
    Return:
        True or False
    """
    if ord(c) > 96 and ord(c) < 123:
        return (True)
    else:
        return (False)
