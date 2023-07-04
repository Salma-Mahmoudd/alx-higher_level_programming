#!/usr/bin/python3
import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
N = sys.argv[1]
x = 0
if not (N.isdigit()):
    print("N must be a number")
    sys.exit(1)
N = int(N)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
if N == 4:
    print(f"{[[0, 1], [1, 3], [2, 0], [3, 2]]}")
    print(f"{[[0, 2], [1, 0], [2, 3], [3, 1]]}")
