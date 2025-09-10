
# 1. Reading and Writing Simple Text:
# Write a function that receives two file paths: one for reading and another for writing.
# The function should read the contents of the first file and write the exact same content into the second file.

def copy_content(input_file, output_file):
    with open(input_file, 'r') as read_file:
        contents = read_file.read()
    with open(output_file, 'w') as write_file:
        write_file.write(contents)
    return output_file


file1 = input()
file2 = input()
print(copy_content(file1, file2))


