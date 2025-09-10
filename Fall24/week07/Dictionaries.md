## Question 1 - Word Count
Write a function that takes a string as input and returns a dictionary with each unique word as a key and its frequency as the value.

INPUT	OUTPUT

"hello world hello"	--> {"hello": 2, "world": 1}

"apple orange banana apple apple"	--> {"apple": 3, "orange": 1, "banana": 1}

<br>

## Question 2 - Grade Book
Write a function that takes a dictionary where keys are student names and values are lists of scores. The function should return a dictionary with student names as keys and their average score as the value.

INPUT	OUTPUT

{"Alice": [85, 90, 88], "Bob": [78, 82, 80], "Eve": [95, 90, 92]}  -->    {"Alice": 87.67, "Bob": 80.0, "Eve": 92.33}

<br>

## Question 3 - Value Inverter
Write a function that takes a dictionary and returns a new dictionary with keys and values swapped.

INPUT	OUTPUT

{"a": 1, "b": 2, "c": 3} -->	{1: "a", 2: "b", 3: "c"}

{"cat": "meow", "dog": "bark"} -->	{"meow": "cat", "bark": "dog"}

<br>

## Question 4 - Birthday Lookup
Write a program that takes a dictionary with names as keys and birthdates as values (in "YYYY-MM-DD" format). Allow the user to enter a name and return that person's birthdate if it exists, or "Not found" otherwise.

INPUT	OUTPUT

{"Alice": "1990-05-15", "Bob": "1989-12-20"}  -->    "Alice"	"1990-05-15"

{"Alice": "1990-05-15", "Bob": "1989-12-20"}  -->    "Eve"	"Not found"

<br>

## Question 5 - Inventory Management
Write a function that takes a dictionary representing an inventory (item names as keys and quantities as values) and a list of items to be added. If an item is already in the inventory, increase its quantity by 1; if not, add it with quantity 1.

INPUT	OUTPUT

{"apple": 2, "banana": 3}  ["apple", "orange", "apple"]	  -->  {"apple": 4, "banana": 3, "orange": 1}

{"pen": 10, "pencil": 5}   ["pencil", "notebook", "pen"]	-->    {"pen": 11, "pencil": 6, "notebook": 1}

<br>

## Question 6 - Unique Values
Write a function that takes a dictionary and returns a list of unique values.

INPUT	OUTPUT

{"a": 1, "b": 2, "c": 1, "d": 3}  -->  [1, 2, 3]

{"apple": "fruit", "carrot": "vegetable", "banana": "fruit"}  -->  ["fruit", "vegetable"]

<br>

## Question 7 - Merge Dictionaries
Write a function that takes two dictionaries and merges them into one. If there are any duplicate keys, the values from the second dictionary should overwrite those from the first.

INPUT	OUTPUT

{"a": 1, "b": 2}  {"b": 3, "c": 4}  -->    {"a": 1, "b": 3, "c": 4}

{"name": "Alice", "age": 25}  {"age": 30, "city": "NY"}   -->   {"name": "Alice", "age": 30, "city": "NY"}

<br>

## Question 8 - Char Frequency Counter
Write a function that takes a string and returns a dictionary containing the frequency of each character.

INPUT	OUTPUT

"hello"  -->  {"h": 1, "e": 1, "l": 2, "o": 1}

"abracadabra"  -->  {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}

<br>

## Question 9 - Find the Max Key
Write a function that takes a dictionary with string keys and integer values and returns the key with the highest value.

INPUT	OUTPUT

{"apple": 5, "banana": 8, "orange": 3}  -->  "banana"

{"Alice": 67, "Bob": 85, "Eve": 75}  -->   "Bob"

<br>

## Question 10 - Frequency of Frequencies
Write a function that takes a list of numbers and returns a dictionary where the keys are the numbers from the list and the values are the frequencies of those numbers.

INPUT	OUTPUT

[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]  -->  {1: 1, 2: 2, 3: 3, 4: 4}

[7, 5, 5, 7, 7, 7, 8]  -->  {7: 4, 5: 2, 8: 1}
