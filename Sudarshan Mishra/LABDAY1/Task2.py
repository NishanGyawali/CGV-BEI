import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)

y1 = 0.5 * x     
y2 = 2 * x       
y3 = np.full_like(x, 3)   
x4 = np.full_like(x, 2)   
y5 = -1 * x      

plt.figure(figsize=(8,8))

plt.plot(x, y1, label='m = 0.5')
plt.plot(x, y2, label='m = 2')
plt.plot(x, y3, label='horizontal (m = 0)')
plt.plot(x4, x, label='vertical (undefined slope)')
plt.plot(x, y5, label='m = -1')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Lines with Different Slopes")
plt.grid(True)
plt.show()