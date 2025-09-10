
# 5. Reading Specific Parts of a File:
# Write a function that takes a file path and an integer n as input.
# The function should read the first n characters from the file and return them as a string.

def read_n_chars(file_path, character_count):
    with open(file_path, 'r') as file_handle:
        text = file_handle.read(character_count)
    return text


print(read_n_chars('new_file', 23))
print(read_n_chars('new_file', 100))


