import numpy as np
import matplotlib.pyplot as plt

"""
The program computes the x and y coordinates for points on a sine curve and plots the points using matplotlib.
"""

if __name__ == '__main__':
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
