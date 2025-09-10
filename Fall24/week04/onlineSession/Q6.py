
# Factorial Calculation: Write a recursive function that takes an integer n
# and returns the factorial of n (i.e., n! = n * (n-1) * ... * 1).

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call


print(factorial(5))
