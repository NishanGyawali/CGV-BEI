import numpy as np
import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    xlist, ylist = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    if steps == 0:
        return np.array([x1]), np.array([y1]), 0
    xInc = dx / steps
    yInc = dy / steps
    x = x1
    y = y1
    for _ in range(steps + 1):
        xlist.append(round(x))
        ylist.append(round(y))
        x += xInc
        y += yInc
    return np.array(xlist), np.array(ylist), steps

def apply_transformation(x1, y1, x2, y2, tx, ty, theta):
    # Homogeneous coordinates for points
    p1 = np.array([[x1], [y1], [1]])
    p2 = np.array([[x2], [y2], [1]])
    
    # Translation matrix
    T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    
    # Rotation matrix (theta in degrees)
    theta_rad = np.radians(theta)
    R = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                  [np.sin(theta_rad), np.cos(theta_rad), 0],
                  [0, 0, 1]])
    
    # Apply translation then rotation
    p1_transformed = R @ T @ p1
    p2_transformed = R @ T @ p2
    
    return p1_transformed[0][0], p1_transformed[1][0], p2_transformed[0][0], p2_transformed[1][0]

def main():
    print("____")
    print("Enter Starting Point:")
    x1 = int(input("Enter X:"))
    y1 = int(input("Enter Y:"))

    print("Enter Ending Point:")
    x2 = int(input("Enter X:"))
    y2 = int(input("Enter Y:"))

    print("Enter Translation:")
    tx = float(input("Enter TX:"))
    ty = float(input("Enter TY:"))

    print("Enter Rotation Angle (in degrees):")
    theta = float(input("Enter Theta:"))

    # Original line
    xlist_orig, ylist_orig, steps_orig = DDA(x1, y1, x2, y2)
    
    # Transformed line
    x1_t, y1_t, x2_t, y2_t = apply_transformation(x1, y1, x2, y2, tx, ty, theta)
    xlist_trans, ylist_trans, steps_trans = DDA(x1_t, y1_t, x2_t, y2_t)
    
    print(f"Original Line - X: {xlist_orig}\nY: {ylist_orig}")
    print(f"Transformed Line - X: {xlist_trans}\nY: {ylist_trans}")
    
    plt.plot(xlist_orig, ylist_orig, label='Original Line', color='blue')
    plt.plot(xlist_trans, ylist_trans, label='Transformed Line', color='red')
    plt.title(f"DDA Algorithm - Original Steps: {steps_orig}, Transformed Steps: {steps_trans}")
    plt.legend()
    plt.savefig("Assignments/DDA_transformed.png")

if __name__ == "__main__":
    main()
