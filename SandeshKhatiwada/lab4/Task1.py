import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_ellipse_points(xc, yc, x, y, xes, yes):
    pts = [
        (x + xc, y + yc),
        (-x + xc, y + yc),
        (x + xc, -y + yc),
        (-x + xc, -y + yc),
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)

def midpoint_ellipse(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry
    x = 0
    y = ry
    xes, yes = [], []
    region1_points = []
    region2_points = []
    
    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, xes, yes)
    region1_points.append((x, y))
    
    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, xes, yes)
        region1_points.append((x, y))
    
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)
    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2
        plot_ellipse_points(xc, yc, x, y, xes, yes)
        region2_points.append((x, y))
    
    return xes, yes, region1_points, region2_points

def calculate_point_spacing(points):
    if len(points) < 2:
        return []
    spacings = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        spacings.append(distance)
    return spacings

def plot_midpoint_ellipse(rx, ry, xc=0, yc=0):
    xes, yes, region1_points, region2_points = midpoint_ellipse(rx, ry, xc, yc)
    
    region1_spacings = calculate_point_spacing(region1_points)
    region2_spacings = calculate_point_spacing(region2_points)
    
    print("POINT SPACING COMPARISON - REGION 1 vs REGION 2")
    print("="*80)
    print(f"\nEllipse Parameters: rx={rx}, ry={ry}, center=({xc}, {yc})")
    print(f"Total Points: {len(region1_points) + len(region2_points)}")
    print(f"Region 1 Points: {len(region1_points)}, Region 2 Points: {len(region2_points)}")
    print(f"Region 1 Spacings: {len(region1_spacings)}, Region 2 Spacings: {len(region2_spacings)}")
    
    if region1_spacings and region2_spacings:
        print("\n" + "-"*80)
        print("REGION 1 ANALYSIS")
        print("-"*80)
        print(f"Number of Points: {len(region1_points)}")
        print(f"Number of Spacings: {len(region1_spacings)}")
        print(f"Average Spacing: {np.mean(region1_spacings):.4f}")
        print(f"Maximum Spacing: {np.max(region1_spacings):.4f}")
        print(f"Minimum Spacing: {np.min(region1_spacings):.4f}")
        print(f"Standard Deviation: {np.std(region1_spacings):.4f}")
        print("\nRegion 1 Spacing Values:")
        for i, spacing in enumerate(region1_spacings, 1):
            print(f"  Point {i} to {i+1}: {spacing:.4f}")
        
        print("\n" + "-"*80)
        print("REGION 2 ANALYSIS")
        print("-"*80)
        print(f"Number of Points: {len(region2_points)}")
        print(f"Number of Spacings: {len(region2_spacings)}")
        print(f"Average Spacing: {np.mean(region2_spacings):.4f}")
        print(f"Maximum Spacing: {np.max(region2_spacings):.4f}")
        print(f"Minimum Spacing: {np.min(region2_spacings):.4f}")
        print(f"Standard Deviation: {np.std(region2_spacings):.4f}")
        print("\nRegion 2 Spacing Values:")
        for i, spacing in enumerate(region2_spacings, 1):
            print(f"  Point {i} to {i+1}: {spacing:.4f}")
        
        print("\n" + "-"*80)
        print("COMPARISON SUMMARY")
        print("-"*80)
        ratio = np.mean(region1_spacings) / np.mean(region2_spacings)
        print(f"Average Spacing Ratio (Region 1 / Region 2): {ratio:.4f}")
        if ratio > 1:
            print(f"  -> Region 1 has {ratio:.2f}x larger average spacing than Region 2")
        else:
            print(f"  -> Region 2 has {1/ratio:.2f}x larger average spacing than Region 1")
        print(f"Difference in Average Spacing: {abs(np.mean(region1_spacings) - np.mean(region2_spacings)):.4f}")
        print("="*80)
    else:
        print("\nWARNING: Could not calculate spacing comparison.")
        print(f"Region 1 spacings: {len(region1_spacings)}, Region 2 spacings: {len(region2_spacings)}")
    
    sys.stdout.flush()
    
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    ax.scatter(xes, yes, marker='.', color='purple', s=20)
    ax.set_title(f"Midpoint Ellipse Algorithm\nrx={rx}, ry={ry}, center=({xc}, {yc})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)
    ax.axis('equal')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_midpoint_ellipse(30, 15, 0, 0)
