
# Fibonacci Sequence: Write a recursive function that takes an integer n and returns the n-th Fibonacci number.
# The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

# f(2) = 1, f(3) = 2, f(4) = 3, f(5) = 5, f(6) = 8 ...

def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call


print(fibonacci(16))
