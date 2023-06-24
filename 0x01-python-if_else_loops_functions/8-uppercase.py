#!/usr/bin/python3
def uppercase(str):
    """Function that prints a string in uppercase
    Args:
        str: string to be transformed
    Return:
        the final string
    """
    up = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            up = up + chr(ord(i) - 32)
        else:
            up = up + i
    print("{}".format(up))
