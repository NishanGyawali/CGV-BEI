# Task 3: Compare the number of additions and multiplications used in DDA and Bresenham's line algorithms for a given line segment.

import matplotlib.pyplot as plt

# --- DDA Algorithm ---
def dda_line_ops(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    x = x1
    y = y1
    
    add_count = 0
    mul_count = 0
    
    xes, yes = [], []
    
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc
        add_count += 2          # two additions per step
        mul_count += 2          # for rounding (approximate)
        
    return xes, yes, add_count, mul_count

# --- Bresenham Algorithm ---
def bresenham_line_ops(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x = x1
    y = y1
    
    add_count = 0
    mul_count = 0  # Bresenham uses no multiplication
    
    xes, yes = [], []
    
    if dx >= dy:
        p = 2 * dy - dx
        add_count += 1  # for initial p calculation
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            add_count += 1
            if p >= 0:
                y += sy
                add_count += 1
                p += 2*dy - 2*dx
                add_count += 2
            else:
                p += 2*dy
                add_count += 1
    else:
        p = 2*dx - dy
        add_count += 1
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            add_count += 1
            if p >= 0:
                x += sx
                add_count += 1
                p += 2*dx - 2*dy
                add_count += 2
            else:
                p += 2*dx
                add_count += 1
                
    return xes, yes, add_count, mul_count

# --- Example comparison ---
x1, y1 = 2, 3
x2, y2 = 15, 9

_, _, dda_add, dda_mul = dda_line_ops(x1, y1, x2, y2)
_, _, bres_add, bres_mul = bresenham_line_ops(x1, y1, x2, y2)

print(f"DDA: Additions = {dda_add}, Multiplications = {dda_mul}")
print(f"Bresenham: Additions = {bres_add}, Multiplications = {bres_mul}")