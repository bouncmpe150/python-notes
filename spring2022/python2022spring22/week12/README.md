# Week 12 - Dictionary and Sets

## Question 1- Disctinctness

A distinct string is a string whose all characters occurs only once. Write a function that takes a string as an argument and checks whether given string is distinct or not.


| Input     | Output |
|-----------| ------ |
| slay      | True   |
| obliviate | False  |
| mahmut    | False  | 

## Question 2 - Seperating the Types

Write a program that takes lists of different types, then seperates the inputs according to their types. The program should print the inputs with their types just like in the example.

| Input                                                        | Output     |
| ------------------------------------------------------------ | ---------- |
| ["music",13,True, "black", (26,1),"16", "False","pencil"] | <class 'str'> ==> ['music', 'black', '16', 'False', 'pencil'] <br />  <class 'int'> ==> [13] <br /> <class 'bool'> ==> [True] <br />  <class 'tuple'> ==> [(26, 1)]  |

## Question 3 - imdB

Write a program that reads lines from the input. Each line will be composed of 4 words, name of the movie, genre of the movie, year of release and the director respectively. If a line is equal to "exit", stop reading. Store the games in a dictionary. Their values should also correspond to dictionaries composed of their genre, release_data and director

| Input                                                        | Output     |
| ------------------------------------------------------------ | ---------- |
| Black Swan, Thriller, 2010, Darren Aronofsky <br /> <br /> Dunkirk, Action, 2017, Christopher Nolan <br /> <br /> The Rocky Horror Picture Show, Musical, 1975, Jim Sherman <br /> <br /> The Matrix, Sci-Fi, 1999, Wachowski Sisters<br /> <br /> exit  | {'Black Swan': {'genre': ' Thriller', 'release_date': ' 2010', 'director': ' Darren Aronofsky'}, 'Dunkirk': {'genre': ' Action', 'release_date': ' 2017', 'director': ' Christopher Nolan'}, 'The Rocky Horror Picture Show': {'genre': ' Musical', 'release_date': ' 1975', 'director': ' Jim Sherman'}, 'The Matrix': {'genre': ' Sci-Fi', 'release_date': ' 1999', 'director': ' Wachowski Sisters'}} |

## Question 4 - String Who Should Not Be Written

Anagram is a word formed by rearranging the letters of a different word (heart, earth). Write a program that takes a tuple of two strings and prints out "Anagram" if the tuple has an anagram.

| Input                                        | Output     |
|----------------------------------------------| ---------- |
| ("peach","cheap")                            | Anagram |
| ("TOM MARVOLO RIDDLE","I AM LORD VOLDEMORT") | Anagram | 

## Question 5 - Cooking Oil Lines

The cooking oil prices have just been raised! There are a lot of people at the supermarket check-out line. Each of them has a single 200,100,50 Turkish liras. A liter of cooking oil costs 50  Turkish liras.

Yiğit is currently working as a cashier. He wants to sell cooking oil to every single person before the prices are raised again next week but he cannot accept credit cards at the moment or has any cash.

Can Yiğit sell cooking oil (only a liter to each) to every person and give change to all of them strictly in the order of the line?

Return YES, if Yiğit can sell cooking oil to every person and give change with the bills he has at that moment. Otherwise return NO.

| Input                 | Output | Explanation                                                  |
| --------------------- | ------ | ------------------------------------------------------------ |
| [50, 50, 100]          | YES    |                                                              |
| [50, 200]             | NO     | Yiğit will not have enough money to give change to 200 Turkish liras. |
| [50, 50, 100, 100, 200] | NO     | Yiğit will not have the right bills to give 150 Turkish liras of change (you can't make two bills of 50 from one of 100) |


