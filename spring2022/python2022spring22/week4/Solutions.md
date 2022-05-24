# Loops

## Question 1 - Staaaars

### Question 1a

```python
print('*')
```

### Question 1b

```python
print('**********')
```

### Question 1c

```python
N = int(input())

for i in range(N):
    print('*')
```

### Question 1d

```python
N = int(input())

for i in range(N):
    print('*', end='')
```

## Question 2 - Numbeeeers

```python
N = int(input())

for i in range(N):
    print(i+1, end=' ')

# OR

for i in range(1, N+1):
    print(i, end=' ')
```

## Question 3 - Hooping Numbers

### Question 3a

```python
A = int(input())
B = int(input())
t = int(input())

for i in range(A, B+1, t):
    print(i, end=' ')
```

### Alternative

```python
A, B, t = input().strip().split()
A = int(A)
B = int(B)
t = int(t)

for i in range(A, B+1, t):
    print(i, end=' ')
```



### Question 3b

```python
A = int(input())
B = int(input())
t = int(input())

for i in range(B, A-1, -t):
    print(i, end=' ')
```

### Alternative

```python
A, B, t = input().strip().split()
A = int(A)
B = int(B)
t = int(t)

for i in range(B, A-1, -t):
    print(i, end=' ')
```

## Question 4 - Even Numbeeeers

```python
A = int(input("A: "))
B = int(input("B: "))

result = 0

for i in range(A+1, B):
    if i % 2 == 0:
        result += i

print(result)
```

## Question 5 - Average Team

```python
N = int(input())

result = 0

for _ in range(N):
    x = int(input())
    # result = result + x 
    result += x

print(result/N)
```

## Question 6 - Boom Boom POW

```python
a = int(input("a: "))
b = int(input("b: "))

result = 1

for _ in range(b):
    result *= a

print(result)

```

## Question 7 - Factorial

```python
n = int(input())

result = 1
for i in range(n):
    result *= i+1

print(result)
```

## Question 8 - Sum of Products

```python
n = int(input())
total = 0

for i in range(n):
    x1, x2 = input().strip().split()
    total += int(x1) * int(x2)
print(total)
```

## Question 9 - Fibonacci

```python
N = int(input("N: "))

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
    
# OR

"""
     F_x_2 + F_x_1 = F_x
F_0: 0
F_1: 1
F_2: 0 + 1 = 1
F_3: 1 + 1 = 2
F_4: 1 + 2 = 3
F_5: 2 + 3 = 5
F_6: 3 + 5 = 8
F_7: 5 + 8 = 13

0 1 1 2 3 5 8 13
"""

n = int(input()) - 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    F_x_2 = 0
    F_x_1 = 1
    index = 2
    while index < n:
        F_sum = F_x_2 + F_x_1
        F_x_2 = F_x_1
        F_x_1 = F_sum
        index = index + 1

    print(F_x_2 + F_x_1) 
```

## Question 10 - list
```python
items = [3, 4, -9, 4]
sum = 0
for x in items:
    sum += x
print(sum)
```

# Nested Loops

## Question 1 - R\*\*\*tangle

### Question 1a

```python
N = int(input("N: "))
M = int(input("M: "))

for _ in range(N):
    for _ in range(M):
        print("*", end='')
    print()
```

### Question 1b

```python
N = int(input("N: "))
M = int(input("M: "))

for _ in range(M):
    print("*", end='')
print()

for _ in range(N-2):
    print("*", end='')
    for _ in range(M-2):
        print("-", end='')
    print("*")

for _ in range(M):
    print("*", end='')
```

## Question 2 - TriNumber

### Question 2a

```python
N = int(input())

for i in range(1, N+1):
    for j in range(i):
        print(i, end='')
    print()
```

### Question 2b

```python
N = int(input())

for i in range(1, N+1):
    for j in range(i):
        print(j+1, end='')
    print()
```

### Question 2c

```python
N = int(input())
x = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(x ** j, end=' ')
    print()
```

## Question 3 - TriHard

```python
N = int(input())

for i in range(1, N+1):
    for j in range(N - i):
        print('-', end='')
    for j in range(i):
        print('*', end='')
    print()
```

#Turtle

##Question 1 - Spiral square

'''
   python
   import turtle
 
   t = turtle.Turtle()
   side = 200
   for i in range(100):
       t.forward(side)
       t.right(90) 
       side = side - 2
'''
