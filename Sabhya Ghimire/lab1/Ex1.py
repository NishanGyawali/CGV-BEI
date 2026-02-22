
print("____________________________________________________________")
y=[]
for i in range(5):
    input_ = input("Enter a number: ")
    y.append(input_)
print(y)

input_ = int(input("Enter a number: "))
y.pop(input_)
print(y)

input_ = int(input("Enter a number: "))
y.insert(input_, 0)
print(y)

input_ = int(input("Enter a number: "))
y.remove(input_)
print(y)

input_ = int(input("Enter a number: "))
y.sort()
print(y)