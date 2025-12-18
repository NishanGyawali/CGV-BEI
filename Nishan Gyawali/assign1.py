import matplotlib
matplotlib.use('TkAgg')  # Ensure Windows compatibility
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    """
    DDA algorithm to calculate points of a line from (x1, y1) to (x2, y2)
    Returns two lists: x_points, y_points
    """
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))  # number of steps
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


print("Enter two opposite corners of the rectangle (x1 y1 x2 y2):")
inp = input().strip()
try:
    x1, y1, x2, y2 = map(int, inp.split())
except:
    print("Invalid input. Please enter four integers separated by space.")
    exit()



xs1, ys1 = dda(x1, y1, x2, y1)

xs2, ys2 = dda(x2, y1, x2, y2)

xs3, ys3 = dda(x2, y2, x1, y2)

xs4, ys4 = dda(x1, y2, x1, y1)


plt.figure()
plt.plot(xs1, ys1, marker='o')
plt.plot(xs2, ys2, marker='o')
plt.plot(xs3, ys3, marker='o')
plt.plot(xs4, ys4, marker='o')

plt.title("Rectangle using DDA")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.show()
