
import matplotlib.pyplot as plt
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
dx = x2 - x1
dy = y2 - y1
steps = max(abs(dx), abs(dy))
x = x1
y = y1
x_step = dx / steps
y_step = dy / steps
x_points = []
y_points = []
for i in range(steps + 1):
    x_points.append(int(x))
    y_points.append(int(y))
    x = x + x_step
    y = y + y_step
plt.plot(x_points,y_points,marker="o",linestyle="-",color="red")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
