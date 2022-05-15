import numpy as np

"""
The program replaces all numbers in a given array which is equal, less and greater to a given number.
"""

if __name__ == '__main__':
    matrix = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    number = 2
    new_number = 0
    print(np.where(matrix == number, new_number, matrix))
    print(np.where(matrix < number, new_number, matrix))
    print(np.where(matrix > number, new_number, matrix))
