## Question 1

```python
X = float(input())
Y = float(input())
total = X + Y
percent_X = X/total * 100
percent_Y = Y/total * 100
#print("%.2f%% %.2f%%" % (percent_X, percent_Y))
print("{:.2f}% {:.2f}%".format(percent_X, percent_Y))
```

## Question 2

```python
weight = float(input())
height = int(input()) / 100
bmi = weight / (height ** 2)
# print('%.2f' % bmi)
print("{:.2f}".format(bmi))
```

## Question 3

```python
x = int(input())
print((5 ** 5628) % 100 * (x - 1))
```

## Question 4

```python
a = float(input())
b = float(input())
c = float(input())

fraction_a = a - a // 1 
fraction_b = b - b // 1
fraction_c = c - c // 1

print(fraction_a, fraction_b, fraction_c)
```

## Question 5

```python
def division(dividend, divisor)
    quotient = dividend // divisor
    remainder = dividend % divisor
	print("quotient =", quotient, "remainder =", remainder)

division(9, 2)
division(156, 13)

```

## Question 6

```python
def number_of_bacteria(initial, t1, total_time):
    return  initial * 2**int(total_time/t1)
print(number_of_bacteria(1, 1, 2))
print(number_of_bacteria(5, 3, 8))
```

## Question 7

```python
def distance(x1, y1, x2, y2):
    return  ((x2-x1)**2 + (y2-y1)**2)**0.5

print(distance(5, 10, 10, 22))
```

## Question 8

```python
def laps(r, x1, x2, total_time): 
    pi = 3.14
    circumference = 2 * pi * r
    total_run_1 = total_time * x1
    total_run_2 = total_time * x2
    total_laps1 = int(total_run_1 / circumference)
    total_laps2 = int(total_run_2 / circumference)
    return total_laps1, total_laps
runner1, runner2 = laps(100, 300, 400, 30)
```

## Question 9

```python
import math
N = 20
C = 5
def find_index(X):	
	page_index = math.ceil(X / (N*C))
    page_items = X % (N*C)
    line_index = math.ceil(page_items / C)
    col_index = page_items - (line_index - 1) * C 
    return page_index, line_index, col_index
num = int(input("Number: "))
page_ix, line_ix, col_ix = find_index(num)
print(page_ix, line_ix, col_ix)
```

## Question 10

```python
def passer_rating(comp, att, yards, td, inter):
    C = (((comp/att * 100)-30) / 20)
    Y = (((yards/att)-3) / 4)
    T = ((td/att) * 20)
    I = (2.375 - ((inter/att) * 35))   
	return ((C + Y + T + I) / 6) * 100
comp = int(input())
att = int(input())   
yards = int(input())
td = int(input())
inter = int(input())
print(passer_rating(cmp, att, yards, td, inter))
```

## Question 11

```python
def estimated_population(year):
    num_year = year - 2021
    seconds = 365 * 24 * 60 * 60  # days * hours * minutes * seconds
    birth_per_year = seconds // 15
    death_per_year = seconds // 20
    immigrant_per_year = seconds // 100
	return population + num_year * (birth_per_year + immigrant_per_year - death_per_year)
population = 84.5 * (10** 6)
print(estimated_population(2030))
```

