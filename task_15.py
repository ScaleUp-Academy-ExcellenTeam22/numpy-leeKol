import numpy as np

"""
The program creates a three-dimension array with shape (300,400,5) and set to a variable.
It fills the array elements with values using unsigned integer (0 to 255).
"""

if __name__ == '__main__':
    matrix = np.random.randint(low=0, high=256, size=(300, 400, 5))
    print(matrix)