import matplotlib.pyplot as plt
import numpy as np

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

def draw_multiple_ellipses():
    ellipses = [
        {'rx': 30, 'ry': 15, 'xc': 0, 'yc': 0, 'color': 'purple', 'label': 'Ellipse 1'},
        {'rx': 25, 'ry': 20, 'xc': 50, 'yc': 30, 'color': 'blue', 'label': 'Ellipse 2'},
        {'rx': 20, 'ry': 30, 'xc': -40, 'yc': 25, 'color': 'red', 'label': 'Ellipse 3'},
        {'rx': 35, 'ry': 10, 'xc': 30, 'yc': -35, 'color': 'green', 'label': 'Ellipse 4'},
        {'rx': 15, 'ry': 25, 'xc': -30, 'yc': -20, 'color': 'orange', 'label': 'Ellipse 5'},
    ]
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    
    all_region1_spacings = []
    all_region2_spacings = []
    ellipse_labels = []
    
    for ellipse in ellipses:
        xes, yes, region1_points, region2_points = midpoint_ellipse(
            ellipse['rx'], ellipse['ry'], ellipse['xc'], ellipse['yc']
        )
        ax.scatter(xes, yes, marker='.', s=15, color=ellipse['color'], 
                   label=ellipse['label'], alpha=0.7)
        
        region1_spacings = calculate_point_spacing(region1_points)
        region2_spacings = calculate_point_spacing(region2_points)
        
        if region1_spacings:
            all_region1_spacings.append(region1_spacings)
        if region2_spacings:
            all_region2_spacings.append(region2_spacings)
        ellipse_labels.append(ellipse['label'])
    
    ax.set_title("Multiple Ellipses with Different Radii and Centers")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.axis('equal')
    
    print("\n" + "="*80)
    print("POINT SPACING COMPARISON - REGION 1 vs REGION 2")
    print("="*80)
    
    for i, ellipse in enumerate(ellipses):
        if i < len(all_region1_spacings) and i < len(all_region2_spacings):
            r1_sp = all_region1_spacings[i]
            r2_sp = all_region2_spacings[i]
            if r1_sp and r2_sp:
                print(f"\n{ellipse['label']}: rx={ellipse['rx']}, ry={ellipse['ry']}, center=({ellipse['xc']}, {ellipse['yc']})")
                print("-"*80)
                print("REGION 1:")
                print(f"  Points: {len(r1_sp)+1}, Spacings: {len(r1_sp)}")
                print(f"  Average: {np.mean(r1_sp):.4f} | Max: {np.max(r1_sp):.4f} | Min: {np.min(r1_sp):.4f} | Std Dev: {np.std(r1_sp):.4f}")
                print("  Spacing Values:", [f"{s:.3f}" for s in r1_sp])
                
                print("\nREGION 2:")
                print(f"  Points: {len(r2_sp)+1}, Spacings: {len(r2_sp)}")
                print(f"  Average: {np.mean(r2_sp):.4f} | Max: {np.max(r2_sp):.4f} | Min: {np.min(r2_sp):.4f} | Std Dev: {np.std(r2_sp):.4f}")
                print("  Spacing Values:", [f"{s:.3f}" for s in r2_sp])
                
                ratio = np.mean(r1_sp) / np.mean(r2_sp)
                print(f"\nCOMPARISON: Ratio (R1/R2) = {ratio:.4f}")
                if ratio > 1:
                    print(f"  -> Region 1 spacing is {ratio:.2f}x larger than Region 2")
                else:
                    print(f"  -> Region 2 spacing is {1/ratio:.2f}x larger than Region 1")
                print(f"  Difference: {abs(np.mean(r1_sp) - np.mean(r2_sp)):.4f}")
    
    print("\n" + "="*80)
    
    plt.tight_layout()
    plt.show()

def compare_region_spacing():
    ellipses = [
        {'rx': 30, 'ry': 15, 'xc': 0, 'yc': 0},
        {'rx': 40, 'ry': 20, 'xc': 0, 'yc': 0},
        {'rx': 50, 'ry': 25, 'xc': 0, 'yc': 0},
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for idx, ellipse in enumerate(ellipses):
        xes, yes, region1_points, region2_points = midpoint_ellipse(
            ellipse['rx'], ellipse['ry'], ellipse['xc'], ellipse['yc']
        )
        
        axes[idx].scatter(xes, yes, marker='.', s=10, color='purple', alpha=0.6)
        axes[idx].set_title(f"Ellipse: rx={ellipse['rx']}, ry={ellipse['ry']}")
        axes[idx].set_xlabel("X")
        axes[idx].set_ylabel("Y")
        axes[idx].grid(True, alpha=0.3)
        axes[idx].axis('equal')
        
        region1_spacings = calculate_point_spacing(region1_points)
        region2_spacings = calculate_point_spacing(region2_points)
        
        if region1_spacings and region2_spacings:
            print(f"\n" + "="*80)
            print(f"Ellipse: rx={ellipse['rx']}, ry={ellipse['ry']}, center=({ellipse['xc']}, {ellipse['yc']})")
            print("-"*80)
            print("REGION 1:")
            print(f"  Points: {len(region1_points)}, Spacings: {len(region1_spacings)}")
            print(f"  Average: {np.mean(region1_spacings):.4f} | Max: {np.max(region1_spacings):.4f} | Min: {np.min(region1_spacings):.4f}")
            print("  Spacing Values:", [f"{s:.3f}" for s in region1_spacings])
            
            print("\nREGION 2:")
            print(f"  Points: {len(region2_points)}, Spacings: {len(region2_spacings)}")
            print(f"  Average: {np.mean(region2_spacings):.4f} | Max: {np.max(region2_spacings):.4f} | Min: {np.min(region2_spacings):.4f}")
            print("  Spacing Values:", [f"{s:.3f}" for s in region2_spacings])
            
            ratio = np.mean(region1_spacings) / np.mean(region2_spacings)
            print(f"\nCOMPARISON: Ratio (R1/R2) = {ratio:.4f}")
            if ratio > 1:
                print(f"  -> Region 1 spacing is {ratio:.2f}x larger than Region 2")
            else:
                print(f"  -> Region 2 spacing is {1/ratio:.2f}x larger than Region 1")
            print("="*80)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_multiple_ellipses()
    compare_region_spacing()
