#!/usr/bin/python3
# Pascal's Triangle program


def pascal_triangle(n):
    if (n <= 0):
        return "Empty list"

    for i in range(n):
        # adjust space
        print(' '*(n-i), end='')

        # compute power of 11
        print(' '.join(map(str, str(11**i))))
