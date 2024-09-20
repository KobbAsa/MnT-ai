import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.linspace(0, 10, 100)

y1 = fuzz.gaussmf(x, 6, 1)

y2 = fuzz.gauss2mf(x, 5, 1, 7, 1)

plt.plot(x, y1, color='darkgreen', linewidth=3)

plt.plot(x, y2, color='darkblue', linewidth=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gaussian Membership Functions')
plt.grid(True)
plt.show()