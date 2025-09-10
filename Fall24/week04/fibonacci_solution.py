def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def report_fibonacci(numbers, index=0):
    # Base case for recursion
    if index >= len(numbers):
        return
    # Get the Fibonacci number for the current index
    n = numbers[index]
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    # Recursive call for the next index
    report_fibonacci(numbers, index + 1)

# List of values of n to compute Fibonacci numbers
n_values = [11, 15, 18, 21, 30]

# Reporting the outputs without using a for loop
report_fibonacci(n_values)

'''
# Alternative

def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

print(fibonacci(3))

'''