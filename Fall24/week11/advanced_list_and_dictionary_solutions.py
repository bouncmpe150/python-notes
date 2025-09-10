### **Question 1 - Sort List with Custom Key**
def sort_by_second(lst):
    def get_second_element(x):
        return x[1]
    return sorted(lst, key=get_second_element)



print(sort_by_second([(1, 3), (3, 1), (2, 2)]))  # Output: [(3, 1), (2, 2), (1, 3)]



### **Question 2 - Count Elements**

def count_occurrences(lst):
    return {x: lst.count(x) for x in set(lst)}

print(count_occurrences([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}




### **Question 3 - Dictionary Merging**

def merge_dicts(d1, d2):
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Output: {'a': 1, 'b': 5, 'c': 4}




### **Question 4 - Remove Duplicates**


def remove_duplicates(lst):
    seen = set()  # To track the elements we have already seen
    result = []   # To store the result without duplicates
    for item in lst:
        if item not in seen:  # If the item is not in the seen set
            result.append(item)  # Add it to the result
            seen.add(item)       # Mark it as seen
    return result


print(remove_duplicates([1, 2, 2, 3, 1]))  # Output: [1, 2, 3]



### **Question 5 - Nested List Processing**

def sum_nested(nested_lst):
    return sum(sum(sublist) for sublist in nested_lst)

print(sum_nested([[1, 2], [3, 4], [5]]))  # Output: 15




### **Question 6 - Create Dictionary with Comprehension**

def square_dict(n):
    return {i: i ** 2 for i in range(1, n + 1)}

print(square_dict(5))  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}




### **Question 7 - Group Elements**

def group_by_length(lst):
    result = {}  # Initialize an empty dictionary to store grouped words.
    for word in lst:  # Iterate over each word in the input list.
        length = len(word)  # Calculate the length of the current word.
        if length not in result:  # Check if the length is not already a key in the dictionary.
            result[length] = []  # If not, initialize it with an empty list.
        result[length].append(word)  # Append the word to the list for this length.
    return result

print(group_by_length(["a", "bb", "ccc"]))  # Output: {1: ['a'], 2: ['bb'], 3: ['ccc']}



### **Question 8 - Dictionary from Two Lists**


def zip_to_dict(keys, values):
    if len(keys) != len(values): # Terminate if lengths are not same
        return
    return {keys[i]:values[i] for i in range(len(keys))}



### **Question 9 - Find Maximum Value**

def max_value(d):
    return max(d, key=d.get)

print(max_value({'a': 3, 'b': 5, 'c': 1}))  # Output: 'b'




### **Question 10 - Filter List with Condition**

def filter_greater(lst, threshold):
    return [x for x in lst if x <= threshold]

print(filter_greater([1, 2, 3, 4], 2))  # Output: [1, 2]




### **Question 11 - Dictionary Key Existence**

def key_exists(d, key):
    return key in d

print(key_exists({'a': 1, 'b': 2}, 'b'))  # Output: True




### **Question 12 - Nested Dictionary Access**

def access_nested_dict(d, keys):
    for key in keys:
        d = d[key]
    return d

print(access_nested_dict({'a': {'b': 2}}, ['a', 'b']))  # Output: 2




### **Question 13 - Reverse Dictionary**

def reverse_dict(d):
    return {v: k for k, v in d.items()}

print(reverse_dict({'a': 1, 'b': 2}))  # Output: {1: 'a', 2: 'b'}



### **Question 14 - Sort List by Frequency**

def sort_by_frequency(lst):
    # Step 1: Create a frequency dictionary
    freq = {x: lst.count(x) for x in set(lst)}

    # Step 2: Define a custom function for sorting key
    def sorting_key(x):
        return -freq[x]

    # Step 3: Sort using the custom function
    return sorted(lst, key=sorting_key)

print(sort_by_frequency([1, 2, 2, 3, 3, 3]))  # Output: [3, 3, 3, 2, 2, 1]




### **Question 15 - Remove Dictionary Entries**

def remove_by_value(d, threshold):
    return {k: v for k, v in d.items() if v >= threshold}

print(remove_by_value({'a': 3, 'b': 1, 'c': 5}, 3))  # Output: {'a': 3, 'c': 5}


### Question 16


def unpack_tuple(tpl):
    a, b, c = tpl
    return a, b, c

# tpl = (1, 2, 3)
# print(unpack_tuple(tpl))
# output: 1, 2, 3


### Question 17
def tuple_length(tpl):
    return len(tpl)

# tpl = (10, 20, 30, 40)
# print(tuple_length(tpl))
# output: 4


### Question 18

def check_membership(tpl, value):
    return value in tpl

#tpl = (1, 2, 3, 4)
#value = 3
#print(check_membership(tpl, value))

#output True

### Quesiton 19 

def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2

# tpl1 = (1, 2)
# tpl2 = (3, 4)
# print(concatenate_tuples(tpl1, tpl2))
# output: (1, 2, 3, 4)

### Question 20

def slice_tuple(tpl, start, end):
    return tpl[start:end]

# tpl = (10, 20, 30, 40, 50)
# start = 1
# end = 4
# print(slice_tuple(tpl, start, end))
# (20, 30, 40)

