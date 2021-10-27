# Loops

## Question 1 - Staaaars

### Question 1a

Write a program that prints 1 star ('\*') to the screen.

### Question 1b

Write a program that prints 10 stars ('\*') next to each other to the screen.

### Question 1c

Write a program that reads an integer N and prints N stars ('\*') vertically to the screen.

### Question 1d

Write a program that reads an integer N and prints N stars ('\*') next to each other to the screen.



## Question 2 - Numbeeeers

Write a program that reads an integer N and prints numbers from 1 to N to the screen.

| INPUT |  OUTPUT   |
| :---: | :-------: |
|   5   | 1 2 3 4 5 |
|   2   |    1 2    |



## Question 3 - Hooping Numbers

### Question 3a

Write a program that reads 3 integers A, B and t from the user. Then prints numbers from A to B with increment of t. Assume that B > A.

| INPUT  |    OUTPUT    |
| :----: | :----------: |
| 7 16 3 |  7 10 13 16  |
| 2 30 6 | 2 8 14 20 26 |

### Question 3b

Write a program that reads 3 integers A, B and t from the user. Then prints numbers from B to A with decrement of t. Assume that B > A.

| INPUT  |    OUTPUT     |
| :----: | :-----------: |
| 7 16 3 |  16 13 10 7   |
| 2 30 6 | 30 24 18 12 6 |



## Question 4 - Numbeeeers

Write a program that reads two integers A and B. Then prints the sum of numbers between A and B (excluding A and B). Assume that B > A.

| INPUT | OUTPUT |
| :---: | :----: |
|  3 8  |   10   |
| 2 13  |   22   |
|  3 5  |   75   |



## Question 5 - Average Team

Write a program that reads a number N, then reads N more numbers. Calculate the average of those N numbers.

|    INPUT     | OUTPUT |
| :----------: | :----: |
| 4<br>4 9 5 2 |  5.0   |
|    1<br>8    |  8.0   |

## Question 6 - Boom Boom POW

Write a program that takes 2 integers a and b, then prints the result of a^b (a\*a\*a...\*a\*a). 

| INPUT | OUTPUT |
| :---: | :----: |
|  3 4  |   81   |
| 2 10  |  1024  |

## Question 7 - Factorial

Write a program that takes an integer n and then prints n!.

| INPUT | OUTPUT  |
| :---: | :-----: |
|   5   |   120   |
|  10   | 3628800 |

## Question 8 - Sum of Products 

Write a program that takes an integer and then reads n lines containing two integers. The program then multiplies the integers in the same line and sums all the products. 


| INPUT | OUTPUT  |
| :---: | :-----: |
|   3<br /> 1 2 <br/> 2 3 <br/> 3 4 <br/>    |   20   |
|  2 <br/> 3 4 <br/> 5 10  | 62 |


# Nested Loops

## Question 1 - R\*\*\*tangle

### Question 1a

Write a program which takes two positive integers as N and M then prints a rectangle with size NxM. 

| Input | Output                               |
| :---: | ------------------------------------ |
|  3 4  | \*\*\*\*<br />\*\*\*\*<br />\*\*\*\* |
|  2 6  | \*\*\*\*\*\*<br />\*\*\*\*\*\*       |

### Question 1b

Write a program which takes two positive integers as N and M then prints a rectangle with size NxM which has stars (\*) at borders, and lines (-) inside.

| Input | Output                                               |
| :---: | ---------------------------------------------------- |
|  3 3  | \*\*\*<br />\*-\*<br />\*\*\*                        |
|  4 5  | \*\*\*\*\*<br />\*---\*<br />\*---\*<br />\*\*\*\*\* |

## Question 2 - TriNumber

### Question 2a

Write a program to display a right angle triangle using the number N, which will repeat the number for that row, like below.

| Input | Output                                  |
| :---: | --------------------------------------- |
|   3   | 1<br />22<br />333                      |
|   5   | 1<br />22<br />333<br />4444<br />55555 |

### Question 2b

Write a program to display a right angle triangle with N number of rows, like below.

| Input | Output                                  |
| :---: | --------------------------------------- |
|   3   | 1<br />12<br />123                      |
|   5   | 1<br />12<br />123<br />1234<br />12345 |

<details><summary>Hint</summary> At each row, we iterate from 1 to the row number.</details>

### Question 2c

Write a program which takes two integer as N and x and display a right angle triangle with N number of rows formed by powers of x as follows:

| Input | Output                                |
| :---: | ------------------------------------- |
|  3 4  | 4<br />4 16 <br />4 16 64             |
|  4 3  | 3<br />3 9<br />3 9 27<br />3 9 27 81 |

<details><summary>Hint</summary> At each row, we take power of input integer from once to the row number times.</details>

## Question 3 - TriHard

Write a program which takes an integer N as input and prints a right triangle which consists of N many lines.

| Input | Output                                                       |
| :---: | ------------------------------------------------------------ |
|   3   | --\*<br/>-\*\*<br/>\*\*\*                                    |
|   5   | ----\*<br/>---\*\*<br/>--\*\*\*<br/>-\*\*\*\*<br/>\*\*\*\*\* |



