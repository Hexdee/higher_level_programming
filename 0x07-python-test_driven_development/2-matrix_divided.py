#!/usr/bin/python3
"""Module matrix_divided"""


def matrix_divided(matrix, div):
    """matrix_divided.

    Args:
        Matrix: Matrix to divide.
        div: Number to divide.

    Returns:
        Matrix divided.

    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) not in (int, float):
        raise TypeError('div must be a number')

    width = set([len(k) for k in matrix])
    if len(width) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    matrix_tmp = [[0] * len(matrix[0]) for z in range(len(matrix))]

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            tmp = matrix[i][j]
            if type(tmp) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            matrix_tmp[i][j] += round(tmp / div, 2)

    return matrix_tmp

if __name__ == '__main__':
    import doctest
    doctest.testfile("test/2-matrix_divided.txt")
