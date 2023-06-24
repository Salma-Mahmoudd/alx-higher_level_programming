#!/usr/bin/python3
def fizzbuzz():
    """Function that prints the numbers from 
        1 to 100 separated by a space.
        prints the numbers from 1 to 100 separated by a space.
    Args:
        a: first number
        b: second number
    Return:
        Nothing
    """
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
