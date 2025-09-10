
# 2. Summing Numbers in a Range
# Write a function that takes two numbers, start and end, as inputs.
# The function should use a for loop to calculate the sum of all numbers from start to end and then return this total.
# For example, if you input 1 and 10, the function should return the sum of numbers from 1 to 10.

def sum_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


print(sum_numbers(1, 10))

