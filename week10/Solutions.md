# Sets

## Question 1 - Set Operations

```python
A = {1, 2, 3, 4, 5, 6}
B = {1, 1, 2, 7, 11}

def set_operations(set1, set2):
    print("A ∪ B = {}".format(set1.union(set2)))
    print("A ∩ B = {}".format(set1.intersection(set2)))
    print("A / B = {}".format(set1.difference(set2)))
    print("B / A = {}".format(set2.difference(set1)))

set_operations(A, B)
```

## Question 2 - Eligible to graduate?

```python
required = {"CmpE150","CmpE160","CmpE220","CmpE250","CmpE260"}
def is_eligible(current):
    if len(required.intersection(current)) == len(required):
        return "Eligible"
    else:
        return "Not Eligible"
print(is_eligible({"Cmpe150"}))
```

Alternative:

```python
required = {"CmpE150","CmpE160","CmpE220","CmpE250","CmpE260"}
def is_eligible(current):
    if required.intersection(current) == required:
        return "Eligible"
    else:
        return "Not Eligible"
print(is_eligible({"Cmpe150"}))
```

## Question 3 - How good friends can they be?

```python
def overall_traits(traits1, traits2):
    intersection = traits1.intersection(traits2)
    return sum(intersections)
```

## Question 4 - Distinct

```python
def is_distinct(string):
    return len(set(string)) == len(string)

print(is_distinct('violate'))
```

# Files

## Question 5 - Reverse Lines

```python
filename = input()
input_f = open(filename, 'r')
output_f = open('output.txt', 'w')
for line in input_f:
    output_f.write(line[::-1])
input_f.close()
output_f.close()
```

Alternative:

```python
filename = input()

with open(filename, 'r') as input_f:
  lines = input_f.readlines()
  
with open('output.txt', 'w') as output_f:
  for line in lines:
    line = line.strip()
    output_f.write(line[::-1] + "\n")
```

## Question 6 - Pluralize

```python
with open('input.txt','r') as f:
    words = [line.strip() for line in f.readlines()]
    alphas = [word for word in words if word.isalpha()]

with open('output.txt','w') as f:
    f.write("\n".join([word +'s' if word[-1] != 'y' else word[:-1]+'ies' for word in alphas]))
```

Alternative:

```python
input_filename = "q6.txt"
output_filename = "pluralWords.txt"

with open(input_filename, "r") as input_file:
    lines = input_file.readlines()
    words = [line.strip() for line in lines]
    alphas = [word for word in words if word.isalpha()]

with open(output_filename, "w") as output_file:
    for word in alphas:
        if word[-1] == "y":
            plural_word = word[:-1] + "ies"
        else:
            plural_word = word + "s"
        output_file.write(plural_word + "\n")
```

## Question 7 - Correct Grades

```python
with open("grades.txt", 'r') as f:
    mt1 = [str(max(0, int(grade))) for grade in f.readline().split()]
    mt2 = [str(max(0, int(grade))) for grade in f.readline().split()]
    final = [str(max(0, int(grade))) for grade in f.readline().split()]
    
with open("corrected.txt", 'w') as f:
    f.write(' '.join(mt1))
    f.write('\n')
    f.write(' '.join(mt2))
    f.write('\n')
    f.write(' '.join(final))
```

# List Bonus Question

## Question 8 - Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp

    return arr


print(bubble_sort([4, 2, 8, 6, 7, 3, 1, 5]))

#print(sorted([4, 2, 8, 6, 7, 3, 1, 5]))
```


