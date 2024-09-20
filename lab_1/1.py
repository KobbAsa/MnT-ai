import numpy as np
import matplotlib.pyplot as plt

def triangular_membership(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

x = np.linspace(0, 10, 100)

a, b, c = 2, 5, 8

y = triangular_membership(x, a, b, c)

plt.plot(x, y, color='green', linewidth=3)
plt.title('Triangular Membership Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

def trapezoidal_membership(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

a, b, c, d = 1, 3, 7, 9

y = trapezoidal_membership(x, 1, 3, 7, 9)

plt.plot(x, y, color='blue', linewidth=3)
plt.title('Trapezoidal Membership Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()