#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle("S", 4)
print(my_rectangle.__dict__)

my_rectangle.width = 11
my_rectangle.height = 11
print(my_rectangle.__dict__)
