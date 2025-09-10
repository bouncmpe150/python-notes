## Question 1 - Fibonacci

Write a program which reads a positive integer number N and prints the Nth fibonacci number. *0, 1, 1, 2, 3, 5, ...*

F<sub>0</sub> = 0 

F<sub>1</sub> = 1

F<sub>n</sub> = F<sub>n-2</sub> + F<sub>n-1</sub>

| INPUT | OUTPUT |
| ----- | ------ |
| 2     | 1      |
| 4     | 2      |
| 7     | 8      |

## Question 2 - Second Largest

Write a program that will take nonnegative integers as inputs until the user enters 0. Then prints the difference between of largest two numbers among given inputs.

| INPUT                                              | OUTPUT |
| -------------------------------------------------- | ------ |
| 12 <br />25 <br />3 <br />8 <br />0                | 13     |
| 15 <br />1 <br />2 <br />3 <br />8 <br />5 <br />0 | 7      |

## Question 3 - Digiiiits

Write a program that takes a number and prints its total digit count and sum of even digits.

| INPUT  | OUTPUT |
| ------ | ------ |
| 542175 | 6 6    |
| 24680  | 5 20   |
| 135    | 3 0    |

## Question 4 - Positive Mental Attitude

Write a program that will take integers as inputs until the user enters a negative number. Then shows the user the sum of all ODD non-negative numbers that is entered.

| INPUT                                                        | OUTPUT |
| ------------------------------------------------------------ | ------ |
| 4 <br />7 <br />45 <br />9 <br />2 <br />0 <br />0 <br />5<br />8 <br />-4 | 66     |
| 1 <br />1 <br />0 <br />1 <br />-1                           | 3      |

## Question 5 - NoBig

Write a program that reads numbers until the entered number is greater than the previous entered number. Then print the average of all entered numbers except the last one. Assume that at least two numbers will be entered.

| INPUT                                                     | OUTPUT |
| --------------------------------------------------------- | ------ |
| 5 <br />4 <br />3 <br />3 <br />8                         | 3.75   |
| 5 <br />4 <br />3 <br />3 <br />8 <br />7 <br />5 <br />9 | 3.75   |
| 1 <br />2                                                 | 1.0    |
| 100 <br />54 <br />46 <br />2 <br />3 <br />50            | 50.5   |

## Question 6 - Guess

Generate a random number between 1 and 100 (including 1 and 100). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. Also print the number of tries.

| Input                         | Output                                                       |
| ----------------------------- | ------------------------------------------------------------ |
| 35 <br />67 <br />73 <br />71 | Too low! <br />Too low! <br />Too high! <br />You got it! And it only took you 4 tries! |



## Question 7 - Sum Facts

Write a program which takes an integer as input and computes the sum of the factorial of each digit. For example, assume that the user enters 572 as the input. For each digit of the integer, you will compute the factorial. Then you will compute the sum of these factorials: 5! + 7! + 2! = 120 + 5040 + 2 = 5162.

| Input | Output |
| ----- | ------ |
| 572   | 5162   |
| 27    | 5042   |

## Question 8 - Sum of Digits

Write a program that takes an integer n and calculates sum of all digits. If the result has more than one digit, continue to calculate in this way until a single digit number is produced.

```
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
```

| INPUT | OUTPUT |
| ----- | ------ |
| 942   | 6      |
| 17703 | 9      |

## Question 9 - Prime factors

### Question 9a

Write a program that reads an integer N and prints all the numbers that can divide N.

| INPUT | OUTPUT             |
| ----- | ------------------ |
| 21    | 1 3 7 21           |
| 30    | 1 2 3 5 6 10 15 30 |

### Question 9b

Write a program that reads an integer N and prints the prime factorization of N.

*Hint: A non-prime number is always composed of prime numbers smaller than it.*

| INPUT | OUTPUT        |
| ----- | ------------- |
| 21    | 3 * 7         |
| 60    | 2 * 2 * 3 * 5 |

### Question 9c

Write a program that reads an integer N and prints the prime factorization of N in the form of exponents.

| INPUT | OUTPUT          |
| ----- | --------------- |
| 21    | 3^1 * 7^1       |
| 60    | 2^2 * 3^1 * 5^1 |

## Question 10 - Palindromic Primes

Palindromic number is a number that remains the same when its digits are reversed. A [palindromic prime](https://en.wikipedia.org/wiki/Palindromic_prime) is a prime number that is also a palindromic number. 

Write a program that prompts the user for two integers, starting and ending points. Then print out all the palindromic primes between starting and ending points inclusively.

| INPUT         | OUTPUT          |
| ------------- | --------------- |
| 10 <br />150  | 11 101 131      |
| 150 <br />350 | 151 181 191 313 |
| 700 <br />800 | 727 757 787 797 |
