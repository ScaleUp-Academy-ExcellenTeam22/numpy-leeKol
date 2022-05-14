import numpy as np

"""
The program creates a vector with values from 0 to 20 and changes the sign of the numbers in the range from 9 to 15
"""
if __name__ == '__main__':
    vector = np.array(range(21))
    vector[9:16] *= -1
    print(vector)
