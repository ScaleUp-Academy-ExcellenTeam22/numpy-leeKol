import numpy as np

"""
The program combines a one and a two dimensional array together and display their elements.
"""

if __name__ == '__main__':
    array_1_d = np.arange(4)
    print("One dimensional array:")
    print(array_1_d)
    array_2_d = np.arange(8).reshape(2, 4)
    print("Two dimensional array:")
    print(array_2_d)
    for number_1, number_2 in np.nditer([array_1_d, array_2_d]):
        print("{}:{}".format(number_1, number_2))
