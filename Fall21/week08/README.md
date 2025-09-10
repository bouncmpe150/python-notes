# Lists

## Question 1 - Large

Write a program that reads an integer N from the user, then reads N more integers from the user and store them in a list. Then prints elements larger than the average of numbers held in the array.

| Input                                                        | Output     |
| ------------------------------------------------------------ | ---------- |
| 10 <br />1 <br />2 <br />3 <br />4 <br />5 <br />6 <br />7 <br />8 <br />9 <br />10 | 6 7 8 9 10 |
| 4 <br />4 <br />1 <br />3 <br />8                            | 8          |



## Question 2 - Let's Count

Write a function that takes a list and find frequency of each element in the list then prints. Assume the numbers in the list will be between 0 and 100 (inclusive).

| INPUT                  | OUTPUT                                                       |
| ---------------------- | ------------------------------------------------------------ |
| 5 10 2 5 50 5 10 1 2 2 | 1 --> 1 <br />2 --> 3 <br />5 --> 3 <br />10 --> 2 <br />50 --> 1 |



## Question 3 - Fifth Powers

List comprehensions might enable you to turn loop-based codes into one line elegant expressions. Write a program that takes 5 integers as input and prints a new list consisting of the fifth power of each number. Try to construct and print the new list in just one line.

| INPUT             | OUTPUT                      |
| ----------------- | --------------------------- |
| [1, 2, 3, 5, 0]   | [1, 32, 243, 3125, 0]       |
| [4, 1, 6, -2, -3] | [1024, 1, 7776, -32, -243]  |
| [-3, -6, 2, 9, 0] | [-243, -7776, 32, 59049, 0] |


## Question 4 - To the left

Write a function which takes a list of numbers and an integer k and shifts the numbers to the left circularly by *k* and
return the shifted list.

| Input             | Output          |
| ----------------- | --------------- |
| [1, 2, 3, 4, 5] 2 | [3, 4, 5, 1, 2] |
| [2, 18, 6, 0] 3   | [0, 2, 18, 6]   |


## Question 5 - Reverse

Write a program which reads a list of integers from the user and store them in a list.

**a**. Then print them to the screen in reverse order.

**b.** Then reverse the order of these integers in the array and print the array.

| Input          | Output         |
| -------------- | -------------- |
| 3 1 -4 5 2     | 2 5 -4 1 3     |
| 15 7 2 89 8 12 | 12 8 89 2 7 15 |



## Question 6 - Remove X

Write a function that accepts a list and variable X and removes all occurrence of X from the list.

| INPUT                           | OUTPUT          |
| ------------------------------- | --------------- |
| [5, 20, 15, 20, 25, 50, 20], 20 | [5, 15, 25, 50] |


## Question 7 - Remove Duplicates

Write a function that takes a list of integers then returns without all duplicates.

| Input                                   | Output          |
| --------------------------------------- | :-------------- |
| [1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 2, 4, 5] | [1, 2, 3, 4, 5] |
| [0,0,0,0,0,0,0]                         | [0]             |



## Question 8 - Odd Occurrences

Write a function that takes a list and prints the elements that occur 2n+1 times. If there is no element with odd number
of occurrences then it should not print anything.

| Input                                           | Output    |
| ----------------------------------------------- | --------- |
| [1, 1, 2, 3, 4, 2, 'apple', 'banana', 'banana'] | 3 4 apple |
| [2, 2, 3, 3, 2]                                 | 2         |
| [ 'a' , 'b' , 'c' , 'c' , 'b' , 'a' ]           |           |

# Tuples

## Question 9 - Fractions

Fractions can be expressed as as tuple: (numerator, denominator).

Write a function that adds two fractions that are passed as tuples.

| Input         | Output   |
| ------------- | -------- |
| (1, 3) (4, 5) | (17, 15) |
| (3, 5) (1, 2) | (11, 10) |

## Question 10 - Points

Points can be expressed as as tuple: (x, y).

#### Question 10a - Distance

Write a function  **distance** which takes two tuples (points) and returns Euclidian distance between these points.

| Input           | Output |
| --------------- | ------ |
| (3, 0) (0, 4)   | 5.0    |
| (5, 8) (10, 20) | 13.0   |

#### Question 10b - Closest

Write a function which takes two tuples (points) and returns the point closest to the origin. *Use the distance
function.*

| Input          | Output |
| -------------- | ------ |
| (3, 0) (0, 4)  | (3, 0) |
| (11, 7) (6, 8) | (6, 8) |

#### Question 10c - Farthest

Write a program which takes an integer N and reads N points (given by their x and y coordinates) and determines the pair
that is the farthest apart.

| Input                                       | Output              |
| ------------------------------------------- | ------------------- |
| 3<br/>3 0<br/>0 0<br/>0 4                   | (0, 4)<br/>(3, 0)   |
| 5<br/>10 5<br/>4 8<br/>0 8<br/>4 5<br/>-1 2 | (-1, 2)<br/>(10, 5) |


