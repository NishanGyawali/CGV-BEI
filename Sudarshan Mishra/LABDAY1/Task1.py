import matplotlib.pyplot as plt
def dda_line(x1,x2,y1,y2):
    xes,yes=[],[]
    dx=x2-x1
    dy=y2-y1
    steps=int(max(abs(dx),abs(dy)))
    x_inc=dx/steps
    y_inc=dy/steps
    x=x1
    y=y1
    for i in range(steps+1):
        xes.append(round(x))
        yes.append(round(y))
        x+=x_inc
        y+=y_inc
    return xes,yes
def plot_dda(x1,x2,y1,y2):
    xes,yes=dda_line(x1,x2,y1,y2)
    plt.figure(figsize=(6,6))
    plt.plot(xes,yes,marker="o",color='red')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    print("X=",xes,"\nY=",yes)
    plt.show()
plot_dda(2,3,15,9)