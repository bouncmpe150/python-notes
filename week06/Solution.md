## Question 1

```python
n = int(input())

while n != 1:
    print(n,end=" ")
    n = n*3 +1 if n %2 else n//2
print(1)
```

## Question 2

```python
N = int(input())

my_sum = 0
for i in range(1, N+1):
    my_sum *= 10
    for j in range(i):
        my_sum += N

print(my_sum)
```

## Question 3

```python
def binary_find(num, L):
    while len(L) != 0:
        if num == L[len(L)//2]:
            return True
        elif num > L[len(L)//2]:
            L = L[len(L)//2+1:]
        else:
            L = L[:len(L)//2]
    return False


```

## Question 4

```python
def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num
n = int(input())
reversed = reverse(n)
digit = 1
total = 0
while reversed > 0:
    total += (reversed % 10) ** digit
    digit += 1
    reversed = reversed // 10
print(n == total)

```

## Question 5

```python
def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while(b != 0):
        rem = a
        a = b
        b = rem % b
    return a

def relatively_prime(a, b):
    return gcd(a, b) ==1

def euler_totient(n):
    cnt = 0
    for i in range(n+1):
        cnt = cnt + 1 if relatively_prime(i, n) else cnt
    return cnt

a = int(input())
print(euler_totient(a))
```

## Question 6

```python
def max(limit, weight, profit):
	total_profit = 0
	sum = 0
	max_profit = -1
	max_index = -1
	while sum < limit:
		for i in range(len(weight)):
			profit_per_mass = profit[i]/weight[i]
			if profit_per_mass > max_profit:
				max_index = i
				max_profit = profit_per_mass
		if max_index == -1:
			break
		if sum + weight[max_index] <= weight[max_index]:
			total_profit += profit[max_index]
			sum += weight[max_index]
		profit[max_index] = 0
		max_index = -1
		max_profit = -1
	return total_profit

weight = [10, 20, 30]
profit = [4 , 5 , 60]
limit = 30

print(max(limit, weight, profit))
```

