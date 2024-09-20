import numpy as np
import matplotlib.pyplot as plt

def generalized_bell(x, c, sigma, b):
    return 1 / (1 + np.abs((x - c) / sigma) ** (2 * b))

x = np.linspace(0, 10, 100)

sigma, c, b = 1, 5, 3

y = generalized_bell(x, c, sigma, b)

plt.plot(x, y, color='purple', linewidth=3)
plt.title('3. Generalized Bell Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()