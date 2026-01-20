import numpy as np
import matplotlib.pyplot as plt
Add imports for numpy and matplotlib
x = np.linspace(0, 1, 50)
y_log = np.log(x)
y_exp = np.exp(x)

plt.scatter(x, y_log, label='Natural Log')
plt.scatter(x, y_exp, label='Exponential')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Natural Log and Exponential Functions')
plt.legend(loc='lower right')
plt.show()
