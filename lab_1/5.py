import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.linspace(0, 10, 100)

y_z = fuzz.zmf(x, 3, 4)
y_pi = fuzz.pimf(x, 3, 6, 7, 9)
y_s = fuzz.smf(x, 5, 8)

plt.plot(x, y_z, color='blue', linewidth=3)
plt.plot(x, y_pi, color='green', linewidth=3)
plt.plot(x, y_s, color='red', linewidth=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('5. Polynomial Membership Functions')
plt.grid(True)
plt.show()