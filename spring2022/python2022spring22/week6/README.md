# Conditional Execution

## Question 1 - Multiple
Write a program which calculates whether any given two numbers are multiples of one another.

| Input | Output       |
| ----- | ------------ |
| 2 4   | Multiple     |
| 4 2   | Multiple     |
| 5 3   | Not Multiple |

## Question 2 - Simple Sort

### Question 2a

Write a program that takes 2 integers from the user and then prints these integeres in an ascending order using a single if statement.

| Input | Output |
| ----- | ------ |
| 3 5   | 3 5    |
| 5 3   | 3 5    |

### Question 2b

Write a program that takes 3 integers from the user and then prints these integeres in an ascending order

| Input | Output |
| ----- | ------ |
| 1 3 2 | 1 2 3  |
| 3 2 1 | 1 2 3  |
| 2 3 1 | 1 2 3  |

## Question 3 - Leap
A leap year is a calendar year that contains an additional day added to keep the calendar year synchronized with the astronomical year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.
These extra days occur in each year which is an integer multiple of 4, except for the years evenly divisible by 100, but not by 400. Given a year between 1 and 10000, you will write a function that find whether it is a leap year or not.
  
  |  INPUT | OUTPUT |
| :------: | :------: |
| 1005 | not a leap year |
| 4 | leap year |
| 1000 | not a leap year |
| 4000 | leap year |

## Question 4 - Parking Fee
A parking lot "Park150" is charging its users as follows:  
  <= 15 minutes ---> 15 liras  
  After 15 minutes, users pay 10 liras per hour, as well as the first 15 liras.  
Given two integers hour and minute, write a program to calculate and print the total amount the user has to pay.  
For example: An input "1 28" means that the customer's car stayed in "Park150" for an hour and 28 minutes. So s/he has to pay 15 + 2\*10 liras.
You can assume that hour and minute will always be non-negative integers and minute will always be less than 60.
  |  INPUT | OUTPUT |
| :------: | :------: |
| 0 45 | 25 |
| 1 34 | 35 |
| 2 0 | 35 |
| 4 59 | 65 |

## Question 5 - GCD
In mathematics, the greatest common divisor (GCD) of two or more integers is the largest positive integer that divides each of the integers. For two integers x, y, the greatest common divisor of x and y is denoted by gcd(x,y).
For example, gcd(8,12)=4. Without using recursion, write a function that finds GCD of two given integers.

  |  INPUT | OUTPUT |
| :------: | :------: |
| 14, 21 | 7 |
| 1, 300 | 1 |
| 256, 16 | 16 |
| 109, 109 | 109 |

## Question 6 - Prime
Given two integers A and B, find and print all the prime integers that are between A and B (including A and B). You can assume that B will always be bigger than or equal to A.
  |  INPUT | OUTPUT |
| :------: | :------: |
| 1 5 | 2 3 5 |
| 50 100 | 53 59 61 67 71 73 79 83 89 97 |
| -3 10 | 2 3 5 7 |
| 24 28 |   |

## Question 7 - Grade
There are n students enrolled in the CmpE150 course. At the end of the semester students can pass the course only if they attended at least 75% of the lectures and have a minimum overall score of 50, otherwise they fail.  
A student passes CmpE150  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with "A" if s/he has an overall score that is greater than or equal to 80,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with "B" if s/he has an overall score that is greater than or equal to 65,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with "C" if s/he has an overall score that is greater than or equal to 50.  
Write a program that prints the number of students that passed with "A", "B", "C" and the students that failed the course by taking n (the number of students), then the attendance (as a percentage) and the overall scores of these students.
  |  INPUT | OUTPUT |
| :------: | :------: |
| 4 <br />75 90 <br />75 60 <br />60 60 <br />75 40 | Passed with A: 1 <br />Passed with B: 0 <br />Passed with C: 1 <br />Failed the course: 2 |
| 3<br />5 40<br />80 100<br />98 50 | Passed with A: 1<br />Passed with B: 0<br />Passed with C: 1<br />Failed the course: 1 |

## Question 8 - FizzBuzz
FizzBuzz is a simple game played by 2 people. Players should count in turns, yet they are forbidden from saying numbers divisible by 3 or 5. Instead they should say "Fizz" instead of numbers divisible by 3,"Buzz" instead of numbers divisible by 5, and "FizzBuzz" for numbers divisible by 15.

A demonstration:

Player1: 1

Player2: 2

Player1: Fizz

Player2: 4

Player1: Buzz

...

Player2: 14

Player1: FizzBuzz

Create a script that inputs a number and simulates a player's decision for a single number.

## Question 9 - Odd Print
Given an integer N, prints N line such that i'th line consists of i times the number "i" if i is odd, else just print i.

|  Input| Output|
| :------: | :------: |
| 3 | 1<br />2<br />333|
| 5 | 1<br />2<br />333<br />4<br />55555|


