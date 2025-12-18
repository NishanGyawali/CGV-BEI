def factorial(n):
    """Compute the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter a non-negative integer to compute its factorial: "))
        fact = factorial(num)
        print(f"The factorial of {num} is {fact}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
