import numpy as np

"""
The program creates a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
"""

if __name__ == '__main__':
    matrix = np.ones((10, 10))
    matrix[1:-1, 1:-1] = 0
    print(matrix)
