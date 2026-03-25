import matplotlib.pyplot as plt
print("____")
print("Enter Starting Point:")
x1=int(input("Enter X:"))
y1=int(input("Enter Y:"))

print("Enter Ending Point:")
x2=int(input("Enter X:"))
y2=int(input("Enter Y:"))

def DDA(x1, y1, x2, y2):
    xlist, ylist = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    # Use float for increments to support negative and non-integer steps
    if steps == 0:
        # Single point case
        return [x1], [y1], 0
    xInc = dx / steps
    yInc = dy / steps
    x = x1
    y = y1
    for _ in range(steps + 1):
        xlist.append(round(x))
        ylist.append(round(y))
        x += xInc
        y += yInc
    return xlist, ylist, steps

xlist, ylist,steps = DDA(x1,y1,x2,y2)
print(f"X: {xlist}\nY: {ylist}")
plt.plot(xlist, ylist)
plt.title(f"DDA Algorithm - Steps: {steps}")
plt.show()