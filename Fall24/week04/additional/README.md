## Question 1: Find the largest number from a file and categorize it

Write a program that reads a list of floating-point numbers from a file (one number per line), finds the largest number, and categorizes it as follows:

If the number is greater than 100, categorize it as "High."
If the number is between 50 and 100 (inclusive), categorize it as "Medium."
If the number is less than 50, categorize it as "Low."

The program should:

Take the file name as input.
Print the largest number and its category.

<br>

## Question 2: Temperature conversion program with error handling and file I/O

Write a program that reads temperatures in Celsius from a file (one temperature per line), converts each temperature to Fahrenheit, and categorizes them as follows:

If the temperature is below 32°F, categorize it as "Freezing."
If the temperature is between 32°F and 68°F, categorize it as "Cold."
If the temperature is between 68°F and 85°F, categorize it as "Warm."
If the temperature is above 85°F, categorize it as "Hot."

The program should:

Take the file name as input.
For each temperature, print its Celsius value, the corresponding Fahrenheit value, and the category.

<br>

## Question 3: Recursive Directory Size Calculation with Conditional Output

Write a program that recursively calculates the total size of all files in a directory and its subdirectories. If the total size exceeds a certain threshold (e.g., 100 MB), print a warning message to the console. Use recursion to explore subdirectories and sum the sizes of all files.

The program should:

Take a directory path as input.
Recursively calculate the total size.
If the size exceeds the threshold, print a warning.
Write the total size to a file, "directory_size.txt".

<br>

## Question 4: Recursive Binary Search with File Input/Output

Write a program that performs a binary search using recursion on a sorted list of numbers from an input file. The program should:

Read the sorted list of numbers from the file.
Read a target number to search for.
Use a recursive binary search function to find the number.
Write whether the number was found in an output file, along with its position.

Input file:
1, 3, 5, 7, 9, 11, 13, 15
Target: 7

Output file:
Number 7 was found at position 4



