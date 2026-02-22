# Task 3: Even and odd numbers from a list

numbers = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n)

print("Odd numbers:")
for n in numbers:
    if n % 2 != 0:
        print(n)