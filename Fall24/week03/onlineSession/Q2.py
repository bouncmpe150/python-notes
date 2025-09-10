
# 2. Appending Text to a File:
# Write a function that takes two arguments: a file path and a string of text.
# The function should append the provided text to the end of the file without erasing the existing content.

def append_text(file_path, text):
    with open(file_path, 'a') as file_handle:
        file_handle.write(text)


txt = "\n\n# 2. Appending Text to a File: Write a function that takes two arguments: a file path and a string of text. " \
      "The function should append the provided text to the end of the file without erasing the existing content."


inp = input()
append_text(inp, txt)
