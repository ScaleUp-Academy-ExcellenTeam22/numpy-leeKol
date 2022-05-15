import numpy as np

"""
The program removes single-dimensional entries from a specified shape.
"""

if __name__ == '__main__':
    matrix = np.ones((3, 1, 4))
    print(matrix.shape)
    print(np.squeeze(matrix).shape)
