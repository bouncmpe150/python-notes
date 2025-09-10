# Sets

## Question 1 - Set Operations

Write a function that takes two sets then prints union, intersection and difference operations between them.

| Input                                       | Output                                                       |
| ------------------------------------------- | ------------------------------------------------------------ |
| A = {1, 2, 3, 4, 5, 6} B = {1, 1, 2, 7, 11} | A ∪ B = {1, 2, 3, 4, 5, 6, 7, 11} A ∩ B = {1, 2} A / B = {3, 4, 5, 6} B / A = {11, 7} |

## Question 2 - Eligible to graduate?

You are given 2 sets one of which is the set of all courses that has to be taken to graduate from CmpE department. Other one is the courses that has been taken by a student so far. Write a function indicating whether student can graduate or not.

| Input                                                        | Output       |
| ------------------------------------------------------------ | ------------ |
| {"CmpE150","CmpE160","CmpE220","CmpE250","CmpE260"} {"Cmpe150"} | Not Eligible |

## Question 3 - How good friends can they be?

People need to have common things to be friends. Let's say we have a set for every person consisting of the ID's of their personality traits. Two people can make as better friendship as the sum of their common personality trait IDs. Write a function that calculates the sum of common personality trait IDs.

| Input                 | Output |
| --------------------- | ------ |
| {1,2,3,4,5} {4,5,6,7} | 9      |

## Question 4 - Distinct

A distinct string is a string whose all characters occurs only once.

Write a function that takes a string as an argument and checks whether given string is distinct or not.

| Input                 | Output |
| --------------------- | ------ |
| dwarf                 | True   |
| violate               | True   |
| violation             | False  | 

# Files

## Question 5 - Reverse Lines

Write a program that prompts for a file name and reverses each line of the file and writes the resulting list of lines to a new file.

| Input File                                                   | Output File                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Eating raw fish didn't sound like a good idea<br />"It's a delicacy in Japan," didn't seem to make it any more appetizing<br />Raw fish is raw fish, delicacy or not | aedi doog a ekil dnuos t'ndid hsif war gnitaE<br/>gniziteppa erom yna ti ekam ot mees t'ndid ",napaJ ni ycaciled a s'tI"<br/>ton ro ycaciled ,hsif war si hsif waR |

## Question 6 - Pluralize

Write a program which takes a file name and reads file that has one word each line. It should pluralize only the words that is made up only letters and will print out the pluralized form of these words in to an output file called pluralWords.txt. If the last letter of a word is 'y', drop 'y' and add 'ies' (cherry to cherries). In other cases add 's' to that word (orange to oranges).
| input.txt                                                    | output.txt                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| lady <br> CMPE150 <br> phone <br> Mr.Nobody <br> area51 <br> 8ship <br> student <br> secretary <br> Dr.ErolBey <br> python_variable <br> Hello! <br> system | ladies <br> phones  <br> students <br> secretaries <br> systems |

## Question 7 - Correct Grades

Write a program which reads the file named `grades.txt` which has Midterm 1 grades on the first line, Midterm 2 grades on the second line and Final grades on the third line. Assume that each line has the same number of grades. Correct the grades such that nonnegative grades will be replaced by 0. Write the resulting grades to `corrected.txt`.

| grades.txt                                                   | corrected.txt                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 70 85 0 -5 20 100 <br> 100 50 45 30 -10 90 <br>-3 50 30 25 60 85 | 70 85 0 0 20 100 <br> 100 50 45 30 0 90 <br> 0 50 30 25 60 85 |

# List Bonus Question

## Question 8 - Bubble Sort

Write a function that sorts elements of the list in ascending order.

| INPUT           | OUTPUT          |
| --------------- | --------------- |
| 4 2 8 6 7 3 1 5 | 1 2 3 4 5 6 7 8 |

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
wrong order.

**Example:**

**First Pass:**

- ( **5** **1** 4 8 2 ) –> ( **1** **5** 4 8 2 ), Here, algorithm compares the first two elements, and swaps since 5 >
  1.
- ( 1 **5** **4** 8 2 ) –> ( 1 **4** **5** 8 2 ), Swap since 5 > 4
- ( 1 4 **5** **8** 2 ) –> ( 1 4 **5** **8** 2 ), since these elements are already in order (8 > 5), no swap.
- ( 1 4 5 **8** **2** ) –> ( 1 4 5 **2** **8** ), Swap since 8 > 2.

The largest element is at the end.

**Second Pass:**

- ( **1** **4** 5 2 8 ) –> ( **1** **4** 5 2 8 )
- ( 1 **4** **5** 2 8 ) –> ( 1 **4** **5** 2 8 )
- ( 1 4 **5** **2** 8 ) –> ( 1 4 **2** **5** 8 ), Swap since 5 > 2
- ( 1 4 2 **5** **8** ) –> ( 1 4 2 **5** **8** )

**Third Pass:**

- ( **1** **4** 2 5 8 ) –> ( **1** **4** 2 5 8 )
- ( 1 **4** **2** 5 8 ) –> ( 1 **2** **4** 5 8 ), Swap since 4 > 2
- ( 1 2 **4** **5** 8 ) –> ( 1 2 **4** **5** 8 )
- ( 1 2 4 **5** **8** ) –> ( 1 2 4 **5** **8** )

Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass
without any swap to know it is sorted.

**Fourth Pass:**

- ( **1** **2** 4 5 8 ) –> ( **1** **2** 4 5 8 )
- ( 1 **2** **4** 5 8 ) –> ( 1 **2** **4** 5 8 )
- ( 1 2 **4** **5** 8 ) –> ( 1 2 **4** **5** 8 )
- ( 1 2 4 **5** **8** ) –> ( 1 2 4 **5** **8** )

