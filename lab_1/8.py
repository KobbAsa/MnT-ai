import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import gaussmf

def not_a(a):
    return 1 - a

x = np.linspace(0, 10, 100)

a = gaussmf(x, 6, 3)

plt.plot(x, a, color='blue')
plt.plot(x, not_a(a),  color='red', linestyle='--', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('8. Fuzzy Set and Vague Judgement')
plt.grid(True)
plt.show()
