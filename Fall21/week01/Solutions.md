## Question1

### a

```python
x = 5
y = 3
print(x)
print(y)
```

### b

```python
x = int(input())
y = int(input())
print(x)
print(y)
```

### c

```python
x = int(input())
y = int(input())
print(x+y, x-y, x*y, x**y, x%y)
```

## Question 2

### a

```python
x = 5
y = 1.7
z = "I am a string!"
print(type(x))
print(type(y))
print(type(z))
```

### b

```python
x = int(input())
y = float(input())
z = input()
print(x, y, z)
```

## Question 3

```python
x = int(input())
y = int(input())
z = int(input())
sum = x + y + z
print(sum, sum/3, x * y * z) 
```

## Question 4

```python
A = int(input())
i = int(input())
n = int(input())
# print(A * (1 + (i / 100)) ** n)
print('%.2f' % (A * (1 + (i / 100)) ** n))
```

## Question 5

```python
print(int('6') + int('4'))
print('1' + '4')
print(int(3.9))
print(str(5.3) + '2.7')
print(int('5') * str(0.6))
print(float('3' + '8.6'))
print(3.5 + 6.7)
print(2 ** 3 ** 2 / 32)
print(str(4.4) + str(7.3))
print(int(6.5) + float('6.5'))
print(int(4.5 + 3.2))
print(int(3.2) + int(float(str(3.2))))
```

## Question 6

```python
years = int(input())
months = int(input())
days = int(input()) 
hours = int(input())
minutes = int(input())

total_days = years * 365 + month * 30 + days
total_hours = total_days * 24 + hours
total_minutes = total_hours * 60 + minutes
print(total_minutes * 60)
```

## Question 7

```python
# as a program
# money = int(input())
# print('5tl banknotes:', money / 5)
# print('1tl banknotes:', money % 5)
# with functions
def to_banknotes(money):
    print('5tl banknotes:', money / 5)
	print('1tl banknotes:', money % 5)

to_banknotes(57)
to_banknotes(269)
```

## Question 8

```python
def volume(radius):
    return 4 / 3 * radius ** 3 * 3

print(volume(3))
result = volume(6)
print(result)
```

## Question 9

```python
def power(number, n):
    return number ** n

print(power(5, 2))
print(power(3, 2))
```

## Question 10

```python
a = int(input())
b = int(input())
c = int(input())

print(a * (a % 2) + b * (b % 2) + c * (c % 2))
```

## Question 11

```python
def is_square(number):
    sqroot = number ** 0.5
    sqroot_int = int(sqroot)
    return number == sqroot_int ** 2

print(is_square(23))
print(is_square(25))
```

