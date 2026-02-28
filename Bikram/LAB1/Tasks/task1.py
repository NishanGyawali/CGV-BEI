# Task 1: Largest of five numbers

numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)
print("The largest number is:", largest)