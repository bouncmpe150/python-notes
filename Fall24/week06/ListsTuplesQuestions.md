## Question 1

Write a program that reads an integer N from the user, then reads N more integers from the user and stores them in a list. Then prints elements larger than the average of numbers held in the array.

Example Test Case 1:
10 1 2 3 4 5 6 7 8 9 10 -> 6 7 8 9 10

Example Test Case 2:
4 4 1 3 8 -> 8

<br>

## Question 2

Write a function that takes a list, finds the frequency of each element, and then prints. Assume the numbers in the list will be between 0 and 100 (inclusive).

Example Test Case: 5 10 2 5 50 5 10 1 2 2 -> 

1 --> 1 

2 --> 3 

5 --> 3 

10 --> 2 

50 --> 1

<br>

## Question 3

List comprehensions enable you to turn loop-based codes into one-line elegant expressions.  Write a program that takes 5 integers as input and prints a new list of each number's fifth power. Try to construct and print the new list in just one line.

Example Test Case 1: [1, 2, 3, 5, 0] -> [1, 32, 243, 3125, 0]

Example Test Case 2: [4, 1, 6, -2, -3] -> [1024, 1, 7776, -32, -243]

Example Test Case 3: [-3, -6, 2, 9, 0] -> [-243, -7776, 32, 59049, 0]


<br>

## Question 4

Write a function that takes a list of numbers and an integer k shifts the numbers to the left circularly by k and returns the shifted list.

Example Test Case 1: [1, 2, 3, 4, 5] 2 -> [3, 4, 5, 1, 2]

Example Test Case 2: [2, 18, 6, 0] 3 -> [0, 2, 18, 6]

<br>

## Question 5

Write a function that takes a list as a parameter

a. Then print elements to the screen in reverse order.

b. Then reverse the order of these integers in the array and print the array.

Example Test Case 1: 3 1 -4 5 2 -> 2 5 -4 1 3

Example Test Case 2: 15 7 2 89 8 12 -> 12 8 89 2 7 15

<br>

## Question 6

Write a function that accepts a list and variable X and removes all occurrences of X from the list.

Example Test Case: [5, 20, 15, 20, 25, 50, 20], 20 -> [5, 15, 25, 50]

<br>

## Question 7

Write a function that takes a list of integers and then returns without all duplicates.

Example Test Case 1: [1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 2, 4, 5] -> [1, 2, 3, 4, 5]

Example Test Case 2: [0,0,0,0,0,0,0] -> [0]

<br>

## Question 8: 

Write a function that takes a list and prints the elements that occur 2n+1 times. If there is no element with an odd number of occurrences then it should not print anything.

Example Test Case 1: [1, 1, 2, 3, 4, 2, 'apple', 'banana', 'banana'] -> 3 4 apple

Example Test Case 2: [2, 2, 3, 3, 2] -> 2

<br>

## Question 9: 

Fractions can be expressed as tuples: (numerator, denominator). Write a function that adds two fractions that are passed as tuples.

Example Test Case 1: (1, 3) (4, 5) -> (17, 15)

Example Test Case 2: (3, 5) (1, 2) -> (11, 10)

<br>

## Question 10a: 

Points can be expressed as a tuple: (x, y). Write a function distance that takes two tuples (points) and returns the Euclidian distance between these points.

Example Test Case 1: (3, 0) (0, 4) -> 5.0

Example Test Case 2: (5, 8) (10, 20) -> 13.0

## Question 10b: 

Write a function that takes two tuples (points) and returns the point closest to the origin. Use the distance function.

Example Test Case 1: (3, 0) (0, 4) -> (3, 0)

Example Test Case 2: (11, 7) (6, 8) -> (6, 8)

## Question 10c: 

Write a program that takes an integer N and reads N points (given by their x and y coordinates) and determines the pair that is the farthest apart.

Example Test Case 1:

3

3 0

0 0

0 4

->

(0, 4)

(3, 0)


<br>

## Question 11:

Write a function that sorts elements of the list in ascending order.

INPUT-OUTPUT

4 2 8 6 7 3 1 5	        1 2 3 4 5 6 7 8

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

Example:

First Pass:

( 5 1 4 8 2 ) ?> ( 1 5 4 8 2 ), Here, the algorithm compares the first two elements, and swaps since 5 > 1.

( 1 5 4 8 2 ) ?> ( 1 4 5 8 2 ), Swap since 5 > 4

( 1 4 5 8 2 ) ?> ( 1 4 5 8 2 ), since these elements are already in order (8 > 5), no swap.

( 1 4 5 8 2 ) ?> ( 1 4 5 2 8 ), Swap since 8 > 2.

The largest element is at the end.

Second Pass:

( 1 4 5 2 8 ) ?> ( 1 4 5 2 8 )

( 1 4 5 2 8 ) ?> ( 1 4 5 2 8 )

( 1 4 5 2 8 ) ?> ( 1 4 2 5 8 ), Swap since 5 > 2

( 1 4 2 5 8 ) ?> ( 1 4 2 5 8 )

Third Pass:

( 1 4 2 5 8 ) ?> ( 1 4 2 5 8 )

( 1 4 2 5 8 ) ?> ( 1 2 4 5 8 ), Swap since 4 > 2

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )

Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Fourth Pass:

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )

( 1 2 4 5 8 ) ?> ( 1 2 4 5 8 )


