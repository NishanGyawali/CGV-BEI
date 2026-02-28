# Assignment 2: Factorial Calculation

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")