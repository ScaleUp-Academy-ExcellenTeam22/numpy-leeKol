import numpy as np

"""
The program computes the median of flattened given array.
"""

if __name__ == '__main__':
    array = np.arange(12).reshape(2, 6)
    print("Original array:")
    print(array)
    print("Median of said array:")
    print(np.median(array))
