# Question 1 - Set Operations
A = {1, 2, 3, 4, 5, 6}
B = {1, 1, 2, 7, 11}

def set_operations(A, B):
    union = A | B
    intersection = A & B
    difference_a_b = A - B
    difference_b_a = B - A
    return union, intersection, difference_a_b, difference_b_a
# Example
print(set_operations({1, 2, 3, 4, 5, 6}, {1, 1, 2, 7, 11}))

## Alternative
'''
def set_operations(set1, set2):
    print("A ∪ B = {}".format(set1.union(set2)))
    print("A ∩ B = {}".format(set1.intersection(set2)))
    print("A / B = {}".format(set1.difference(set2)))
    print("B / A = {}".format(set2.difference(set1)))

set_operations(A, B)
'''

# Question 2 - Check Subset
def is_subset(set1, set2):
    return set1 <= set2
# Example
print(is_subset({1, 2}, {1, 2, 3}))
print(is_subset({1, 4}, {1, 2, 3}))


# Question 3 - Remove Duplicates from List
def remove_duplicates(lst):
    return list(set(lst))
# Example
print(remove_duplicates([1, 2, 2, 3, 4, 4]))

# Question 4 - Common Elements in Two Lists
def common_elements(list1, list2):
    return set(list1) & set(list2)
# Example
print(common_elements([1, 2, 3], [2, 3, 4]))


# Question 5 - Find Unique Values Across Dictionaries
def unique_values_across_dicts(dict1, dict2):
    return set(dict1.values()) | set(dict2.values()) #set(dict1.values()).union(dict2.values())
# Example
print(unique_values_across_dicts({"a": 1, "b": 2}, {"c": 3, "d": 2}))

# Question 6 - Merge Inventories
def merge_inventories(inv1, inv2):
    # Find the union of keys using sets
    all_items = set(inv1.keys()) | set(inv2.keys())
    
    # Create the result dictionary by iterating through the unified set of keys
    result = {item: inv1.get(item, 0) + inv2.get(item, 0) for item in all_items}
    
    return result

# Example usage
inv1 = {"apple": 2, "banana": 3}
inv2 = {"apple": 1, "orange": 4}
print(merge_inventories(inv1, inv2))


'''
# Alternative
def merge_inventories(inv1, inv2):
    result = inv1.copy()
    for item, qty in inv2.items():
        result[item] = result.get(item, 0) + qty
    return result
# Example
print(merge_inventories({"apple": 2, "banana": 3}, {"apple": 1, "orange": 4}))
'''

# Question 7 - Filter by Threshold
def filter_by_threshold(scores, threshold):
    # Initialize an empty set to store the names that meet the threshold
    result = set()
    
    # Loop through each name and score in the dictionary
    for name, score in scores.items():
        # Check if the score exceeds the threshold
        if score > threshold:
            # Add the name to the result set if the condition is met
            result.add(name)
    
    # Return the set of names that passed the threshold
    return result

# Example usage
scores = {"Alice": 85, "Bob": 78, "Eve": 92}
threshold = 80
print(filter_by_threshold(scores, threshold))

'''
# Alternative
def filter_by_threshold(scores, threshold):
    return {name for name, score in scores.items() if score > threshold}
# Example
print(filter_by_threshold({"Alice": 85, "Bob": 78, "Eve": 92}, 80))
'''

# Question 8 - Common Words in Sentences
def common_words(sentence1, sentence2):
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    return words1 & words2
# Example
print(common_words("I like apples and oranges", "She likes oranges and grapes"))


# Question 9 - Power Set Generator
def generate_power_set(s):
    # Convert the set to a list so we can access elements by index
    s_list = list(s)
    
    # Initialize a list to store all subsets (the power set)
    power_set = []
    
    # Total number of subsets is 2^n, where n is the number of elements in the set
    num_subsets = 2 ** len(s_list)
    
    # Loop through all numbers from 0 to 2^n - 1 (each number represents a subset)
    for i in range(num_subsets):
        subset = []
        
        # For each bit in the binary representation of the current number
        for j in range(len(s_list)):
            # If the j-th bit of i is set (i.e., 1), include the corresponding element in the subset
            if i & (1 << j):
                subset.append(s_list[j])
        
        # Append the subset to the power set
        power_set.append(set(subset))  # We use a set to ensure elements are unique
    
    return power_set

# Example usage
print(generate_power_set({1, 2}))
print(generate_power_set({"a"}))


'''
# Alternative
from itertools import chain, combinations

def generate_power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
# Example
print(generate_power_set({1, 2}))
print(generate_power_set({"a"}))
'''

# Question 10 - Find Anagrams Using Sets
def find_anagrams(word1, word2):
    # Create dictionaries to store the frequency of each character
    word1_dict = {}
    word2_dict = {}

    # Count the characters in word1
    for char in word1.lower():
        word1_dict[char] = word1_dict.get(char, 0) + 1
    
    # Count the characters in word2
    for char in word2.lower():
        word2_dict[char] = word2_dict.get(char, 0) + 1
    
    # Compare the two dictionaries
    return word1_dict == word2_dict

# Example usage
print(find_anagrams("listen", "silent"))
print(find_anagrams("hello", "world"))

'''
# Alternative 1
from collections import Counter

def find_anagrams(word1, word2):
    # Convert both words to lowercase and count the frequency of each character
    word1_count = Counter(word1.lower())
    word2_count = Counter(word2.lower())
    
    # Compare the two frequency distributions (Counters)
    return word1_count == word2_count

# Example usage
print(find_anagrams("listen", "silent"))
print(find_anagrams("hello", "world"))
'''

'''
# Alternative 2
def find_anagrams(word1, word2):
    clean_word1 = ''.join(sorted(word1.replace(" ", "").lower()))
    clean_word2 = ''.join(sorted(word2.replace(" ", "").lower()))
    return clean_word1 == clean_word2
# Example
print(find_anagrams("listen", "silent"))
print(find_anagrams("hello", "world"))
'''
