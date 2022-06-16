import numpy as np
import re

"""
The program finds the number of rows and columns of a given matrix.
"""


def get_matrix_dimensions(matrix: np.array) -> tuple:
    """
    The function gets a matrix and returns the number of rows and columns of it.
    :param matrix: The matrix to be measured.
    :return: A tuple which contains the number of rows and columns of the given matrix.
    """
    return matrix.shape


if __name__ == '__main__':
    matrix_dimensions = get_matrix_dimensions(np.array([[1, 2, 3], [4, 5, 6]]))
    print("Matrix dimensions: rows = {}, columns = {}.".format(matrix_dimensions[0], matrix_dimensions[1]))
