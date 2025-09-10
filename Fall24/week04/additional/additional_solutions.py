### Question 1: Find the largest number from a file and categorize it

file_name = input()

# Assume the file contains a list of floating-point numbers, one on each line.
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# Open the file and read its content
with open(file_name, 'r') as f:
    numbers = [float(line.strip()) for line in f]

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
# Find the largest number
largest = max(numbers)

print("Largest number: %.2f" % largest)

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def categorize_number(number):
    if number > 100:
        return "High"
    elif 50 <= number <= 100:
        return "Medium"
    else:
        return "Low"

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
category = categorize_number(largest)
print("Category of the largest number: " + category)


### Question 2: Temperature conversion program with error handling and file I/O

input_file = input()

# Assume the file contains temperatures in Celsius on each line.
# Read the temperatures and convert them to Fahrenheit.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

with open(input_file, 'r') as file:
    temperatures = [float(line.strip()) for line in file]

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def categorize_temperature(fahrenheit):
    if fahrenheit < 32:
        return "Freezing"
    elif 32 <= fahrenheit < 68:
        return "Cold"
    elif 68 <= fahrenheit < 85:
        return "Warm"
    else:
        return "Hot"

# Calculate Fahrenheit and categorize the temperatures
for temp in temperatures:
    fahrenheit = celsius_to_fahrenheit(temp)
    category = categorize_temperature(fahrenheit)
    print("Celsius: %.2f, Fahrenheit: %.2f, Category: %s" % (temp, fahrenheit, category))



### Question 3: Recursive Directory Size Calculation with Conditional Output

import os

# Function to recursively calculate the total size of files
def calculate_directory_size(directory):
    # Base case: if the directory is empty
    if not os.path.isdir(directory):
        return 0

    # List all entries in the directory
    entries = os.listdir(directory)
    
    # Helper function to accumulate the size recursively
    def get_size(entries, index=0):
        # Base case for recursion
        if index >= len(entries):
            return 0
        
        entry = entries[index]
        path = os.path.join(directory, entry)

        # Calculate size based on whether it's a file or a directory
        if os.path.isfile(path):
            size = os.path.getsize(path)
        elif os.path.isdir(path):
            size = calculate_directory_size(path)
        else:
            size = 0

        # Recursive call to get the size of the next entry
        return size + get_size(entries, index + 1)

    # Start recursion with the entries
    return get_size(entries)

def write_directory_size(directory, threshold):
    total_size = calculate_directory_size(directory)
    
    # Convert size to MB
    total_size_mb = total_size / (1024 * 1024)
    
    with open("directory_size.txt", "w") as f:
        f.write(f"Total directory size: {total_size_mb:.2f} MB\n")
        
        # If size exceeds threshold, write a warning message
        if total_size_mb > threshold:
            f.write(f"Warning: Directory size exceeds {threshold} MB\n")

# Input: Directory path and size threshold
directory_path = input("Enter the directory path: ")
size_threshold = float(input("Enter the size threshold in MB: "))

# Calculate and write the directory size
write_directory_size(directory_path, size_threshold)


### Question 4: Recursive Binary Search with File Input/Output

# Function to perform recursive binary search
def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1  # Base case: target not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid  # Found the target, return index (0-based)
    
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)  # Search in the right half
    
    else:
        return recursive_binary_search(arr, target, low, mid - 1)  # Search in the left half

# Read sorted list and target number from a file
input_file = input("Enter the input file name: ")

with open(input_file, 'r') as f:
    # Read the sorted list from the file
    numbers = list(map(int, f.readline().strip().split(',')))
    
    # Read the target number
    target = int(f.readline().strip().split(':')[-1].strip())

# Perform binary search
result_index = recursive_binary_search(numbers, target, 0, len(numbers) - 1)

# Write the result to an output file
output_file = "binary_search_output.txt"

with open(output_file, 'w') as f:
    if result_index == -1:
        f.write(f"Number {target} not found\n")
    else:
        f.write(f"Number {target} found at position {result_index + 1}\n")  # Convert to 1-based index
