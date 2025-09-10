import turtle


# Function to write the turtle's position to a file
def write_position_to_file(file, message):
    file.write(f"{message}: ({t.xcor()}, {t.ycor()})\n")


# Set up turtle
t = turtle.Turtle()

# Open a file to write the coordinates of the turtle's position
with open("flower_coordinates.txt", "w") as f:
    f.write("Turtle Drawing a Flower - Petal Coordinates:\n")


    # Function to draw one petal and write its position
    def draw_petal():
        write_position_to_file(f, "Start of petal")  # Write starting point of each petal
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(60)  # Position for the next petal
        write_position_to_file(f, "End of petal")  # Write ending point of each petal


    # Draw the flower (6 petals) and write the positions to the file
    draw_petal()  # First petal
    draw_petal()  # Second petal
    draw_petal()  # Third petal
    draw_petal()  # Fourth petal
    draw_petal()  # Fifth petal
    draw_petal()  # Sixth petal

# Open the file again to append additional information
with open("flower_coordinates.txt", "a") as f:
    f.write("\nFlower drawing complete.\n")

# Hide the turtle and finish
t.hideturtle()
turtle.done()
