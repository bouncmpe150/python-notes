## Question 1 - Set Operations
Write a function that takes two sets then prints union, intersection and difference operations between them.

INPUT -> OUTPUT

A = {1, 2, 3, 4, 5, 6}

B = {1, 1, 2, 7, 11} -> A ∪ B = {1, 2, 3, 4, 5, 6, 7, 11}, A ∩ B = {1, 2}, A / B = {3, 4, 5, 6}, B / A = {11, 7}

<br>

## Question 2 - Check Subset
Write a function is_subset that takes two sets as input and checks if the first set is a subset of the second.

INPUT ->	OUTPUT

Set1: {1, 2}, Set2: {1, 2, 3} -> True

Set1: {1, 4}, Set2: {1, 2, 3} -> False

<br>

## Question 3 - Remove Duplicates from List
Write a function remove_duplicates that takes a list as input and uses a set to remove duplicates, returning the list without duplicates.

INPUT -> OUTPUT

[1, 2, 2, 3, 4, 4] -> [1, 2, 3, 4]

<br>

## Question 4 - Common Elements in Two Lists
Write a function common_elements that takes two lists as input and returns a set of their common elements.

INPUT	-> OUTPUT

List1: [1, 2, 3], List2: [2, 3, 4] -> {2, 3}


<br>

## Question 5 - Find Unique Values Across Dictionaries
Write a function unique_values_across_dicts that takes two dictionaries and returns a set of all unique values across both.

INPUT	-> OUTPUT

Dict1: {"a": 1, "b": 2}, Dict2: {"c": 3, "d": 2} -> {1, 2, 3}

<br>

## Question 6 - Merge Inventories
Write a function merge_inventories that takes two dictionaries representing inventories (item names as keys and quantities as values) and merges them. If an item exists in both, add their quantities and return a single dictionary.

INPUT	-> OUTPUT

Inventory1: {"apple": 2, "banana": 3}, Inventory2: {"apple": 1, "orange": 4} -> {"apple": 3, "banana": 3, "orange": 4}

<br>

## Question 7 - Filter by Threshold
Write a function filter_by_threshold that takes a dictionary where keys are names and values are scores, and a threshold value. Return a set of names whose scores exceed the threshold.

INPUT	-> OUTPUT

Scores: {"Alice": 85, "Bob": 78, "Eve": 92}, Threshold: 80 -> {"Alice", "Eve"}

<br>

## Question 8 - Common Words in Sentences
Write a function common_words that takes two strings (representing sentences) and returns a set of words common to both sentences.

INPUT	-> OUTPUT

"I like apples and oranges", "She likes oranges and grapes" -> {"oranges", "and"}

<br>

## Question 9 - Power Set Generator
Write a function generate_power_set that takes a set and returns a list of all subsets (the power set).

INPUT	-> OUTPUT

{1, 2} -> [set(), {1}, {2}, {1, 2}]

{"a"} -> [set(), {"a"}]

<br>

## Question 10 - Find Anagrams Using Sets
Write a function find_anagrams that takes two strings and determines if they are anagrams (ignoring case and spaces) using sets.


INPUT	-> OUTPUT

"listen", "silent" -> True

"hello", "world" -> False



