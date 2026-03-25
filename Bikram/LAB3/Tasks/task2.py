# Task 2: Draw lines for different octants and compare with DDA

import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1
    if dx >= dy:
        p = 2*dy - dx
        for _ in range(dx+1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2*dy - 2*dx
            else:
                p += 2*dy
    else:
        p = 2*dx - dy
        for _ in range(dy+1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2*dx - 2*dy
            else:
                p += 2*dx
    return xes, yes

# Function to plot multiple lines
def plot_bresenham_octants():
    plt.figure(figsize=(6,6))
    
    # Octant examples
    lines = [
        (2,2,10,5),   # slope < 1, positive
        (2,2,5,10),   # slope > 1, positive
        (10,10,2,5),  # slope < 1, negative
        (5,10,2,2),   # slope > 1, negative
        (2,5,12,5),   # horizontal
        (5,2,5,12)    # vertical
    ]
    
    colors = ['red','green','blue','purple','orange','brown']
    
    for i, (x1,y1,x2,y2) in enumerate(lines):
        xes, yes = bresenham_line(x1,y1,x2,y2)
        plt.plot(xes, yes, marker='o', linestyle='-', color=colors[i], label=f'({x1},{y1}) to ({x2},{y2})')
    
    plt.title("Bresenham Lines for Different Octants")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

plot_bresenham_octants()