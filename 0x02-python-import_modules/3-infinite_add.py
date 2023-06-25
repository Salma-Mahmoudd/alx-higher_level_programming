#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    n = len(sys.argv)
    for i in range(n):
        sum = sum + int(sys.argv[i + 1])
    print("{}".format(sum))
