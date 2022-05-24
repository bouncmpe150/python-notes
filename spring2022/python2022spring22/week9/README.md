# Strings

## Question 1 - Voweeels
Write a function which takes a string that all characters are lowercase and returns the length of longest sequence of consecutive vowels. It should return 0 for the empty string. Vowels are a,e,i,o,u. 

| Input                         | Output     |
| ----------------------------- | ---------- |
| "happy beaar" | 3 |
| "how you doin?" | 2 |
| "aiaiai" | 6 |
| "try" | 0 |



## Question 2 - Palindrome

Write a function to check whether given string is palindrome or not. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward.

| Input | Output |
| ----- | ------ |
| madam | True   |
| radix | False  |

## Question 3 - Abbreviate

Write a function called abbreviation() that takes a string st.<br>
If st has strictly more than 14 characters: returned string:<br>
* has the same first and last two characters as st.
* the characters in the middle should be replaced by the number of characters being replaced. (if you are replacing 15 characters return value should look like ww15ww)<br>

Else return st as is.

| INPUT  | OUTPUT |
| ------ | ------ |
| afyonkarahisarlarstiramadiklarimizdan |  af33an    |
| helo|  helo     |


## Question 4 - Lower/Upper Counts

Write a program to calculate the number of uppercase and lowercase letters in a string.

| Input            | Output |
| ---------------- | ------ |
| CMPE will be fun | 9 4    |
| HeLLo WoRLD      | 7 3    |

## Question 5 - Requirements

Write a function which takes a password as parameter and return whether the password is valid or not. The password has the following requirements:

* The password must be at least 6 characters and at most 20 characters.

* It must contain at least one lowercase letter, one uppercase letter, and one number.

| Input   | Output |
| ------- | ------ |
| Covid19 | True   |
| 123456  | False  |

## Question 6  - Length

Write a program to find shortest and largest word in a given string.

| Input                              | Output         |
| ---------------------------------- | -------------- |
| the house is a long way from here  | a house        |
| This room is exclusively for women | is exclusively |


## Question 7 - Word Cases

Write a function that takes a string and returns it by modifying it such that every word with odd index should be lowercase and every word with even index should be uppercase.

| Input                                  | Output                                 |
| -------------------------------------- | -------------------------------------- |
| stop making sponge bob memes           | STOP making SPONGE bob MEMES           |
| CMPE will be fun in the next few years | CMPE will BE fun IN the NEXT few YEARS |


## Question 8 - Second Most Common
Write a program that prompts the user for a string. Then find and print out the second most repeated character (lowercase) in the string (not case-sensitive). Do not take whitespaces into consideration.

<em> Hint : You can use replace() method of strings to get rid of whitespaces. Then you can use count() method to check if a character is in the string. </em>
<em> Alternatively, you can use a dictionary to store the occurrences of each character. </em>

| INPUT  | OUTPUT |
| ------ | ------ |
| " Hey there partner! " |  "r"    |
| "CaN you CAn a CAN as a canner CaN CAn a CAN?"|  "n"     |
|  "    LEsSer leather weaTheREd weTTer weathEr BettEr"| "t"   |

## Question 9 - Not poor

Write a function to find the first appearance of the substring **'not'** and **'poor'** from a given string, if **'not'** follows the **'poor'**, replace the whole '**not'...'poor'** substring with **'good'. ** and return the resulting string.

| Input                        | Output              |
| ---------------------------- | ------------------- |
| The lyrics is not that poor! | The lyrics is good! |
| The lyrics is poor!          | The lyrics is poor! |


## Question 10 - Find and replace

Write a function that takes 3 strings ``input``, ``a`` and ``b`` and replaces all the instances of ``a`` in ``input`` with ``b``.

| ``input``                         |``a``|``b``| Output     |
| ----------------------------- |----|---| ---------- |
| This is another test |"is"|"is not"| This not is not another test |
| I mean, it went badly last time but surely it will go much better this time. |"it"|"filling zepplins with hydrogen"|I mean, filling zepplins with hydrogen went badly last time but surely filling zepplins with hydrogen will go much better this time.|
| Test test TeSt te st TEst teSt crest TEA  | "st TE" |" test "|Test test TeSt te testst teSt cretestA |



