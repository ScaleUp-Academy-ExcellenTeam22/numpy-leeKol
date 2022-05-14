import numpy as np
import re

"""
The program finds the number of rows and columns of a given matrix.
"""

if __name__ == '__main__':
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_dimensions = matrix.shape
    print("Matrix dimensions: rows = {}, columns = {}.".format(matrix_dimensions[0], matrix_dimensions[1]))
