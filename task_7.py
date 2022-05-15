import numpy as np

"""
The program creates a 4x4 array with random values,
and creates a new array from the said array swapping first and last rows.
"""

if __name__ == '__main__':
    matrix = np.random.rand(4, 4)
    print("First array:")
    print(matrix)
    matrix[0], matrix[-1] = matrix[-1].copy(), matrix[0].copy()
    print("Second array:")
    print(matrix)
