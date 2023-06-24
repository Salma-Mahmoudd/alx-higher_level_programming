#!/usr/bin/python3
def print_last_digit(number):
    """Function that prints the last digit of a number
    Args:
        number: given number
    Return:
        last digit of a given number
    """
    LD = abs(number) % 10
    print("{}".format(LD), end="")
    return (LD)
