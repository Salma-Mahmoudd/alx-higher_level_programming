#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """== and != operators"""
    def __init__(self, num):
        self.num = num

    def __eq__(self, comp):
        return self.num != comp

    def __ne__(self, comp):
        return self.num == comp
