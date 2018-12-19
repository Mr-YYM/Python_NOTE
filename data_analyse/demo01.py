import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x
y2 = 2 * x**2

plt.figure()
plt.plot(x, y1, label='quadratic')

plt.figure()
plt.plot(x, y2, label='quadratic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
