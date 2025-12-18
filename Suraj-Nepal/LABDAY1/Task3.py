import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    x = []
    y = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    Xinc = dx / steps
    Yinc = dy / steps

    X = x1
    Y = y1

    for i in range(steps + 1):
        x.append(round(X))
        y.append(round(Y))
        X += Xinc
        Y += Yinc

    return x, y


print("Enter line endpoints:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

x, y = dda(x1, y1, x2, y2)

plt.plot(x, y, marker='o')
plt.title("User Input Line (Using DDA)")
plt.grid()
plt.show()
