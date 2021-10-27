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





## Question 4 - Numbeeeers

```python
A = int(input())
B = int(input())

result = 0

for i in range(A+1, B):
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



