
# 1. Basic Counting with a For Loop
# Write a function that takes two numbers, start and end, as inputs.
# Use a for loop to print all numbers on a new line from start to end, inclusive.
# For example, if you input 1 and 10, the function should print the numbers 1 to 10.

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)


print_numbers(1, 10)


