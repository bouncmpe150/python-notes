# Week 10

## Question 1 - What is your Type?

Write a program that only prints the strings and integers from a given list. The outputs should look like the example

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
|["pasta",14, False, "True", 3.5,"makarna",(3,8),12] | pasta 14 True makarna 12  |
|[13,51.5,(False,3),"9"] | 13 9 | 

## Question 2 - Slice and Dice

Write a program that takes a list. If the list has more than 5 items in it and the number of items is odd, the program prints the list without the 3 items in the middle. If the list is shorter than 5 or the number of items are even, the original list is printed. 

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
|[3,325,12365,21,41,3,5,1,5] | [3, 325, 12365, 5, 1, 5] |
|["horse","chicken","pig","lamb","cow","ox","rooster","dog"] | ["horse","chicken","pig","lamb","cow","ox","rooster","dog"] | 
|[1,22,333,444] | [1,22,333,444] |

## Question 3 - To the left, to the left

Write a function that takes a list and an integer N and shift the every member by N number to the left and return the new shifted list back.


| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| N=3 <br /> ["everything","you","own","in","the", "box"] | ["in","the", "box","everything", "you", "own"] |
| N=11 <br /> ["i","r","r","e","p","l","a","c","a","b","l","e"] | ['a', 'b', 'l', 'e', 'i', 'r', 'r', 'e', 'p', 'l', 'a', 'c'] |

## Question 4 - The Odd Ones

Write a function that takes a lists and remove the odd integers from the list and return the list with only even integers.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| [1,5,2,3,5,6,82,63,5,6,12,5,436] | [2, 6, 82, 6, 12, 436] |
| [0,12,4,21,53,346,234] | [0, 12, 4, 346, 234] |

## Question 5 - Let's add on that!

Write a function that takes a list full of integers that adds every 2 consecutive items together and returns a list with the addition results between the added items.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| [1,3,5,7,8] | [1, 4, 3, 8, 5, 12, 7, 15, 8] |
| [3,5,4,124,5,3,9,7] | [3, 8, 5, 9, 4, 128, 124, 129, 5, 8, 3, 12, 9, 16, 7] |

## Question 6 - The Cloning Machine

Write a function that takes a list of integers and duplicates them by their value and returns the list with the duplicates.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| [1,2,3,4,5] | [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5] |
| [3,2,6,9,3,1] | [3, 3, 3, 2, 2, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 3, 3, 1] |

## Question 7 - Assassination

Write a function that takes a list and returns a list without the "N"th item on that list.

Hint= You can use pop(), remove() functions.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| ["apples","oranges", "JFK", "potato","tomato"] <br /> 3 | ["apples","oranges","potato","tomato"] |
| ["euro","dollar","won","yen","tl"] <br /> 5 | ["euro","dollar","won","yen"] |

## Question 8 - Flip It and Reverse It

Write a program that takes a list of strings from the user  and store them in a list until it reads ".". Then, it reverses the each string and reverses the order of the strings and prints the result as a single string without the ".".

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
|I <br /> put <br /> my <br /> thang <br /> down <br /> flip <br /> it <br /> and <br /> reverse <br /> it <br /> . | ti esrever dna ti pilf nwod gnaht ym tup I |

## Question 9 - Sorter Hat

Write a program that takes a list of strings or list of integers and prints the list in alphabetical order/ascending order.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| [1,5,54,312,52,9] | [1, 5, 9, 52, 54, 312] |
| ["Slytherin","Gryffindor", "Ravenclaw","Hufflepuff"] | ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'] |

## Question 10 - Popular Item

Write a function that finds the most recurring integer in list of integers and prints that integer.

| INPUT                     | OUTPUT                                                       |
| ------------------------- | ------------------------------------------------------------ |
| [3,2,1,2,2,2,3,1,1,3,2,5,1] | 2 |
