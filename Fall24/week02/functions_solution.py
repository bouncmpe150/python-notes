

def square(number):
    # exponentiation operator

    return number ** 2


# Example usage:
print(square(5))  # Output: 25

'''
#manually calculated using multiplication
def square(number):
    return number * number

# Example usage:
print(square(5))  # Output: 25

'''

######


def is_even(number):
    return number % 2 == 0

# Example usage:
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False


###

def sum_of_list(numbers):
    return sum(numbers)

# Example usage:
print(sum_of_list([1, 2, 3, 4]))  # Output: 10

'''
#iterates through the list to find the total sum
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage:
print(sum_of_list([1, 2, 3, 4]))  # Output: 10

'''
###

def reverse_string(string):
    return string[::-1]

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"

'''
#builds a new string character by character in reverse order
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"

'''

###

def find_largest(numbers):
    return max(numbers)

# Example usage:
print(find_largest([1, 3, 7, 0, 5]))  # Output: 7

'''
# manually checks for the largest element
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

# Example usage:
print(find_largest([1, 3, 7, 0, 5]))  # Output: 7

'''

###

def is_palindrome(word):
    return word == word[::-1]

# Example usage:
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False

'''
#  uses a loop to compare characters from the start and end of the string
def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Example usage:
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False

'''


###

def concatenate_strings(str1, str2):
    return str1 + str2

# Example usage:
print(concatenate_strings("Hello, ", "world!"))  # Output: "Hello, world!"


'''
# combines strings by iterating through each character
def concatenate_strings(str1, str2):
    concatenated = ""
    for char in str1:
        concatenated += char
    for char in str2:
        concatenated += char
    return concatenated

# Example usage:
print(concatenate_strings("Hello, ", "world!"))  # Output: "Hello, world!"

'''

###
def raise_to_power(base, exponent):
    return base ** exponent

# Example usage:
print(raise_to_power(2, 3))  # Output: 8

'''
# uses a loop to multiply the base repeatedly
def raise_to_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
print(raise_to_power(2, 3))  # Output: 8

'''
###
def absolute_value(number):
    return abs(number)

# Example usage:
print(absolute_value(-10))  # Output: 10

'''
# manually checks for the sign of the number
def absolute_value(number):
    if number < 0:
        return -number
    return number

# Example usage:
print(absolute_value(-10))  # Output: 10
print(absolute_value(5))    # Output: 5

'''
###

def string_length(string):
    return len(string)

# Example usage:
print(string_length("hello"))  # Output: 5

'''
# uses a loop to count the number of characters
def string_length(string):
    length = 0
    for char in string:
        length += 1
    return length

# Example usage:
print(string_length("hello"))  # Output: 5

'''