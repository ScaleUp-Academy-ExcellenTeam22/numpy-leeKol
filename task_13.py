import numpy as np

"""
The program converts (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
"""

if __name__ == '__main__':
    array_1 = np.array([10, 20, 30])
    array_2 = np.array([40, 50, 60])
    matrix = np.dstack((array_1, array_2))
    print(matrix)
