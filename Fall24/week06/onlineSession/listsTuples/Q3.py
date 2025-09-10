
# 3. Sort a List in Ascending Order
# Write a function that takes a list of numbers as input and returns a new list with the numbers arranged
# from smallest to largest. Do not use any built-in sorting functions (such as sort() or sorted()).
# Hint: Use two for loops: one to keep iterating over the list and another to compare each pair of adjacent elements.
# If two adjacent elements are in the wrong order, swap them. Repeat this until all elements are in the correct order.
# For example, if the input list is [5, 2, 9, 1, 5, 6], the function should return [1, 2, 5, 5, 6, 9].

def sort_list_ascending(input_list):
    # Create a copy of the input list to avoid modifying the original list
    sorted_list = input_list[:]

    # Outer loop to keep passing through the list
    for i in range(len(sorted_list)):
        # Inner loop to compare each pair of adjacent elements
        for j in range(len(sorted_list) - 1):
            # Swap if the elements are in the wrong order
            # if sorted_list[j] > sorted_list[j + 1]:
            #   temp = sorted_list[j]  # Store the value of sorted_list[j] in a temporary variable
            #   sorted_list[j] = sorted_list[j + 1]  # Move the value of sorted_list[j + 1] to sorted_list[j]
            #   sorted_list[j + 1] = temp  # Assign the value from the temporary variable to sorted_list[j + 1]

            if sorted_list[j] > sorted_list[j + 1]:
                # Swap if the elements are in the wrong order
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


# Example usage
result = sort_list_ascending([5, 2, 9, 1, 5, 6])
print(result)  # Output: [1, 2, 5, 5, 6, 9]
