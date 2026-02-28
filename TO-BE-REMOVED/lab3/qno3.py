def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    Xinc = dx / steps  
    Yinc = dy / steps  
    
    x = x1
    y = y1
    
    int_additions = 0
    int_multiplications = 0
    
    for i in range(steps + 1):
      
        x += Xinc
        y += Yinc
        int_additions += 2   
        int_multiplications += 2  
    
    return int_additions, int_multiplications

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    
    if dx > dy:
        p = 2*dy - dx
        int_additions = 0
        int_multiplications = 0
        for _ in range(dx):
            x += sx
            int_additions += 1
            if p >= 0:
                y += sy
                p += 2*(dy - dx)
                int_additions += 2  
            else:
                p += 2*dy
                int_additions += 1  
    else:
        p = 2*dx - dy
        int_additions = 0
        int_multiplications = 0
        for _ in range(dy):
            y += sy
            int_additions += 1
            if p >= 0:
                x += sx
                p += 2*(dx - dy)
                int_additions += 2
            else:
                p += 2*dx
                int_additions += 1
    
    return int_additions, int_multiplications


x1, y1 = 2, 3
x2, y2 = 20, 15

dda_add, dda_mul = dda(x1, y1, x2, y2)
bres_add, bres_mul = bresenham(x1, y1, x2, y2)

print(f"DDA: Additions = {dda_add}, Multiplications = {dda_mul}")
print(f"Bresenham: Additions = {bres_add}, Multiplications = {bres_mul}")
