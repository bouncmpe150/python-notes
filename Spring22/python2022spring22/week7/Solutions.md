## Question 1 - Fibonacci

```python
N = int(input())

prev = 0
curr = 1

for _ in range(3, N+1):
    next = prev + curr
    prev = curr
    curr = next

if N <= 0:
    print("Invalid!")
elif N == 1:
    print(prev)
else:
    print(curr)
```

## Question 2 - Second Largest

```python
x = int(input())
largest = 0
second = 0
    
while x != 0:
    if x > largest:
        second = largest
        largest = x
    elif x > second:
        second = x
    x = int(input())
            
print(largest-second)
```

## Question 3 - Digiiiits

```python
x = int(input())

count = 0
even_sum = 0

while x > 0:
    digit = x % 10
    if digit % 2 == 0:
        even_sum += digit
    count += 1

    x //= 10

print(count, even_sum)
```

## Question 4 - Positive Mental Attitude

```python
odd_sum = 0

x = int(input())
while x >= 0:
    if x % 2 == 1:
        odd_sum += x
    x = int(input())

print(odd_sum)
```

## Question 5 - NoBig

```python
total_sum = 0
count = 1

x = int(input())
y = int(input())
total_sum += x
while y <= x:
    total_sum += y
    count += 1

    x = y
    y = int(input())

print(total_sum/count)
```

## Question 6 - Guess

```python
import random

number = random.randint(1,100)
count = 0

while True:
    guess = input("Make your guess: ")
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")
        break
```

## Question 7 - Sum Facts

```python
x = int(input())

fact_sum = 0

while x > 0:
    digit = x % 10
    fact = 1
    for i in range(2, digit+1):
        fact *= i
    fact_sum += fact

    x //= 10

print(fact_sum)
```

## Question 8 - Sum of Digits

```python
n = int(input())

while n >= 10:
    sum = 0
    while n:
        sum += n%10
        n //= 10
    n = sum

print(n)
```

## Question 9 - Prime factors

### Question 9a

```python
number = int(input())
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end =" ")

```

### Question 9b

```python
number = int(input())
for i in range(2, number + 1):
    while number % i == 0:
        number //= i
        print(i, end=" ")

```

This works because at any point in the loop, number doesn't have any factors smaller than `i`. Therefore, `i` has to be prime if it divides `number`.

### Question 9c

```python
number = int(input())
firstPrime = True
for i in range(2, number + 1):
    count = 0
    while number % i == 0:
        number //= i
        count += 1
    if count > 0:
        if firstPrime:
            firstPrime = False
        else:
            print(" * ", end="")
        print(i, "^", count, end="")

```

## Question 10 - Palindromic Primes

```python
def reverse_number(number):
    reverse = 0
    while num != 0:
        digit = num % 10
        num = num // 10
        reverse = reverse * 10 + digit
    return reverse

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
start = int(input())
end = int(input())

for i in range(start, end + 1): 
    if reverse_number(i) == i and is_prime(i):
    	print(i, end = " ")

```
  
  ## Question 11
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
  
## Question 12

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