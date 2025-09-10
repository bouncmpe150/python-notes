# Variables / Expressions / Statements

## Q1

```
# a) Create three different integer variables, and print them
x, y, z = 10, 20, 30
print(x, y, z)

# b) Take two floating-point numbers from the user, and print them
a = float(input("Enter first float: "))
b = float(input("Enter second float: "))
print(a, b)

# c) Take three integers from the user (x, y, z), and then print their sum, product, average, and modulus (using the modulus operator)
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
z = int(input("Enter third integer: "))
sum_values = x + y + z
product_values = x * y * z
average_values = sum_values / 3
modulus = x % y

print(f"Sum: {sum_values}, Product: {product_values}, Average: {average_values}, Modulus of x % y: {modulus}")

```

<br>

## Q2
```
# a) Create a boolean, a complex number, and a list variable. Print their types using the type() function
boolean_var = True
complex_var = 4 + 5j
list_var = [1, 2, 3]

print(type(boolean_var))  # Output: <class 'bool'>
print(type(complex_var))  # Output: <class 'complex'>
print(type(list_var))     # Output: <class 'list'>

# b) Take a boolean, a complex number, and a list from the user as input. Print the variables along with their types.
boolean_var_user = bool(int(input("Enter a boolean (0 or 1): ")))  # Convert int to bool
complex_var_user = complex(input("Enter a complex number (e.g., 2+3j): "))
list_var_user = eval(input("Enter a list (e.g., [1, 2, 3]): "))  # Use eval to directly input a list

print(boolean_var_user, type(boolean_var_user))
print(complex_var_user, type(complex_var_user))
print(list_var_user, type(list_var_user))

```

<br>

## Q3
```
# Take 4 integers from the user and print the sum, geometric mean, and product of the numbers
import math

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
d = int(input("Enter fourth integer: "))

sum_values = a + b + c + d
product_values = a * b * c * d
geometric_mean = math.pow(product_values, 1/4)

print(f"Sum: {sum_values}, Geometric Mean: {geometric_mean:.3f}, Product: {product_values}")

```

<br>

## Q4
```
# Compound interest calculation
P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in percentage): "))
t = float(input("Enter the number of years: "))

A = P * (1 + r/(100 * 12))**(12 * t)  # Compound interest formula with monthly compounding
print(f"Final amount: {A:.2f}")

```

<br>

## Q5
```
# Guess the outcome of each statement and then check results

print(float('12.34') + 1)    # Output: 13.34
print(5 * 'hello')           # Output: hellohellohellohellohello
print(bool('False'))         # Output: True
print('abc' * int(2.7))      # Output: abcabc
print(int(7.8) + int('3'))   # Output: 10
print('python' + '3')        # Output: python3
print(4 ** 2 // 8)           # Output: 2
print(str(10.5) + '7')       # Output: 10.57
print(float(2.5 + 3.5))      # Output: 6.0
print(int('50') * 0.5)       # Output: 25.0

```

<br>

## Q6
```
# Time conversion to seconds
weeks = int(input("Enter the number of weeks: "))
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = (weeks * 7 * 24 * 3600) + (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds
print(f"Total seconds: {total_seconds}")

```

<br>

## Q7
```
# Change calculation using 20-cent and 5-cent coins
def coin_change(amount):
    twenty_cent_coins = amount // 20
    remainder = amount % 20
    five_cent_coins = remainder // 5
    print(f"20-cent coins: {twenty_cent_coins}, 5-cent coins: {five_cent_coins}")

amount = int(input("Enter the amount in cents: "))
coin_change(amount)


```

<br>


## Q8
```
# Custom power function
def exponent(base, exp):
    return base ** exp

base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))
print(exponent(base, exp))

```

<br>

## Q9
```
# Sum of even numbers
nums = [int(input(f"Enter number {i+1}: ")) for i in range(4)]
even_sum = sum(num for num in nums if num % 2 == 0)
print(f"Sum of even numbers: {even_sum}")

```

<br>

## Q10
```
# Check if a number is a perfect number
def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

number = int(input("Enter an integer: "))
print(is_perfect_number(number))

```
