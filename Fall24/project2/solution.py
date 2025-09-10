## Solution for Question 1

def best_cities_to_visit(city_data, places_dict, budget):
    # Filter cities within the budget
    affordable_cities = {city: data for city, data in city_data.items() if data[0] <= budget}

    # Check if there are any affordable cities
    if not affordable_cities:
        print("No cities within your budget.")
        return None, None

    # Define explicit key functions
    def economical_key(city):
        return affordable_cities[city][0]

    def distance_key(city):
        return affordable_cities[city][1]

    # Find the most economical city and the closest city in terms of distance
    best_economical_city = min(affordable_cities, key=economical_key)
    best_distance_city = min(affordable_cities, key=distance_key)

    # Display the results
    print(
        f"\nMost economical city within budget: {best_economical_city} - Cost: {affordable_cities[best_economical_city][0]} dollars")
    print(f"Closest city within budget: {best_distance_city} - Distance: {affordable_cities[best_distance_city][1]} km")

    return best_economical_city, best_distance_city

def citys_liked_to_go():
    list_cities = []
    city_num = int(input("How many cities would you like to travel? "))
    print("Can you tell me the names of these cities?")
    for i in range(city_num):
        city_name = input()
        list_cities.append(city_name)

    # Collect city data
    city_data = {}  # {city_name: (price, distance)}
    for city in list_cities:
        budget_for_city = int(input(f"How much dollars for {city}? "))
        distance = int(input(f"How far is {city} in kilometers? "))
        city_data[city] = (budget_for_city, distance)

    budget_total = int(input("What's your budget for this trip? "))

    return city_data, budget_total


def collect_places_to_visit(city_data):
    places_dict = {}  # {city_name: [places_to_visit]}
    for city in city_data:
        places_to_visit = []
        print(f"Add places to visit in {city}. Type 'q' to finish.")
        while True:
            place = input("Place to visit: ")
            if place == 'q':
                break
            places_to_visit.append(place)
        places_dict[city] = places_to_visit
    return places_dict


def save_data_to_file(city_data, places_dict, filename="travel_data.txt"):
    with open(filename, "w") as file:
        # Write city data (price and distance)
        for city, (price, distance) in city_data.items():
            file.write(f"{city}: {price}, {distance}\n")

        # Write places data
        file.write("\nPlaces to visit:\n")
        for city, places in places_dict.items():
            file.write(f"{city}:\n")
            for place in places:
                file.write(f" - {place}\n")
            file.write("\n")
    print(f"Data has been saved to {filename}")


def load_data_from_file(filename="travel_data.txt"):
    city_data = {}
    places_dict = {}
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Parsing city data (price and distance)
        section = "city_data"
        for line in lines:
            line = line.strip()
            if line == "Places to visit:":
                section = "places"
                continue

            if section == "city_data" and line:
                city, rest = line.split(": ")
                price, distance = map(int, rest.split(", "))
                city_data[city] = (price, distance)

            elif section == "places" and line:
                if line.endswith(":"):
                    current_city = line[:-1]
                    places_dict[current_city] = []
                else:
                    places_dict[current_city].append(line.strip(" - "))

        print("Data loaded successfully.")
        return city_data, places_dict

    except FileNotFoundError:
        print("File not found. Starting with empty data.")
        return {}, {}


def main():
    # Step 1: Collect city data and user budget
    city_data, budget_total = citys_liked_to_go()

    # Step 2: Collect places to visit for each city
    places_dict = collect_places_to_visit(city_data)

    # Step 3: Save data to file
    save_data_to_file(city_data, places_dict)

    # Step 4: Load data from file
    loaded_city_data, loaded_places_dict = load_data_from_file()

    # Step 5: Find best cities to visit based on budget
    best_economical_city, best_distance_city = best_cities_to_visit(loaded_city_data, loaded_places_dict, budget_total)

    # Step 6: Display best city options
    if best_economical_city:
        print("\nSummary of the best cities based on your budget:")
        print(f"- Most economical city: {best_economical_city}")
        print(f"- Closest city: {best_distance_city}")


# Run the program
main()



## Solution for Question 2

import turtle
import random

# Set up the screen and the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Random Nested Shapes")
pen = turtle.Turtle()
pen.speed(5)

# Define minimum size threshold for each shape
MIN_SIZE = 5  # Minimum size threshold for stopping recursion

# Function to reset turtle for a new shape and ensure clear centering
def reset_turtle():
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)  # Reset orientation
    pen.pendown()

# Function to draw nested circles recursively with constant decrement
def draw_nested_circles(radius, decrement):
    if radius <= MIN_SIZE:  # Stop if radius is too small
        return
    reset_turtle()
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)
    draw_nested_circles(radius - decrement, decrement)  # Recursive call with constant decrement

# Function to draw nested squares recursively with constant decrement
def draw_nested_squares(side, decrement):
    if side <= MIN_SIZE:  # Stop if side length is too small
        return
    reset_turtle()
    pen.penup()
    pen.goto(-side / 2, side / 2)
    pen.pendown()
    for _ in range(4):
        pen.forward(side)
        pen.right(90)
    draw_nested_squares(side - decrement, decrement)  # Recursive call with constant decrement

# Function to draw nested stars recursively with constant decrement
def draw_nested_stars(size, decrement):
    if size <= MIN_SIZE:  # Stop if size is too small
        return
    reset_turtle()
    pen.penup()
    pen.goto(-size / 2, size / 4)
    pen.pendown()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    draw_nested_stars(size - decrement, decrement)  # Recursive call with constant decrement

# Function to draw nested triangles recursively with constant decrement
def draw_nested_triangles(side, decrement):
    if side <= MIN_SIZE:  # Stop if side length is too small
        return
    reset_turtle()
    pen.penup()
    pen.goto(-side / 2, -side / (2 * 3**0.5))
    pen.pendown()
    for _ in range(3):
        pen.forward(side)
        pen.left(120)
    draw_nested_triangles(side - decrement, decrement)  # Recursive call with constant decrement

# Function to draw nested rectangles recursively with constant decrement
def draw_nested_rectangles(width, height, width_decrement, height_decrement):
    if width <= MIN_SIZE or height <= MIN_SIZE:  # Stop if dimensions are too small
        return
    reset_turtle()
    pen.penup()
    pen.goto(-width / 2, height / 2)
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    draw_nested_rectangles(width - width_decrement, height - height_decrement, width_decrement, height_decrement)

# List of shapes and random selection
shapes = ["circle", "square", "star", "triangle", "rectangle"]
shape = random.choice(shapes)
print(f"Randomly selected shape: {shape}")

# User input for initial size and fixed decrement size
initial_size = int(input("Enter the initial size of the shape (e.g., 100): "))
decrement = int(input("Enter the constant decrement for nesting (e.g., 10): "))


# Draw the randomly selected shape with specified parameters
if shape == "circle":
    draw_nested_circles(initial_size, decrement)
elif shape == "square":
    draw_nested_squares(initial_size, decrement)
elif shape == "star":
    draw_nested_stars(initial_size, decrement)
elif shape == "triangle":
    draw_nested_triangles(initial_size, decrement)
elif shape == "rectangle":
    # Rectangles use separate decrements for width and height
    draw_nested_rectangles(initial_size, initial_size // 2, decrement, decrement / 2)
else:
    print("Invalid shape selection!")

# Keep the window open after drawing is complete
turtle.done()



## Solution for Question 3

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
    board.append([int(x) for x in input().split(" ")])

print_board()

def explode(x,y):

    blast = board[y][x]

    if blast <= 0:
        return

    board[y][x] = 0

    print_board()

    start_y = y - blast
    end_y = y + blast

    if start_y < 0:
        start_y = 0
    if end_y >= height:
        end_y = height-1

    start_x = x - blast
    end_x = x + blast

    if start_x < 0:
        start_x = 0
    if end_x >= width:
        end_x = width - 1

    for y_ in range(start_y, end_y +1):
        for x_ in range(start_x, end_x +1):
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

