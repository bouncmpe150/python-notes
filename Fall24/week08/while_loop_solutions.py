# Question 1 - Factorial

def factorial():
    while True:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive number.")
            continue
        result = 1
        i = 1
        while i <= n:
            result *= i
            i += 1
        print(f"Factorial of {n}: {result}")
        
        another = input("Do you want to calculate another factorial? (yes/no): ").lower()
        if another != "yes":
            break

# Question 2 - Sum until Negative

def sum_until_negative():
    total = 0
    count = 0
    while True:
        num = int(input("Enter a number: "))
        if num < 0:
            break
        total += num
        count += 1
    print(f"Sum: {total}")
    print(f"Numbers Entered: {count}")


# Question 3 - Guess the Number

import random

def guess_the_number():
    target = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number: "))
        attempts += 1
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

# Question 4 - Password Check

def password_check():
    correct_password = "python123"
    attempts = 3
    while attempts > 0:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted.")
            return
        else:
            attempts -= 1
            print(f"Wrong password. Attempts left: {attempts}")
    print("Access denied.")

# Question 5 - Remove Elements

def remove_elements(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:  # Check if the element is odd
            lst.pop(i)       # Remove the odd number
        else:
            i += 1           # Move to the next index if the number is even
    print(f"Modified List: {lst}")
    print(f"List now has only even numbers.")

# Call the function directly
remove_elements([1, 2, 3, 4, 5, 6])


# Question 6 - Count Word Frequencies

def count_word_frequencies():
    word_frequencies = {}
    while True:
        word = input("Enter a word (type 'stop' to end): ").strip().lower()
        if word == "stop":
            break
        if word:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

# Example Usage
frequencies = count_word_frequencies()
print("Final Word Frequencies:", frequencies)

# Question 7 - Move until Boundary

import turtle
import random

def move_until_boundary():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(-300, -300, 300, 300)
    
    t = turtle.Turtle()
    while -300 < t.xcor() < 300 and -300 < t.ycor() < 300:
        t.forward(10)
        t.left(random.randint(-90, 90))
    print("Turtle hit the boundary!")

# Question 8 - Number Filter

def number_filter(lst, low, high):
    i = 0
    while i < len(lst):
        if lst[i] < low or lst[i] > high:
            lst.pop(i)
        else:
            i += 1
    print(f"Filtered List: {lst}")


# Question 9 - Find the First Repeated Word

def first_repeated_word(words):
    seen = []  
    i = 0
    while i < len(words):
        if words[i] in seen:  
            print(f"First repeated word: {words[i]}")
            return
        seen.append(words[i])  
        i += 1
    print("No repeated words.")

first_repeated_word(['e', 'e', 'klm', 'klm', 'yu'])

# Question 10 - Dynamic Menu

def dynamic_menu():
    while True:
        print("\nMenu:")
        print("1. Calculate Factorial")
        print("2. Guess the Number")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            factorial()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
