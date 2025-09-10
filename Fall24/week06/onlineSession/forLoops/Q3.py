
# 3. Counting Even Numbers in a Range
# Write a function that takes two numbers, start and end, as inputs.
# The function should use a for loop to find all even numbers between start and end (inclusive)
# and print each even number. At the end, the function should return the total count of even numbers.
# For example, if you input 1 and 20, it should print each even number from 1 to 20
# and return the total number of even numbers in that range.


def count_even_numbers(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i)
            count += 1
    return count


print("Amount of even numbers:", count_even_numbers(1, 20))

