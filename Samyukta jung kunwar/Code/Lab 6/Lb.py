def liang_barsky(x1,y1,x2,y2,xmin,xmax,ymin,ymax):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1 = 0
    u2 = 1
    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)
    if u1 > u2:
        return None
    return (x1 + u1 * dx, y1 + u1 * dy), (x1 + u2 * dx, y1 + u2 * dy)

x1, y1 = 1, 2   
x2, y2 = 4, 5
xmin, xmax = 2, 3
ymin, ymax = 3, 4
result = liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax)
if result:
    print("Clipped line segment:", result)
