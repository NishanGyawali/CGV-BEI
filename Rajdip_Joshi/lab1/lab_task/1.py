#Program to input five numbers and print the largest number
numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number =", largest)
