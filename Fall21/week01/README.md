## Question 1 

**a)** Create two integer variables, and print them

**b)** Take two integers from the user, and print them

**c)** Take two integers from the user (a, b), and then print their sum, difference, product, power and remainder. 

| Input | Output           |
| ----- | ---------------- |
| 13 5  | 18 8 65 371293 3 |

## Question 2

**a)** Create an integer, a float, and a string variable. Print their types, using the type() function. 

**b)** Take an integer, a float, and a string variable from the user. Print the variables.

## Question 3

Write a program that takes 3 integers from the user and then prints the sum, mean and multiple of the numbers.

| Input    | Output        |
| -------- | ------------- |
| 13 27 14 | 54 18.00 4914 |

## Question 4

Using the formula below of compound interest, take the **principal amount (A)**, **interest rate (i)** (per month) and **duration (n)** (months) and print the final amount.

<img src="https://render.githubusercontent.com/render/math?math=\large S = A * (1 %2B i/100)^{n}">


| Input     | Output  |
| --------- | ------- |
| 1000 12 5 | 1762.34 |
| 500 12 5  | 881.17  |

## Question 5

 Guess the outcome of each statement. Then check the results.

<em> Hint: You can multiply strings with integers. It basically performs the concatenation operation n many times. </em>
<br>

- print(int('6') + int('4'))  <br>
- print('1' + '4')<br>
- print(int(3.9))
- print(str(5.3) + '2.7')<br>
- print(int('5') * str(0.6))<br>
- print(float('3' + '8.6'))<br>
- print(3.5 + 6.7)<br>
- print(2 ** 3 ** 2 / 32)
- print(str(4.4) + str(7.3))<br>
- print(int(6.5) + float('6.5'))<br>
- print(int(4.5 + 3.2))<br>
- print(int(3.2) + int(float(str(3.2))))<br>

<em> Remarks: </em>
<br>
<em>

- Observe that float-to-int type conversion is not a rounding operation. int(3.9) = 3. To round floats, we will use a built-in function called round(). Stay tuned! <br>
- As you see, we can multiply strings with integers, but not floats. What does 3.14 times "pi" mean, anyway?  <br>
- Exponent operator ** has right-to-left associativity. <br>
  </em>
  <br>

## Question 6

Write a program that calculates the amount of seconds in a given period of years, months, days, hours and minutes respectively.

* 1 year = 365 days
* 1 month = 30 days

| Input     | Output    |
| --------- | --------- |
| 5 2 4 3 0 | 163220400 |
| 1 1 1 1 1 | 34218060  |

## Question 7

There is a cash machine with an infinite supply of 5tl banknotes and 1tl coins inside it.

Write a function that takes an integer  representing the amount of money requested by a customer. The function then prints the number of banknotes and coins given to the customer. (Machine must prefer giving away banknotes instead of coins if possible)

| Input | Output                                   |
| ----- | ---------------------------------------- |
| 57    | 5tl banknotes: 11 <br />1tl banknotes: 2 |
| 269   | 5tl banknotes: 53 <br />1tl banknotes: 4 |

## Question 8

Write a function that takes a radius and returns the volume of the sphere.

| Input | Output        |
| ----- | ------------- |
| 3     | 113.097335529 |
| 6     | 904.778684234 |

## Question 9

Write a function called `power` that takes two integer parameter as **number** and **n**. The function should return the **nth** power of **number**.

| Input | Output |
| ----- | ------ |
| 5 2   | 25     |
| 3 2   | 9      |
| 4 3   | 64     |

## Question 10 & 11 requires knowledge of Boolean expressions and they are for those with Python background. Solve them without using if statements. 

## Question 10

Write a program that takes 3 integers from the user and then prints the sum of odd numbers.

| Input  | Output |
| ------ | ------ |
| 3 4 5  | 8      |
| 2 2 4  | 0      |
| 1 9 15 | 25     |

## Question 11

When you multiply an integer by itself, the result is a square number.

Write a function that takes an integer and determines whether it is a square number or not.

| Input | Output |
| ----- | ------ |
| 25    | True   |
| 23    | False  |
| 0     | True   |
| -1    | False  |
