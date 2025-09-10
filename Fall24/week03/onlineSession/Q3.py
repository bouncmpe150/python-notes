
# 3. Counting Words in a File: Write a function that takes a file path as input.
# The function should open the file, read the content, and return the number of words in the file.

def count_words(file_path):
    with open(file_path) as file_handle:
        content = file_handle.read()
    word_count = len(content.split())
    return word_count


print(count_words('new_file'))

