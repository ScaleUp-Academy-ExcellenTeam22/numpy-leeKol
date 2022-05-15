import numpy as np

"""
The program sorts an along the first, last axis of an array. 
"""

if __name__ == '__main__':
    matrix = np.array([[2, 5], [4, 4]])
    print(matrix)
    ordered_by_axis_0 = np.sort(matrix, axis=0)
    print(ordered_by_axis_0)
    ordered_by_axis_1 = np.sort(ordered_by_axis_0, axis=1)
    print(ordered_by_axis_1)
