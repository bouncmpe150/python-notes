# Strings

## Question 1 - Voweeels

```python
def vowel(s):
    max_length, length = 0, 0
    for c in s:
        if c in 'oeaiu':
            length += 1
        else:
            length = 0
        max_length = max(length, max_length)
    return max_length

print(vowel("happy beaar"))
print(vowel("how you doin?"))
print(vowel("aiaiai"))
print(vowel("try"))
```


## Question 2 - Palindrome

```python
def is_palindrome(str):
    return str == str[::-1]
```

## Question 3 - Abbreviate

```python
def abbreviation(st):
    if (len(st) <= 14):
        return st
    else:
        return st[0:2] + str(len(st) - 4) + st[-2:]
```

## Question 4 - Lower/Upper Counts

```python
str = "HeLLo WoRLD"
lower_count, upper_count = 0, 0
for c in str:
    lower_count += c.islower()
    upper_count += c.isupper()

print(upper_count, lower_count)
```

## Question 5 - Requirements

```python
def is_valid(password):
    length = len(password)
    if length < 6 or length > 20:
        return False
    lower, upper, digit = 0, 0, 0
    for c in password:
        lower += c.islower()
        upper += c.isupper()
        digit += c.isdigit()
    return lower >= 1 and upper >= 1 and digit >= 1 

print(is_valid("Covid19"))
```

## Question 6  - Length

```python
sentence = input()
words = sentence.split()
lengths = [len(w) for w in words]
shortest_index = lengths.index(min(lengths))
longest_index = lengths.index(max(lengths))
print(words[shortest_index], words[longest_index])
```

## Question 7 - Word Cases

```python
def modify(str):
    words = str.split()
    new_str = ''
    for ix, word in enumerate(words):
        if ix % 2 == 0:
            new_str += word.upper() + ' '
        else:
            new_str += word.lower() + ' '
    return new_str

def modify2(str):
    return ' '.join([word.upper() if ix % 2 == 0 else word.lower() for ix, word in enumerate(str.split())])

print(modify('stop making sponge bob memes'))
print(modify2('stop making sponge bob memes'))

```


## Question 8 - Second Most Common
```python
string = str(input())
modified = string.replace(" ", "").lower()
Max = 0
secondMax = 0
second = ''
first = ''
for i in modified:
    occur = modified.count(i)
    if(occur > Max):
        second = first
        first = i
        secondMax = Max
        Max = occur
    elif(occur < Max and occur > secondMax):
        second = i
        secondMax = occur
print(first, second)
```

## Question 9 - Not poor
```python
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  if spoor > snot and snot > 0 and spoor > 0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
  return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
```

## Question 10 - Find and replace

```python

def find_and_replace(string, a, b):
    ix = 0
    while string.find(a, ix) != -1:
        ix = string.find(a, ix)
        string = string[:ix] + b + string[ix+len(a):]
        ix = ix + len(b)
    return string


print(find_and_replace("This is another test", "is", "is not"))
print(find_and_replace("I mean, it went badly last time but surely it will go much better this time.", "it", "filling zeppelins with hydrogen"))
print(find_and_replace("Test test TeSt te st TEst teSt crest TEA", "st TE", "test"))
```

