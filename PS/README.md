### Problem 1:

Mat is a student at Bogazici University, and he needs to find an apartment to rent. Since there are various renting options near Bogazici,
he needs our help to find the best suitable apartment. He has a monthly rent budget, which he cannot exceed.
Although he does not have any specific limits regarding the number of rooms, he would like to have possibly the maximum number of rooms.
Given the number of rooms and monthly rents of N different apartments, determine the fittest apartment for Mat.

When two apartments have the same number of rooms, choose the one with less rent.

**Examples**:

**Explanation for the first input:**

- Mat's monthly rent limit is 1300.
- There are 4 options: 4 rooms with the rent 1400; 3 rooms with the rent 1250; 1 room with the rent 1300; 2 rooms with the rent 1500.
- He cannot rent the first and the last apartments because of his budget.
- Among the remaining two, second option is better since it has more rooms.

**Explanation for the second input:**

- The monthly rent limit is 2000.
- There are 5 options: 4 rooms with the rent 2000; 3 rooms with the rent 1250; 1 room with the rent 1300; 2 rooms with the rent 2000; and 5 rooms with the rent 2300.
- The first four options meet the rent criteria.
- Among them, first option hes the most rooms.

| INPUT                                                                 | OUTPUT                                          |
| --------------------------------------------------------------------- | ----------------------------------------------- |
| 1300<br />4<br />4 1400<br />3 1250<br />1 1300<br />2 1500           | The best option: 3 rooms with 1250 monthly rent |
| 2000<br/>5<br/>4 2000<br />3 1250<br />1 1300<br />2 2000<br />5 2300 | The best option: 4 rooms with 2000 monthly rent |

```python
rent_limit = int(input())
num_of_options = int(input())
best_rooms = 0
best_rent = 0

for i in range(num_of_options):
    lst = input().split()
    num_of_rooms, rent = int(lst[0]), int(lst[1])
    if rent <= rent_limit:
        if num_of_rooms > best_rooms:
            best_rooms = num_of_rooms
            best_rent = rent
        elif num_of_rooms == best_rooms:
            if rent < best_rent:
                best_rent = rent

print("The best option:", best_rooms, "rooms with", best_rent, "monthly rent")

```

### Problem 2:

Ms. Sakura is an old Japanese woman who is eager to learn English. As her online English teacher,
you gave her homework to write some sentences that she has learned this week. However, since she is accustomed to traditional Japanese writing,
she forgets to use the regular left-to-write writing system of English, and types her sentences vertically, from top-to-bottom.
Also, she has a hard time using the computer to write her homework, she sometimes presses buttons that are not letters.
Fortunaltey, she always use "#" character to seperate the words, she never accidentaly types "#".
While reading and grading her homework, you first need to convert it to the horizontal position, then eliminate non-letter characters.
In the end, the number of words she wrote will be her grade. Given a matrix as her homework, calculate her grade.

- The first row consists of two integers, n and m, respectively representing the number of rows and columns in the following matrix.
- Following each n line consists of m characters.

**Examples**:

**Explanation for the first input:**

- Matrix has 6 rows and 7 columns.
- Starting from the top left of the matrix, we need to read from top-to-bottom, and eliminate the characters that are not letters nor "#".
- In the first column that we look (the right-most column), among the characters 'H', 'e', '/', 'l', 'l', 'o' , all except the 3rd are legit.
- In the second column, among the characters '#', 'm', ';', '&', 'y', '#' , all except 3rd and 4th characters are legit.
- Contiuning like this, at the end we will have some data like "Hello#my#sweet#teacherr#I#love#me", and we need to count the number of words after eliminating '#'s.

| INPUT                                                                              | OUTPUT |
| ---------------------------------------------------------------------------------- | ------ |
| 6 7 <br />orets#H<br />vra#wme<br />e#ct(;/<br />#I;)^&l<br />m#h)eyl<br />ele)e#o | 7      |
| 4 3 <br />iam<br />smy<br />#e#<br />S#n                                           | 4      |

```python
lst = input().split()
rows = int(lst[0])
columns = int(lst[1])
text = ""
matrix = []
for i in range(rows):
    row = input()
    row_lst = []
    for char in row:
        row_lst.append(char)
    matrix.append(row_lst)

for e in range(columns-1, -1, -1):
    for i in range(rows):
        c = matrix[i][e]
        if 97 <= ord(c) <= 122 or 65<= ord(c) <= 90 or ord(c) == 35:
            text += c
# print(text)
output = text.split("#")
# print(output)
print(len(output))

```

### Problem 3:

Mr. Thorn comes home tired every day and does not have time to think about what to cook today.
He has a recipe notebook that consists of different recipes that are numbered in ascending order starting from number n to number m, which are given in the input.
On the ith day of the month, Mr. Thorn prefers to cook a recipe with a number that is an exact multiple of i.
Also, he does not cook the same food again. With this information, you need to determine his cooking plan for the second half of December.
For example, for the 15th of December, he can cook the 30th or 105th recipe. If he cooks the 105th recipe, for the 21st of December,  
he can cook the 21st recipe but cannot cook the 105th recipe. For any ith day, if there is not any multiple of i available, print "cannot be determined". With these conditions, determine his cooking plan from 15th to 31st of December.

**Examples**:

**Explanation for the first input:**

- 15's first multiple in the given interval is 105. For 16, it is 112 and for 17 it is 102.
- However, 24's only multiple in the interval is 120 but it is already used as the multiple of 20.
- Therefore, for 24, 'cannot be determined' is added to the cooking plan.

| INPUT         | OUTPUT                                                                                                                                                            |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 101 <br />130 | [105, 112, 102, 108, 114, 120, 126, 110, 115, 'cannot be determined', 125, 104, 'cannot be determined', 'cannot be determined', 116, 'cannot be determined', 124] |
| 71 <br />95   | [75, 80, 85, 72, 76, 'cannot be determined', 84, 88, 92, 'cannot be determined', 'cannot be determined', 78, 81, 'cannot be determined', 87, 90, 93]              |

```python
start = int(input())
end = int(input())
recipes = [i for i in range(start, end+1)]
output = []
for day in range(15, 32):
    isFound = False
    for k in recipes:
        if k % day == 0 and not isFound:
            output.append(k)
            recipes.remove(k)
            isFound = True
    if not isFound:
        output.append("cannot be determined")
print(output)

```

### Problem 4:

Yuki is in a very busy semester at her university and is having a hard time keeping up with homework.
She has many articles and books to read, but the number of pages she can read in a day is limited.
Also if she reads some page from a book one day and finishes it, she cannot start a new book even though she does not exceed her daily limit yet.
Given her limit and number of pages of the books, she needs our help to determine the minimum number of days to finish all of her readings.

**Examples**:

**Explanation for the first input:**

- Yuki's limit is 30 pages per day.
- She can read the book with 50 pages, 60 pages and 35 pages in 2 days; 6 days in total.
- She can read the book with 20 pages, 15 pages and 15 pages in 1 days; 3 days in total.
- She can read the book with 100 pages in 4 days and 210 pages in 7 days; 11 days in total.
- 6 + 3 + 11 = 20.

| INPUT                              | OUTPUT |
| ---------------------------------- | ------ |
| 30 <br />50 60 20 15 100 210 35 15 | 20     |
| 18 <br />20 32 44 54 100 36 10     | 19     |

```python
limit = int(input())
books = input().split()
result = 0
for book in books:
    book = int(book)
    remaining = book % limit
    if remaining != 0:
        result += 1
    result += book // limit

print(result)

```

### Problem 5:

Harun is very smart but a lazy student. He studies computer engineering in Bogazici University. In his CMPE150 course, he had a homework about arrays.
Since he wants to watch Shingeki No Kyojin, he needs your help for the homework. Can you help him to find the longest increasing subarray of the given integer array?
If there are more than one subarray that have the same length, then you need to find the last one.

**Examples**:

| INPUT                           | OUTPUT             |
| ------------------------------- | ------------------ |
| 30 50 60 20 15 100 210 35 15    | 15 100 210         |
| 90 102 18 20 32 44 54 100 36 10 | 18 20 32 44 54 100 |

```python

array = map(int,input().split())

temp = []
result = []
for i in array:
    if len(temp) == 0 or i > temp[-1]:
        temp.append(i)
    else:
        if len(temp) >= len(result):
            result = temp
        temp = [i]
for i in result:
    print(i,end=" ")

```

### Problem 6:

Ahmet Cemil is a prep school student at Bogazici University. Because of that he and his friends are stayed in the Kilyos dormitory. They are planning to go to the Halloween Party next weekend. They are very excited because of their costume preparation. However, there is a problem: party will be end later than the midnight and there is no 59RK to return to Kilyos. Hence, they have to take a taxi to go back. There will be many people that is in the same situation. They need your help to minimize this taxi cost.

There are several groups of friends that need to go back to Kilyos. Each of the group consists of 4, 3 or 1 people.
Taxi drivers accept 4 people at most for each taxi.
None of the friend groups does not want to be return seperated. So you can not assign the people of same group to different taxis.
How many taxis do they need at least?

**Input Format**:
First line contains three integers represent 1, 3 and 4 sized groups amount respectively.

**Examples**:

**Explanation for the first input:**

- 1 taxi for 4 people's group
- 1 taxi for 1 and 3 people's group

| INPUT   | OUTPUT |
| ------- | ------ |
| 1 1 1   | 2      |
| 6 3 9   | 13     |
| 20 8 10 | 21     |

```python

input = input().split()
one = int(input[0])
three = int(input[1])
four = int(input[2])

ans = four + ((one + (three-one)) if one < three else three + ((one-three)//4 if (one-three)%4==0 else (one-three)//4 + 1))
print(ans)

```

### Problem 7:
Ford is taking Linear Algebra course this semester and very interested in rotation matrices. However some of the essential transformations such as clockwise 180-degrees transformation is not linear, therefore it doesn't have a definite rotation matrix. At this point, he wants to simulate such rotations, but he doesn't have the coding skills to do so. Help him automate 180 degrees clockwise rotation. Write a program which reads first an integer <code>N</code> and NxN more integers as elements of a matrix with size NxN.
Then, you must print the 180 degrees clockwise rotated version of the initial matrix on the screen.

| INPUT  | OUTPUT |
| ------ | ------ |
|4 <br> 1 2 3 4 <br>  5 6 7 8 <br> 9 0 1 2 <br> 3 4 5 6  |6 5 4 3 <br> 2 1 0 9 <br>8 7 6 5 <br>4 3 2 1|
| 7 <br> 8 9 0 1 2 3 4 <br>1 2 3 4 5 6 7<br>5 6 7 8 9 0 1<br>2 3 4 5 6 7 8<br>8 9 0 1 2 3 4<br>2 3 4 5 6 7 8<br>5 6 7 8 9 0 1 | 1 0 9 8 7 6 5<br>8 7 6 5 4 3 2<br>4 3 2 1 0 9 8<br>8 7 6 5 4 3 2<br>1 0 9 8 7 6 5<br>7 6 5 4 3 2 1<br>4 3 2 1 0 9 8 |
| 15<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 1<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 2<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 3<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 4<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 5<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 6<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 7<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 8<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 9<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 0<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 1<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 2<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 3<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 4<br>0 0 0 0 0 0 0 0 0 0 0 0 0 1 5 | 5 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>4 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>3 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>2 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>1 1 0 0 0 0 0 0 0 0 0 0 0 0 0<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>9 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>8 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>7 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>6 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>5 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>4 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>3 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>2 0 0 0 0 0 0 0 0 0 0 0 0 0 0<br>1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |

```python
n = int(input())
matrix = []
for row in range(n):
    column = [int(x) for x in input().split()]
    matrix.append(column)

if(n % 2 == 1):  # odd
    for i in range(n//2):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = temp
    for j in range(n//2):
        temp = matrix[n//2][j]
        matrix[n//2][j] = matrix[n//2][n-1-j]
        matrix[n//2][n-1-j] = temp
else:            # even
    for i in range(n//2):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = temp

for row in matrix:
    for el in row:
        print(el, " ", end='')
    print()
```

### Problem 8:

Max wants to make huge profits in the stock market, so he needs to keep track of the stock prices everyday. The stock prices are given in a list as input. Prices[i] indicates the stock price on the ith day. Max wants to make the maximum profit he can by buying the stock on a day and then selling it on another day. You need to help him choose the days he should buy and sell the stock. 
Write a function that takes the list of prices and returns the maximum profit.

| INPUT  | OUTPUT |
| ------ | ------ |
| 7 1 5 3 6 4 | 5 |
| 7 6 4 3 1 | 0 |

```python

def max_profit(prices):

    max_profit = 0
    min_purchase = prices[0]

    for price in prices:
        curr_profit = price - min_purchase
        if curr_profit > max_profit:
            max_profit = curr_profit
        if price < min_purchase:
            min_purchase = price

    return max_profit


prices = list(map(int, input().split()))
print(max_profit(prices))
   
```

### Problem 9:

Today is the big day for the residents of [Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch](https://en.wikipedia.org/wiki/Llanfairpwllgwyngyll). Since no one is able to pronounce the name of this lovely town, except [Liam Dutton](https://www.youtube.com/watch?v=fHxO0UdpoxM) the weatherman, people of the town decided to change its name to a simple number from 1 to 100 so that everyone can pronounce its name easily. The number (name) with the most votes wins the election. In case of a tie, the smallest number (name) wins. Your task is to announce the winner of the election and the number of vote the winner got, to the people of Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.

| INPUT  | OUTPUT |
| ------ | ------ |
| 5 <br> 12 8 4 59 8 | 8 2|
|6 <br> 5 46 100 46 5|5 2|
| 10 <br> 1 2 1 3 1 4 1 5 1 6|   1 5|
| 8 <br> 15 78 100 65 100 48 99 100| 100 3 |

```python
n = int(input())
votes = [int(x) for x in input().split()]

dict_votes = {}
for vote in votes:
    if vote in dict_votes:
        dict_votes[vote] += 1
    else:
        dict_votes[vote] = 1

max_votes = 0
color = 0
for key, value in dict_votes.items():
    if(value > max_votes):
        color = key
        max_votes = value
    elif(value == max_votes and color > key):
        color = key

print(color, max_votes)

```


### Problem 10:

The minions Kevin and Stuart are playing a game called "Minion Game". They are given a string S and they have to make substrings using the letters of the string. Stuart has to make words starting with consonants while Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
You have to print the name of the winner with its score, if no winners print "Draw".

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

![banana](https://user-images.githubusercontent.com/88784379/145871831-b644b71d-fb85-4832-9a86-7bca360dfe45.png)

```python

string = input()

stuart = 0
kevin = 0
vowels = ["A", "E", "O", "I", "U"]
for i in range(len(string)):
    if string[i] in vowels:
        kevin += len(string) - i
    else:
        stuart += len(string) - i

if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")
```

### Problem 11:

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different "order". The "order" of the alphabet is some permutation of lowercase letters.

Given a sequence of "words" written in the alien language, and the "order" of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
 

##### Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"

Output: true

Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


##### Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"

Output: false

Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


##### Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"

Output: false

Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > 
'∅', where '∅' is defined as the blank character which is less than any other character (More info).
 


Constraints:

1 <= words.length <= 100

1 <= words[i].length <= 20

order.length == 26


All characters in words[i] and order are English lowercase letters.

```python
 def isAlienSorted(W, O):
        alpha = {O[i]: i for i in range(len(O))}
        for i in range(1,len(W)):
            a, b = W[i-1], W[i]
            for j in range(len(a)):
                if j == len(b): return False
                achar, bchar = a[j], b[j]
                aix, bix = alpha[achar], alpha[bchar]
                if aix < bix: 
                    break
                if aix > bix: 
                    return False
        return True
```

### Problem 12:

A gene is represented as a string of length n (where n is divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string `gene`. It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of `gene`  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string `gene`, can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string `s` is a subsequence made up of zero or more contiguous characters of `s`.

As an example, consider `gene= ACTGAAAG` . The substring `AA` just before or after `G` can be replaced with `CT` or `TC`. One selection would create `ACTGACTG`.

Write a function named steady_gene that takes a string representing a gene and returns an integer that represents the length of the smallest substring to replace.

Sample Input

```
8  
GAAATAAA
```
Sample Output

```
5
```
Explanation

One optimal solution is to replace `AAATA` with  `TTCCG` resulting in `GTTCCGAA`.
The replaced substring has length 5.


```python
def steady_gene(gene):
    n = len(gene) / 4
    gene_l = ['A', 'C', 'T', 'G']
    count_l = [gene.count(letter) for letter in gene_l]
    minlen = int(sum([n - count for count in count_l if count < n]))
    valid = False
    while valid == False:
        for i in range(len(gene) - minlen):
            selection = gene[i:i + minlen]
            count_select = [selection.count(letter) for letter in gene_l]
            subtract = [count_l[i] - count_select[i] for i in range(len(count_l))]
            valid = all(x <= n for x in subtract)
            if valid == True:
                break
        if valid == False:
            minlen += 1
    return minlen

````

### Problem 13:

A team of researchers working in Antartica has settled in various camps around the continent to observe penguins. Sadly, due to the climate change, the ice is melting, thus camps lose means of transportation to each other.

Currently available ways are provided by sattelites in a dictionary, for example: 

```
ways = { 5: {3, 7, 0, 9}}
```

Means that there is a road from camp 5 to camp 3, 7, 0, and 9.

Alice, a member of this team, loves penguins and wants to see one whenever she desires. She is willing to travel on 2 roads between camps to see penguins in a day. 

Given a map and Alice's location, print the camps where she can go to see the penguins. 

```
map = {
 0: {3},
 1: {9},
 2: {3, 10},
 3: {0, 2, 8, 10},
 4: {6, 10},
 5: {6},
 6: {4, 5, 7, 10},
 7: {6, 9},
 8: {3, 9},
 9: {1, 7, 8},
 10: {2, 3, 4, 6}}
```

For example:

When Alice is at 0, she can go to 3 using a road. 

Then from 3, she can go to 0, 2, 8, 10 using the second road.

Thus {0, 2, 3, 8, 10} is the result.


### Problem 14:

Its a dire security problem to use the same password to every website that one logs into. However, remembering a different password for each website is not convenient. You can try to note them down somewhere but someone can get this notes and mess with your accounts.

After thinking about this problem, your best friend comes with the idea secret algorithm and wants you to implement it since she/he can trust only you.

The idea is that you create your secret algorithm which inputs the name of the website and performs some operations to generate a password.

To do so, you generate a palindrome using the website's name via increasing values of letters one by one. For example you can change d to an e. Note that z cannot be increased.

For illustration:

asd → bsd → csd → dsd, thus asd can get to a palindrome in 4 steps.

After palindromizing the website's name, 'palindrom' + number of steps * 141 can be used as a password.

Google account example:

google → googlg in 2 steps

googlg → googog in 3 steps

googog → goooog in 8 steps

Palindrome is created in 14 steps, 14 * 141 = 1974

Thus, goooog1974 is the password.

Note: you can get number of steps between 2 chars using given function:

```python
def steps(a, b):
  return ord(a) - ord(b)
```

### Problem 15:

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string txt, determine if it is valid. If so, return "YES", otherwise return "NO".

For example, If txt = "abc", the string is valid because the frequencies of characters are all the same. If txt = "abcc", the string is also valid, because we can remove 1 "c" and have one of each character remaining in the string. However, if txt = "abccc", the string is not valid, because removing one character does not result in the same frequency of characters.

Examples:<br>
<br>
is_valid("aabbcd") ➞ "NO"<br>
<br>
// We would need to remove two characters, both c and d  -> aabb or a and b -> abcd, to make it valid.<br>
// We are limited to removing only one character, so it is invalid.<br>
<br>
is_valid("aabbccddeefghi") ➞ "NO"<br>
<br>
// Frequency counts for the letters are as follows:<br>
// {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 1, "g": 1, "h": 1, "i": 1}<br>
// There are two ways to make the valid string:<br>
// Remove 4 characters with a frequency of 1: {f, g, h, i}.<br>
// Remove 5 characters of frequency 2: {a, b, c, d, e}.<br>
// Neither of these is an option.<br>
<br>
is_valid("abcdefghhgfedecba") ➞ "YES"<br>
<br>
// All characters occur twice except for e which occurs 3 times.<br>
// We can delete one instance of e to have a valid string.<br>


### Problem 16:

https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d

#### Some people have been killed!

You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

#### Task

Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

```python
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
```

and also a list of the names of the dead people:

```python
['Lucas', 'Bill']
```

return the name of the one killer, in our case `'James'` because he is the only person that saw both `'Lucas'` and `'Bill'`

### Problem 17:

https://www.codewars.com/kata/52ae6b6623b443d9090002c8

It's Christmas! You had to wait the whole year for this moment. You can already see all the presents under the Christmas tree. But you have to wait for the next morning in order to unwrap them. You really want to know, what's inside those boxes. But as a clever child, you can do your assumptions already.

You know, you were a good child this year. So you may assume, that you'll only get things from your wishlist. You see those presents, you can lift them and you can shake them a bit. Now you can make you assumptions about what you'll get.

  #### Your Task

  You will be given a wishlist, containing all possible items. Each item is in the format: `{name: "toy car", size: "medium", clatters: "a bit", weight: "medium"}`

  You also get a list of presents, you see under the christmas tree, which have the following format each: `{size: "small", clatters: "no", weight: "light"}`

  Your task is to return the names of all wishlisted presents that you might have gotten.

  #### Rules

  - Possible values for `size`: "small", "medium", "large"
  - Possible values for `clatters`: "no", "a bit", "yes"
  - Possible values for `weight`: "light", "medium", "heavy"
  - Don't add any item more than once to the result
  - The order of names in the output doesn't matter
  - It's possible, that multiple items from your wish list have the same attribute values. If they match the attributes of one of the presents, add all of them.

  #### Example

  ```python
  wishlist = [
      {name: "Mini Puzzle", size: "small", clatters: "yes", weight: "light"},
      {name: "Toy Car", size: "medium", clatters: "a bit", weight: "medium"},
      {name: "Card Game", size: "small", clatters: "no", weight: "light"}
  ]
  presents = [
      {size: "medium", clatters: "a bit", weight: "medium"},
      {size: "small", clatters: "yes", weight: "light"}
  ]
  
  guessGifts(wishlist, presents) // must return ["Toy Car", "Mini Puzzle"]
  ```

