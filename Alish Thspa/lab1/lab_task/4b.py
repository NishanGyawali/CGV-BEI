#Plot graphs using matplotlib, Bar Graph of marks of 5 subjects
import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]
marks = [78, 85, 69, 88, 92]

plt.bar(subjects, marks)
plt.title("Marks of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(axis='y')
plt.show()
