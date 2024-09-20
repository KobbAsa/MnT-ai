import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import gaussmf

x = np.linspace(0, 10, 100)

y1 = gaussmf(x, 4, 2)
y2 = gaussmf(x, 6, 3)

y_min = np.fmin(y1, y2)

y_max = np.fmax(y1, y2)

plt.figure(figsize=(10, 6))

plt.plot(x, y1, color='red', linewidth=3)
plt.plot(x, y2, color='blue', linewidth=3)
plt.plot(x, y_min, color='cyan', linewidth=3)
plt.plot(x, y_max, color='purple', linewidth=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('6-7. Minimax Interpretation of Logical Operators')
plt.grid(True)
plt.show()