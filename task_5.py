import numpy as np

"""
The program adds a vector to each row of a given matrix.
"""

if __name__ == '__main__':
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    newRow = np.array([1, 1, 1])
    for row in range(matrix.shape[0]):
        matrix[row] += newRow
    print(matrix)
