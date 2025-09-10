
# 2. Extracting and Reversing Part of a List
# Write a function that takes a list of numbers and two integers, start and end, as inputs.
# Use slicing to produce a sublist from the original list that starts at start index and ends at end index (inclusive).
# Then, use a for loop to reverse the sublist. Finally, return the reversed sublist.
# For example, if the input list is [2, 4, 6, 8, 10, 12, 14], with start as 2 and end as 5,
# the function should first create the sublist [6, 8, 10, 12]
# and then return the reversed version of this sublist, which is [12, 10, 8, 6].

def extract_and_reverse_sublist(input_list, start, end):
    # Extract the sublist using slicing
    sublist = input_list[start:end + 1]

    # Reverse the sublist using a for loop
    reversed_sublist = sublist[::-1]
    # for item in sublist:
    #     reversed_sublist.insert(0, item)

    return reversed_sublist


result = extract_and_reverse_sublist([2, 4, 6, 8, 10, 12, 14], 2, 5)
print(result)  # Output: [12, 10, 8, 6]
