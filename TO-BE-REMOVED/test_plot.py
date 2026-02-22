import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x_points, y_points = [], []
    x, y = x1, y1
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc
    return x_points, y_points

x1, y1 = 2, 3
x2, y2 = 10, 7

xs, ys = dda(x1, y1, x2, y2)

print("X points:", xs)
print("Y points:", ys)

plt.plot(xs, ys, marker='o')
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
