# Dictionary

## Question 1 - Letter Count

Write a program that takes a string, then create a dictionary which has letters as keys and the counts of that letters as values. Then sort that dictionary by descending values and print out the letters and the frequency of that letters to console.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| What we think, we become. | e -> 0.21 <br />w -> 0.16 <br />h -> 0.11 <br />t -> 0.11 <br />a -> 0.05 <br />b -> 0.05 <br />c -> 0.05<br />i -> 0.05 <br />k -> 0.05 <br />m -> 0.05 <br />n -> 0.05 <br />o -> 0.05 |

## Question 2 - Different Types

Write a program that takes list of different types, and creates a dictionary which has each different type as keys and the list of elements of that type as as value. Then display all elements of each type like in the example.

| INPUT                                                        | OUTPUT                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [10, 4.20, False, 'Word', 'CMPE150', 30, 3.5, 9.99, 'oblivion', True, 68, 88, "88"] | <class 'int'> -> [10, 30, 68, 88]<br /> <class 'float'> -> [4.2, 3.5, 9.99] <br /><class 'bool'> -> [False, True]<br /> <class 'str'> -> ['Word', 'CMPE150', 'oblivion', '88'] |


## Question 3 - Zip Two Lists

Write a function that takes 2 lists, then returns a dictionary which has keys from the first one, values from the second one.

| INPUT                                                        | OUTPUT                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| list1 = ["melih", "burak", "ahmet", "recep", "melis"] list2 = [1,2,3,4,5] | {'melih': 1, 'burak': 2, 'ahmet': 3, 'recep': 4, 'melis': 5} |

## Question 4 - Dictionary Merge

Write a function that takes one or more dictionaries and combines them in one result dictionary. The keys in the given dictionaries can overlap. In that case you should combine all values in a list. Duplicate values should be preserved.

| Input                                              | Output                                         |
| -------------------------------------------------- | ---------------------------------------------- |
| {"A": 1, "B": 2} {"A": 3}                          | {"A": [1, 3]}, "B": [2]}                       |
| {"A": 1, "B": 2, "C": 3}                           | {"A": [1], "B": [2], "C": [3]}                 |
| {"A": 1, "B": 2, "C": 3} {"A": 4, "D": 5} {"A": 4} | {"A": [1, 4, 4], "B": [2], "C": [3], "D": [5]} |

## Question 5 - Data Collection

Write a program that reads lines from the input. Each line will be composed of 4 words, name of the game, genre of the game, year of release and the producer respectively. If a line is equal to "exit", stop reading. Store the games in a dictionary. Their values should also correspond to dictionaries composed of their genre, release_data and producer.

| Input                                                        | Output                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| RDR2 Action 2018 Rockstar<br />Fifa14 Sports 2013 EA<br />Borderlands Shooter 2009 Gearbox<br />Skyrim RPG 2011 Bethesda<br />Wall-E Platform 2008 THQ<br />exit | {'RDR2': {'genre': 'Action', 'release_date': '2018', 'producer': 'Rockstar'},<br/>'Fifa14': {'genre': 'Sports', 'release_date': '2013', 'producer': 'EA'},<br/>'Borderlands': {'genre': 'Shooter', 'release_date': '2009', 'producer': 'Gearbox'},<br/>'Skyrim': {'genre': 'RPG', 'release_date': '2011', 'producer': 'Bethesda'},<br/>'Wall-E': {'genre': 'Platform', 'release_date': '2008', 'producer': 'THQ'}} |

## Question 6 - Sorting Dictionary

Write a function that returns a sorted list of (key, value) tuples. The list must be sorted by the value and be sorted largest to smallest.

| Input                                     | Output                                         |
| ----------------------------------------- | ---------------------------------------------- |
| {3:1, 2:2, 1:3}                           | [(1,3), (2,2), (3,1)]                          |
| {'a' :5, 'b' :10, 'c' :2, 'd' :3, 'e' :8} | [('b',10), ('e',8), ('a',5), ('d',3), ('c',2)] |

## Question 7 - Word Frequency

Write a program that prompts the user for a sentence. Split the sentence into words and store the frequency of each word (number of occurrences). Then print the words in a sorted manner from most common to the least common. If there is a tie, print the word that comes first in the original sentence.

*Hint: You can use sorted(dict_, key=dict_.get) function to sort a dictionary according to the values. In order to get the reversed version of this, add reverse = True parameter.*

| INPUT                                                        | OUTPUT                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| "one two two three three four four four four"                | "four three two one"                                    |
| "fair is foul and foul is fair"                              | "fair is foul and"                                      |
| "How much wood would a woodchuck chuck if a woodchuck could chuck wood?" | "a woodchuck chuck How much wood would if could wood? " |

## Question 8 - Anagrams

Anagram is a word formed by rearranging the letters of a different word (heart, earth). Write a program that takes a word list and prints out all the anagrams in the word list.

| Input                                                        | Output                                     |
| ------------------------------------------------------------ | ------------------------------------------ |
| ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"] | ['percussion', 'supersonic', 'car', 'arc'] |

## Question 9 - Vasya - Clerk

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

| Input                 | Output | Explanation                                                  |
| --------------------- | ------ | ------------------------------------------------------------ |
| [25, 25, 50]          | YES    |                                                              |
| [25, 100]             | NO     | Vasya will not have enough money to give change to 100 dollars |
| [25, 25, 50, 50, 100] | NO     | Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50) |


