import matplotlib.pyplot as plt
print("____")
print("Enter Starting Point:")
x1=int(input("Enter X:"))
y1=int(input("Enter Y:"))

print("Enter Ending Point:")
x2=int(input("Enter X:"))
y2=int(input("Enter Y:"))

def Rectangle(x1,y1,x2,y2):
    xlist,ylist=[x1,x1,x2,x2,x1],[y1,y2,y2,y1,y1]
    plt.plot(xlist,ylist)
    plt.show()

Rectangle(x1,y1,x2,y2)