## Question 1
```python
list=["pasta",14, False, "True", 3.5,"makarna",(3,8),12]

for item in list:
    if type(item)==str or type(item)==int:
        print (item, end=" ")
```

## Question 2
```python
the_list=["horse","chicken","pig","lamb","cow","ox","rooster"]

if len(the_list)>= 5 and len(the_list)%2!=0:
    a=len(the_list)
    the_list=the_list[0:int((a-3)/2)]+the_list[-int((a-3)/2):a]
    print(the_list)
else:
    print(the_list)
```

## Question 3
```python
def to_the_left(list,N):
    return list[N:] + list[:N]

print(to_the_left(["i","r","r","e","p","l","a","c","a","b","l","e"], 8))
```
## Question 4
``` python
def remove_odd_ones(list):
    return [value for value in list if value%2!= 1]

print(remove_odd_ones([0,12,4,21,53,346,234]))
```
## Question 5
```python
def adding_additions(list):
    new_list=[]
    for i in range(0,len(list)-1):
        addition=list[i]+list[i+1]
        new_list.append(list[i])
        new_list.append(addition)
    new_list.append(list[len(list)-1])

    return new_list

print(adding_additions([1,3,5,7,8]))
```
## Question 6
```python
def create_duplicates(list):
    result = []
    for item in list:
        for i in range(item):
            result.append(item)

    return result


print(create_duplicates([3,2,6,9,3,1]))
```
## Question 7
```python
def popper(list,N):
    list.pop(N-1)
    return list

def remover(list,N):
    Nth_item= list[N-1]
    for item in list:
        if item==Nth_item:
            list.remove(item)

    return list

print(remover(["apples","oranges", "JFK", "potato","tomato"],3))
```
## Question 8
```python
N=str(input())
list_of_strings=[N]

while N != ".":
    N=str(input())
    list_of_strings.append(N)

def reverse_strings(string):
    return " ".join([letter[::-1] for letter in string.split()])

result=[]

for string in list_of_strings:
    string=reverse_strings(string)
    result.append(string)

result.reverse()

def join_strings_as_one(strings):
    return " ".join(string if string!="." else "" for string in strings)

print (join_strings_as_one(result))
``` 
## Question 9
```python
list_of_integers= [1,5,54,312,52,9]
list_of_strings= ["Slytherin","Gryffindor", "Ravenclaw","Hufflepuff"]

list_of_integers.sort()
list_of_strings.sort()

print(list_of_integers)
print(list_of_strings)
```
## Question 10
```python
def counter(list):
    the_most_recurring=0
    counter=0

    for item in list:
        a=list.count(item)
        if a>counter:
            the_most_recurring=item
            counter=a

    return the_most_recurring

print(counter([3,2,1,2,2,2,3,1,1,3,2,5,1]))
```
