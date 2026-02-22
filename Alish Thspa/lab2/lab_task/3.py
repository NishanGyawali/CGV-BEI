#Modify the program to take endpoints as user input.
import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1

    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


# User input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x, y = dda_line(x1, y1, x2, y2)

plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o')
plt.title("DDA Line Drawing (User Input)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()

""" 
example input:
Enter x1: 40
Enter y1: 56
Enter x2: 90
Enter y2: 76 
"""