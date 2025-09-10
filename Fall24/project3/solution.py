## Solution for Question 1

import random
import os

# Initialize the recommendations dictionary
recommendations = {"Movies": {}, "Books": {}}

# File to store invalid options
INVALID_OPTIONS_FILE = "invalid_options.txt"


def load_invalid_options():
    """Load invalid options from a file."""
    if os.path.exists(INVALID_OPTIONS_FILE):
        with open(INVALID_OPTIONS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_invalid_option(option):
    """Save an invalid option to a file."""
    with open(INVALID_OPTIONS_FILE, "a") as file:
        file.write(f"{option}\n")


def load_recommendations():
    """Load recommendations from a file."""
    if os.path.exists("recommendations.txt"):
        with open("recommendations.txt", "r") as file:
            for line in file:
                type_, category, title = line.strip().split(" | ")
                if category not in recommendations[type_]:
                    recommendations[type_][category] = []
                recommendations[type_][category].append(title)
        print("Recommendations loaded successfully.")
    else:
        print("No saved recommendations found.")


def save_recommendations():
    """Save recommendations to a file."""
    with open("recommendations.txt", "w") as file:
        for type_, categories in recommendations.items():
            for category, titles in categories.items():
                for title in titles:
                    file.write(f"{type_} | {category} | {title}\n")


def add_recommendation():
    """Add a new recommendation."""
    type_ = input("Type (Movie/Book): ").strip().lower()  # Normalize input
    if type_ == "movie":
        type_ = "Movies"  # Match the dictionary key
    elif type_ == "book":
        type_ = "Books"  # Match the dictionary key
    else:
        print("Invalid type! Please choose 'Movie' or 'Book'.")
        return

    title = input("Enter the title: ").title()
    category = input("Enter the category: ").title()
    recommendations[type_].setdefault(category, []).append(title)
    print(f"'{title}' added to '{type_}' under category '{category}'.")


def update_or_delete():
    """Update or delete a recommendation."""
    type_ = input("Type (Movie/Book): ").capitalize()
    if type_ in recommendations:
        if not any(recommendations[type_].values()):
            print(f"No recommendations found in {type_}.")
            return
        print("\nCurrent Recommendations:")
        for category, titles in recommendations[type_].items():
            for title in titles:
                print(f"{title} ({category})")
        action = input("Update or Delete: ").lower()
        old_title = input("Enter the title to modify: ").title()
        for category, titles in recommendations[type_].items():
            if old_title in titles:
                if action == "update":
                    new_title = input("Enter the new title: ").title()
                    titles[titles.index(old_title)] = new_title
                    print(f"'{old_title}' updated to '{new_title}'.")
                elif action == "delete":
                    titles.remove(old_title)
                    print(f"'{old_title}' deleted.")
                return
        print(f"'{old_title}' not found.")
    else:
        print("Invalid type!")


def random_recommendation():
    """Provide a random recommendation."""
    # Ensure there are recommendations available
    available_types = [type_ for type_, categories in recommendations.items() if any(categories.values())]
    if not available_types:
        print("No recommendations available to pick from.")
        return
    type_ = random.choice(available_types)
    category = random.choice(list(recommendations[type_].keys()))
    title = random.choice(recommendations[type_][category])
    print(f"Random Recommendation: '{title}' (Category: {category}, Type: {type_})")


def display_recommendations():
    """Display all recommendations."""
    for type_, categories in recommendations.items():
        print(f"\n--- {type_} ---")
        if not categories:
            print("No recommendations available.")
        for category, titles in categories.items():
            print(f"{category}: {', '.join(titles)}")


# Main program
invalid_options = load_invalid_options()
if invalid_options:
    print("\nPreviously invalid options:")
    for option in invalid_options:
        print(f"- {option}")

load_recommendations()

while True:
    print("\n--- Recommendation System ---")
    print("1. Add Recommendation")
    print("2. Update/Delete Recommendation")
    print("3. Random Recommendation")
    print("4. Display Recommendations")
    print("5. Exit")

    option = input("Choose an option: ")
    if option == "1":
        add_recommendation()
    elif option == "2":
        update_or_delete()
    elif option == "3":
        random_recommendation()
    elif option == "4":
        display_recommendations()
    elif option == "5":
        save_recommendations()
        print("Recommendations saved. Goodbye!")
        break
    else:
        print("Invalid option.")
        save_invalid_option(option)



## Solution for Question 2


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def print_board():
    for y in range(height):
        for x in range(width):
            print(str(board[y][x])+" ",end='')
        print()
    print("-"*(width*2-1))


height = int(input())
width = int(input())

board = []

for _ in range(height):
    board.append(input().split(" "))

print_board()

def explode(x,y):

    symbol = board[y][x]

    if symbol == " ":
        return

    board[y][x] = " "

    print_board()

    start_y = y - 1
    end_y = y + 1

    if start_y < 0:
        start_y = 0
    if end_y >= height:
        end_y = height-1

    start_x = x - 1
    end_x = x + 1

    if start_x < 0:
        start_x = 0
    if end_x >= width:
        end_x = width - 1

    for y_ in range(start_y, end_y +1):
        for x_ in range(start_x, end_x +1):
            if(board[y_][x_] == symbol):
                explode(x_, y_)

command = input()

while command.upper() != "END":
    x, y = [int(_) for _ in command.split(",")]

    if x >= width or x < 0 or y >= height or y <0:
        print("INVALID COMMAND:",command)
        command = input()
        continue
    explode(x,y)
    command = input()


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE