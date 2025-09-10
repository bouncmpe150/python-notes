
# 7. Reading a Specific Line from a File:
# Write a function that takes a file path and an integer line_number as input.
# The function should return the content of the specified line from the file.
# Assume that the first line is numbered 1.

def specific_line(file_path, line_number):
    with open(file_path, 'r') as file_handle:
        lines = file_handle.readlines()
        line = lines[line_number - 1]
    return line


print(specific_line('new_file', 3))
