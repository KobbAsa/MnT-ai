import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.linspace(0, 10, 100)

y = fuzz.sigmf(x, 1, 2)

y2 = fuzz.dsigmf(x, 3, 1, 7, 1)

y3 = fuzz.psigmf(x, 5, 1, 7, 2)

plt.plot(x, y, color='green', linewidth=3)
plt.plot(x, y2,  color='blue', linewidth=3)
plt.plot(x, y3,  color='purple', linewidth=3)

plt.title('4. Sigmoid Function Variants')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()