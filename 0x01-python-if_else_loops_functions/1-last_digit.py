#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LD = abs(number) % 10 * (-1 if number < 0 else 1)
if LD == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif LD < 6:
    print(f"Last digit of {number} is {LD} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {LD} and is greater than 5")
