# Question 1 - Lowercase Conversion
def convert_to_lowercase(string):
    return string.lower()

# Question 2 - Count Specific Character
def count_character(string, char):
    return string.count(char)

# Question 3 - Reverse String
def reverse_string(string):
    return string[::-1]

# Question 4 - Palindrome Check
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

# Question 5 - Substring Finder
def find_substring(main_string, substring):
    return main_string.find(substring)

# Question 6 - Word Counter
def word_count(string):
    return len(string.split())

# Question 7 - Join Strings
def join_strings(strings, delimiter):
    return delimiter.join(strings)

# Question 8 - Replace Substring
def replace_substring(string, old, new):
    return string.replace(old, new)

# Question 9 - Remove Whitespace
def strip_whitespace(string):
    return string.strip()

# Question 10 - Dynamic String Menu
def string_menu():
    while True:
        print("1. Convert to Uppercase")
        print("2. Count a Specific Character")
        print("3. Reverse the String")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            string = input("Enter a string: ")
            print(string.upper())
        elif choice == "2":
            string = input("Enter a string: ")
            char = input("Enter a character: ")
            print(count_character(string, char))
        elif choice == "3":
            string = input("Enter a string: ")
            print(reverse_string(string))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

