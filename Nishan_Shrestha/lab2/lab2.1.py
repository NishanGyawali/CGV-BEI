import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2, px, py):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        px.append(round(x))
        py.append(round(y))
        x += x_inc
        y += y_inc

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3, y3 = x1, y2
x4, y4 = x2, y1

px, py = [], []

dda_line(x1, y1, x3, y3, px, py)
dda_line(x3, y3, x2, y2, px, py)
dda_line(x2, y2, x4, y4, px, py)
dda_line(x4, y4, x1, y1, px, py)

plt.plot(px, py,linestyle="-", color='blue')
plt.title("Rectangle using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.show()
