# Question 1 - Word Count

def word_count(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Alternative solution: without get()
# def word_count(text):
#     words = text.split()
#     word_freq = {}
#     for word in words:
#         if word in word_freq: # If word exists in dictionary
#             word_freq[word] = word_freq[word] + 1
#         else: # if it is the first encounter with word, set it as 1
#             word_freq[word] = 1
#     return word_freq

# Example usage
print(word_count("hello world hello"))
print(word_count("apple orange banana apple apple"))

# Question 2 - Grade Book

def average_scores(students):
    averages = {}
    for student, scores in students.items():
        averages[student] = sum(scores) / len(scores)
    return averages

# Example usage
print(average_scores({"Alice": [85, 90, 88], "Bob": [78, 82, 80], "Eve": [95, 90, 92]}))

# Question 3 - Value Inverter

def invert_dict(d):
    return {v: k for k, v in d.items()}

# Alternative solution: without dictionary comprehension
# def invert_dict(d):
#     inverted = {}
#     for k, v in d.items():
#         inverted[v] = k
#     return inverted

# Example usage
print(invert_dict({"a": 1, "b": 2, "c": 3}))
print(invert_dict({"cat": "meow", "dog": "bark"}))

# Question 4 - Birthday Lookup

def find_birthday(birthdays, name):
    return birthdays.get(name, "Not found")

# Alternative solution: without get()
# def find_birthday(birthdays, name):
#     if name in birthdays:
#         return birthdays[name]
#     else:
#         return "Not Found"

# Example usage
print(find_birthday({"Alice": "1990-05-15", "Bob": "1989-12-20"}, "Alice"))
print(find_birthday({"Alice": "1990-05-15", "Bob": "1989-12-20"}, "Eve"))

# Question 5 - Inventory Management

def update_inventory(inventory, new_items):
    for item in new_items: # iterate the list
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Alternative solution: without get()
# def update_inventory(inventory, new_items):
#     for item in new_items:
#         if item in inventory: # an existing item
#             inventory[item] = inventory[item] + 1
#         else: # a new item
#             inventory[item] = 1
#     return inventory

# Example usage
print(update_inventory({"apple": 2, "banana": 3}, ["apple", "orange", "apple"]))
print(update_inventory({"pen": 10, "pencil": 5}, ["pencil", "notebook", "pen"]))

# Question 6 - Unique Values

def unique_values(d):
    return list(set(d.values()))

# Alternative solution 1
# def unique_values(d):
#     unique_set = set() # Initialize an empty set
#     for value in d.values():
#         unique_set.add(value)
#     return list(unique_set)

# Alternative solution 2: without using set
# def unique_values(d):
#     unique_list = []
#     for value in d.values():
#         if value not in unique_list:
#             unique_list.append(value)
#     return unique_list

# Example usage
print(unique_values({"a": 1, "b": 2, "c": 1, "d": 3}))
print(unique_values({"apple": "fruit", "carrot": "vegetable", "banana": "fruit"}))

# Question 7 - Merge Dictionaries

def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

# Alternative solution, without using copy() and update() methods
# def merge_dicts(d1,d2):
#     merged = {}
#     for k, v in d1.items():
#         merged[k] = v
#     for k, v in d2.items():
#         merged[k] = v
#     return merged

# Example usage
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
print(merge_dicts({"name": "Alice", "age": 25}, {"age": 30, "city": "NY"}))

# Question 8 - Char Frequency Counter

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Alternative solution: without get()
# def char_frequency(s):
#     freq = {}
#     for char in s:
#         if char in freq: # An existing char
#             freq[char] = freq[char] + 1
#         else: # The first encounter with char
#             freq[char] = 1
#     return freq

# Example usage
print(char_frequency("hello"))
print(char_frequency("abracadabra"))

# Question 9 - Find the Max Key

def max_key(d):
    return max(d, key=d.get)

# Alternative solution 1
# def max_key(d):
#     highest_key = None
#     highest_value = float('-inf')  # Start with the lowest possible value
#     for key, value in d.items():
#         if value > highest_value:
#             highest_value = value
#             highest_key = key
#     return highest_key

# Alternative solution 2
# def max_key(d):
#     highest_key = None  # Initialize
#     highest_value = None  # Initialize
#
#     for key, value in d.items():
#         if highest_value is None or value > highest_value:
#             highest_value = value
#             highest_key = key
#
#     return highest_key


# Example usage
print(max_key({"apple": 5, "banana": 8, "orange": 3}))
print(max_key({"Alice": 67, "Bob": 85, "Eve": 75}))

# Question 10 - Frequency of Frequencies

def frequency_counter(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Alternative solution: without get()
# def frequency_counter(numbers):
#     freq = {}
#     for num in numbers:
#         if num in freq:
#             freq[num] = freq[num] + 1
#         else:
#             freq[num] = 1
#     return freq

# Example usage
list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(frequency_counter(list_of_numbers))
