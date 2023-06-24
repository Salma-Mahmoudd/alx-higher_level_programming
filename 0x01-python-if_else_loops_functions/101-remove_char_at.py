#!/usr/bin/python3
def remove_char_at(str, n):
    """Function that  creates a copy of the string,
    removing the character at the position n
    Args:
        str: string to be edited
        n: index to be removed
    Return:
        the result
    """
    return (str[:n] + str[n + 1:])
