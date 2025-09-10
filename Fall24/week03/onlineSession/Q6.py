
# 6. Reversing File Content:
# Write a function that takes two file paths as input.
# The function should read the first line of the first file, reverse the order of all characters,
# and write the reversed content into the second file.

def reverse_file(file_in, file_out):
    with open(file_in, 'r') as file_read:
        line = file_read.readline()

    reverse_line = ''.join(reversed(line))

    with open(file_out, 'w') as file_written:
        file_written.write(reverse_line)


reverse_file('new_file', 'reversed_file')