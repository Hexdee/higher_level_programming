#!/usr/bin/python3
"""Module print_square"""


def print_square(size):
    """print_square.

    Args:
        size: Size of a side of the square.

    Returns:
        Print the square.

    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
