#Create a list of 10 integers and print even and odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n)

print("Odd numbers:")
for n in numbers:
    if n % 2 != 0:
        print(n)
