import math
import matplotlib.pyplot as plt

x = [i * 2 * math.pi / 1000 for i in range(1001)]
y = [math.sin(val) for val in x]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave: y = sin(x)')
plt.grid(True)
plt.show()

