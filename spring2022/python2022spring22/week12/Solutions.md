## Question 1 - Distinctness
```python
def is_distinct(string):
    print(set(string))
    return len(set(string)) == len(string)

print(is_distinct('slay'))
```

## Question 2 - Seperating the Types
```python
the_list= ["music",13,True, "black", (26,1),"16", "False","pencil"]
the_dictionary= {}

for item in the_list:
    if type(item) not in the_dictionary:
        the_dictionary[type(item)]=[item]
    else:
        the_dictionary[type(item)].append(item)

for item_type, item_list in the_dictionary.items():
    print(item_type, '->',item_list)

```

## Question 3 - imdB
```python
lines = []
line = str(input())
while line != "exit":
    lines.append(line)
    line = str(input())

my_dict = {}
for line in lines:
    line = line.split(",")
    info = {'genre' : line[1], 'release_date': line[2], 'director':line[3]}
    my_dict[line[0]] = info
print(my_dict)
```

## Question 4 - String Who Should Not Be Written
```python
the_tuple=("TOM MARVOLO RIDDLE","I AM LORD VOLDEMORT")

def freq(word):
    freq_dict = {}
    for char in word:
        if char != (" ") :
            freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

if (freq(the_tuple[0])) == (freq(the_tuple[1])):
    print ("Anagram")
else:
    print("Not an anagram")
``` 

## Question 5 - Cooking Oil Lines
``` python
def cashier(people):
    change = {50: 0, 100: 0, 200: 0}
    for money in people:
        if money == 50:
            change[50] += 1
        elif money == 100:
            change[50] -= 1
            change[100] += 1
        elif money == 200 and change[100] > 0:
            change[50] -= 1
            change[100] -= 1
        elif money==200 and change[100] == 0:
            change[50] -= 3

        if change[100] < 0 or change[50] < 0:
            return 'NO'
    return 'YES'

print(cashier([50, 50, 100]))
print(cashier([50, 200]))
print(cashier([50, 50, 100, 100, 200]))
```
