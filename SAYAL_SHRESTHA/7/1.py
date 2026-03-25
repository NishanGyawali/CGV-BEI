import matplotlib.pyplot as plt
plt.style.use('dark_background')
def liang_barsky(x0, y0, x1, y1, xmin, xmax, ymin, ymax):
    dx = x1 - x0
    dy = y1 - y0

    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    t0, t1 = 0.0, 1.0  # Initialize the parametric t values

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:  # Line is parallel and outside the clipping window
                print("Line is outside the window")
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > t1:  # It's entering
                    return None
                elif t > t0:  # Update entering parameter
                    t0 = t
            else:
                if t < t0:  # It's leaving
                    return None
                elif t < t1:  # Update leaving parameter
                    t1 = t

    # If the line is within the clipping window, calculate the clipped endpoints
    clipped_x0 = x0 + t0 * dx
    clipped_y0 = y0 + t0 * dy
    clipped_x1 = x0 + t1 * dx
    clipped_y1 = y0 + t1 * dy

    return (clipped_x0, clipped_y0, clipped_x1, clipped_y1)

# Define the rectangle bounds and the line segment's endpoints
xmin, xmax, ymin, ymax = 1, 5, 1, 5
x0, y0 = 0, 0  # Starting point of the line
x1, y1 = 6, 6  # Ending point of the line

# Call the clipping function
result = liang_barsky(x0, y0, x1, y1, xmin, xmax, ymin, ymax)

# Visualization using Matplotlib
plt.figure(figsize=(8, 8))
plt.xlim(0, 7)
plt.ylim(0, 7)

# Plot the clipping rectangle
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'c-', label='Clipping Window')

# Plot original line segment
plt.plot([x0, x1], [y0, y1], 'r--', label='Original Line Segment')

if result:
    clipped_x0, clipped_y0, clipped_x1, clipped_y1 = result
    # Plot clipped line segment
    plt.plot([clipped_x0, clipped_x1], [clipped_y0, clipped_y1], 'y-', linewidth=2, label='Clipped Line Segment')

plt.title('Line Clipping using Liang-Barsky Algorithm Roll no  41')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='white',linewidth=0.5, ls='--')
plt.axvline(0, color='white',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
