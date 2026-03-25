import matplotlib.pyplot as plt
x1=-10
y1=-10
xini=10
yini=10
for i in range(100):
    x1=x1+1
    y1=y1+1
    plt.plot(x1,yini,'ro')
    plt.plot(xini,y1,'ro')
plt.show()
