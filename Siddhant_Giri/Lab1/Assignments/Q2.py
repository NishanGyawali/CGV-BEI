import matplotlib.pyplot as plt
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x_points = [x1, x2, x2, x1, x1]
y_points = [y1, y1, y2, y2, y1]
plt.plot(x_points,y_points,marker="o",linestyle="-",color="red")
plt.xla2bel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
