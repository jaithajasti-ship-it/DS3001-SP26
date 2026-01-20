import numpy as np
import matplotlib.pyplot as plt

# Create grid of points
x = np.linspace(-6.5, 6.5, 100)

# Compute sine and cosine
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot as line graphs
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')

# Add legend
plt.legend(loc='lower left')

# Show plot
plt.show()
