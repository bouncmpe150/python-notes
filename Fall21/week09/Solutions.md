# Dictionary

## Question 1 - Letter Count

```python
sentence = input()
my_dict = dict()
total_letter =0
for letter in sentence:
    if letter.isalpha():
        letter = letter.lower()
        total_letter += 1
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

sorted_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
for k,v in sorted_dict:
    print(k,"->","{:.2f}".format(v/total_letter))
```

## Question 2 - Different Types

```python
elements = [10, 4.20, False, 'Word', 'CMPE150', 30, 3.5, 9.99, 'oblivion', True, 68, 88, "88"]
element_dict = {}
for el in elements:
    if el not in element_dict:
        element_dict[type(el)] = [el]
    else:
        element_dict[type(el)].append(el)
for el_type, el_list in element_dict.items():
    print(el_type, '->', el_list)
```

## Question 3 - Zip Two Lists

```python
list1 = ["melih", "burak", "ahmet", "recep", "melis"]
list2 = [1,2,3,4,5]
def dict_2_lists(list1, list2):
    return dict(zip(list1, list2))

print(dict_2_lists(list1,list2))
```

Alternative:

```python
list1 = ["melih", "burak", "ahmet", "recep", "melis"]
list2 = [1,2,3,4,5]
zip_dict = {}
for l1, l2 in zip(list1, list2):
  zip_dict[l1] = l2

print(zip_dict)
```

## Question 4 - Dictionary Merge

```python
def merge(*dicts):
    mydict = dict()
    for d in dicts:
        for k, v in d.items():
            if k in mydict:
                mydict[k].append(d[k])
            else:
                mydict[k] = [v]
    return mydict
    
print(merge({"A": 1, "B": 2} , {"A": 3}))
```

Alternative:

```python
def merge(l_dicts):
    result_dict = {}
    for dictionary in l_dicts:
        for k, v in dictionary.items():
            if k not in result_dict:
                result_dict[k] = []
            result_dict[k].append(v)
    return result_dict
    
print(merge({"A": 1, "B": 2} , {"A": 3}))
```

## Question 5 - Data Collection

```python
lines = []
line = str(input())
while line != "exit":
    lines.append(line)
    line = str(input())

mydict = {}
for line in lines:
    line = line.split() # transform into a list
    info = {'genre' : line[1], 'release_date': line[2], 'producer':line[3]}
    mydict[line[0]] = info
print(mydict)
```

Alternative:

```python
game_dict = {}
while True:
    data = input().strip()
    if data == "exit":
      break
    name, genre, year, producer = data.split()
    game_dict[name] = {"genre": genre, "release_date": year, 'producer': producer}
    
for k, v in game_dict.items():
  print(k, v)
  
print(game_dict["Fifa14"]["genre"])
```

## Question 6 - Sorting Dictionary

```python
def sort_dict(d):
	return sorted(d.items(), key=lambda x: x[1], reverse=True)
 
print(sort_dict({3:1, 2:2, 1:3}))
```

## Question 7 - Word Frequency

```python
mylist = str(input()).split()
mydict = {}

for i in mylist:
    mydict[i] = 1 if mydict.get(i) is None else mydict[i] + 1
for i in sorted(mydict, key=mydict.get, reverse=True):
    print(i, end = " ")
```

Alternative:

```python
words = input().strip().split()
word_count = {}

for word in words:
    word_count[word] = 1 if word not in word_count else word_count[word] + 1
for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
    print(k, end = " ")
```

## Question 8 - Anagrams

```python
word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]

def freq(word):
    freq_dict = {}
    for char in word:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

anagram_list = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (freq(word_1) == freq(word_2)):
            anagram_list.append(word_1)
print(anagram_list)
```

## Question 9 - Vasya - Clerk

```python
def tickets(people):
    change = {25: 0, 50: 0, 100: 0}
    for money in people:
        if money == 25: 
            change[25] += 1
        elif money == 50: 
            change[25] -= 1
            change[50] += 1
        elif money == 100 and change[50] > 0:
            change[25] -= 1
            change[50] -= 1
        elif money==100 and change[50] == 0:
            change[25] -= 3

        if change[25] < 0 or change[50] < 0:
            return 'NO'
    return 'YES'

print(tickets([25, 25, 50])) # => YES
print(tickets([25, 100])) # => NO. Vasya will not have enough money to give change to 100 dollars
print(tickets([25, 25, 50, 50, 100])) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
```
