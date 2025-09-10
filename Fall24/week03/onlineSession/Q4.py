
# 4. Counting Occurrences of a Word in a File:
# Write a function that takes a file path and a word as input.
# The function should return how many times the given word appears in the file.
# Write a function to save the result to an output file.

def frequency_of_word(input_file, word, output_file):
    with open(input_file, 'r') as read_file:
        content = read_file.read()

    count = content.count(word)

    with open(output_file, 'w') as write_file:
        write_file.write(f"The word {word} appears {count} times in this file.")

    return count


frequency_of_word('new_file', 'for', 'frequency')


