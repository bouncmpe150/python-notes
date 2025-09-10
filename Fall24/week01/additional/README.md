# Variables / Expressions / Statements

## Question 1: Basic Variable Operations

 a) Create three different integer variables, and print them.

b) Take two floating-point numbers from the user, and print them.

c) Take three integers from the user (x, y, z), and then print their sum, product, average, and modulus (using the modulus operator).

Input: 10 5 3
Output: Sum: 18, Product: 150, Average: 6.0, Modulus of x % y: 0


<br>

## Question 2: Variable Type Identification and User Input

a) Create a boolean, a complex number, and a list variable. Print their types using the type() function.

b) Take a boolean, a complex number, and a list from the user as input. Print the variables along with their types.

Input: True, 3+4j, [1, 2, 3]
Output: True <class 'bool'>, (3+4j) <class 'complex'>, [1, 2, 3] <class 'list'>


<br>

## Question 3: Basic Mathematical Operations

Write a program that takes 4 integers from the user and prints the sum, geometric mean, and product of the numbers.

Input: 2 4 8 16
Output: Sum: 30, Geometric Mean: 5.656, Product: 1024

<br>

## Question 4: Compound Interest Calculation

Use the formula for compound interest to take the principal amount (P), annual interest rate (r) in percentage, and number of years (t) as input. Calculate and print the compound interest for monthly compounding.

A = P * ( 1 + r/100 * 12)^2 * t where

A = Final amount after interest

P = Principal amount (initial investment)

r = Annual interest rate (in percentage)

t = Time duration in years


Input: 1000 5 2
Output: 1104.94

<br>

## Question 5: Type Conversion and Outcome Prediction 

Guess the outcome of each statement and check the results:

```
print(float('12.34') + 1)  
print(5 * 'hello')  
print(bool('False'))  
print('abc' * int(2.7))  
print(int(7.8) + int('3'))  
print('python' + '3')  
print(4 ** 2 // 8)  
print(str(10.5) + '7')  
print(float(2.5 + 3.5))  
print(int('50') * 0.5)  
```

<br>

## Question 6: Time Conversion

Write a program that calculates the amount of seconds in a given period of weeks, days, hours, minutes, and seconds.

Conversion rates:

1 week = 7 days
1 day = 24 hours
1 hour = 60 minutes
1 minute = 60 seconds


Input: 1 2 3 4 5
Output: Output in seconds: 788645

<br>

## Question 7: Change Calculation

A vending machine dispenses items in quantities of 20-cent coins and 5-cent coins. Write a function that takes an amount in cents and prints the number of 20-cent coins and 5-cent coins needed to make that amount (use the minimum number of coins possible).

Input: 145
Output: 20-cent coins: 7, 5-cent coins: 1

<br>


## Question 8: Custom Power Function 

Write a function called exponent that takes two integer parameters: base and exp. The function should return the expth power of base.

Input: 2 3
Output: 8


<br>

## Question 9: Sum of Even Numbers 

Write a program that takes 4 integers from the user and then prints the sum of the even numbers.

Input: 1 2 3 4
Output: 6

<br>

## Question 10: Perfect Number Check

Write a function that takes an integer and determines whether it is a perfect number or not. A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).

Input: 28
Output: True
Input: 15
Output: False


