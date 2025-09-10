
# 8. Modifying Content in Place:
# Write a function that takes a file path, a target word, and a replacement word as input.
# The function should replace all occurrences of the target word with the replacement word in the file.
# Ensure that the original file is modified and saved with the new content.

def replacing_word(file_path, target_word, replacement_word):
    with open(file_path, 'r') as file_handle:
        contents = file_handle.read()

    new_content = contents.replace(target_word, replacement_word)

    with open(file_path, 'w') as file_handle:
        file_handle.write(new_content)


replacing_word('new_file', 'for', 'four')
