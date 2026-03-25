# Task 4: Line Graph and Bar Graph

import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
marks = [78, 85, 72, 90, 88]

x = [1, 2, 3, 4, 5]
y = [10, 5, 12, 8, 15]

plt.figure(figsize=(10, 4))

# Line graph (left)
plt.subplot(1, 2, 1)
plt.plot(x, y, marker="o")
plt.title("Line Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Bar graph (right)
plt.subplot(1, 2, 2)
plt.bar(subjects, marks)
plt.title("Marks of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(axis="y")

plt.tight_layout()
plt.show()