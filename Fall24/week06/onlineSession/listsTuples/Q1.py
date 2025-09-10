
# 1. Counting Even Numbers in a Range
# Write a function that takes two numbers, start and end, as inputs.
# The function should use a for loop to find all even numbers between start and end (inclusive)
# and store each even number in a list.
# After the loop finishes, the function should return this list of even numbers
# and the total count of even numbers in the range.
# For example, if you input 1 and 20, the function should return a list of all even numbers from 1 to 20
# and the count of those numbers.

def count_even_numbers(start, end):
    evens = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens, len(evens)

# def count_evens(start, end):
#     evens = []
#     even_count = 0
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             evens.append(number)
#             even_count += 1
#     return evens, even_count


evens_list, count_evens = count_even_numbers(1, 20)
print("Even numbers:", evens_list)
print("Total even numbers:", count_evens)
