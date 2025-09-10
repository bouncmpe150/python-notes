# Conditional Execution

## Q1
```python
num1 = int(input("Plese enter first number: "))
num2 = int(input("Plese enter second number: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("Multiple")
else:
    print("Not multiple")

```

## Q2 - Simple Sort

### Q2a

```python
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if num1 > num2:
    tmp = num1
    num1 = num2
    num2 = tmp
    
# Alternatively
# if num1 > num2:
#   num1, num2 = num2, num1

print(num1, num2)
```

Alternative solution:

```python
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if (num1 > num2):
  print(num2, num1)
else:
  print(num1, num2)

```

### Q2b

```python
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

#1 and 2
if (num1 > num2):
    tmp = num1
    num1 = num2
    num2 = tmp

#1 and 3
if (num1 > num3):
    tmp = num1
    num1 = num3
    num3 = tmp

#2 and 3
if (num2 > num3):
    tmp = num2
    num2 = num3
    num3 = tmp

print(num1, num2, num3)

# Another solution
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c
    
# Another solution (with Ternary if)

max_a_b = a if a > b else b
maximum = max_a_b if max_a_b > c else c

min_a_b = a if a < b else b
minimum = min_a_b if min_a_b < c else c

middle = a + b + c - minimum - maximum

print(minimum, middle, maximum)

""" We can find middle in another way
if a != minimum and a != maximum:
    middle = a
if b != minimum and b != maximum:
    middle = b
if c != minimum and c != maximum:
    middle = c
"""
```

## Question 3
 ```python
def is_leap_year(x):
    if x % 4 == 0 and x % 100 != 0:
        print("leap year")
    elif x % 400 == 0:
        print("leap year")
    else:
        print("not a leap year")

year= int(input())
is_leap_year(year)
 ```
 
 Alternative solution:
 
  ```python
def is_leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False

year = int(input())
output = is_leap_year(year)

if output:
    print("leap year")
else:
    print("not a leap year")
 ```
 
 ## Question 4
   ```python
import math

hour = int(input())
minute = int(input())

total_minutes = hour * 60 + minute

if total_minutes <= 15:
    print(15)
else:
    print(15 + 10 * math.ceil(total_minutes / 60))
 ```
 
 ## Question 5
  ```python
a, b = input().strip().split()
a = int(a)
b = int(b)

def greatest_common_divisor(a, b):
    if a < b:
        least = a
    else:
        least = b

    gcd = 0
    for i in range(1, least + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print(gcd)

greatest_common_divisor(a, b)
  ```
  Alternative solution:
  
  ```python
a, b = input().strip().split()
a = int(a)
b = int(b)

def greatest_common_divisor(a, b):
    if a < b:
        least = a
    else:
        least = b

    for i in range(least, 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            return gcd

print(greatest_common_divisor(a, b))
  ```
  
  
  ## Question 6
   ```python
  A, B = input().strip().split()
  A = int(A)
  B = int(B)
  
  
  def is_prime(n):
      if n <= 1:
          return False
  
      for num in range(2, n//2+1):
          if n % num == 0:
              return False
      return True
  
  
  for i in range(A, B+1):
      if is_prime(i):
          print(i, end=" ")
  ```
  
   ## Question 7
```python
  n = int(input())
  
  A_students = 0
  B_students = 0
  C_students = 0
  failed_students = 0
  
  for i in range(n):
      attendance, overall_score = input().strip().split()
      attendance = int(attendance)
      overall_score = int(overall_score)
  
      if attendance >= 75:
          if overall_score >= 80:
              A_students += 1
          elif overall_score >= 65:
              B_students += 1
          elif overall_score >= 50:
              C_students += 1
          else:
              failed_students += 1
      else:
          failed_students += 1
  
  print("Passed with A:", A_students)
  print("Passed with B:", B_students)
  print("Passed with C:", C_students)
  print("Failed the course:", failed_students)
  
```
  
   ## Question 8
   ```python
  x = input()
  if x % 15 == 0:
    print("FizzBuzz")
  elif x % 3 == 0:
    print("Fizz")
  elif x % 5 == 0:
    print("Buzz")
  else:
    print(x)
  ```
  
  ## Question 9
  ```python
  N = int(input())
  
  for i in range(1,N+1):
      if i % 2 == 0:
          print(i)
      else:
          for j in range(i):
              print(i,end='')
          print() 
  ```
  
  ## Question 10
  ```python
  A = int(input())
  B = int(input())
  
  flag = False
  for i in range(0, A):
      if A == B ** i:
          flag = True
          break
  if flag:
      print("Yes")
  else:
      print("No")
  ```
  
  Alternative solution:
  
  ```python
A = int(input())
B = int(input())

for i in range(0, A):
    if B ** i == A:
        print("Yes")
        break
    elif B ** i > A:
        print("No")
        break
  ```
  
## Question 11

  ```python
def is_perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def all_the_perfects(N, M):
    for i in range(N, M + 1):
        if is_perfect(i):
            print(i, end=" ")

all_the_perfects(1, 10000)
  ```

