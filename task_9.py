import numpy as np

"""
The program multiplies two given arrays of same size element-by-element.
"""

if __name__ == '__main__':
    matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.multiply(matrix_1, matrix_2))
