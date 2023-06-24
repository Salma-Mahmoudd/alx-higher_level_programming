#!/usr/bin/python3
def islower(c):
    """Function that checks for lowercase character
    Args:
        c: char to be checked
    Return:
        True or False
    """
    if c >= 'a' and c <= 'z':
        return (True)
    elif c >= 'A' and c <= 'Z':
        return (False)
    else:
        return None
