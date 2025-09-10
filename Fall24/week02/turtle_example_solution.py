import turtle  # Import the turtle graphics module for drawing shapes
import time    # Import the time module for sleep functionality

# Global variable to track mouse clicks
clicked = False

# Function to handle mouse click events
def on_click(x, y):
    global clicked  # Use the global variable
    clicked = True  # Set clicked to True when the screen is clicked

# Bind the on_click function to mouse click events on the screen
turtle.onscreenclick(on_click)

# Function to wait for a click before proceeding
def waitonclick():
    global clicked  # Use the global variable
    turtle.update()  # Update the turtle screen
    clicked = False  # Reset clicked to False
    # Loop until the user clicks the screen
    while not clicked:
        turtle.update()  # Keep updating the screen
        time.sleep(0.1)  # Pause for a short time to reduce CPU usage
    clicked = False  # Reset clicked for the next wait
    turtle.clear()  # Clear the drawing
    turtle.penup()  # Lift the pen so no lines are drawn
    turtle.goto(0, 0)  # Move the turtle to the center of the screen
    turtle.setheading(0)  # Reset the turtle's orientation to face right
    turtle.pendown()  # Lower the pen to start drawing again

turtle.update()  # Ensure the turtle screen is updated before starting
turtle.speed("slowest")  # Set the turtle speed to the fastest for quick drawing
turtle.pensize(5)  # Set the pen size to 5 pixels

size = 300  # Define the size for the shapes

# Position the turtle to start drawing the star
turtle.penup()  # Lift the pen to avoid drawing while moving
turtle.backward(size / 2)  # Move the turtle backward to center the star
turtle.pendown()  # Lower the pen to start drawing

# Function to draw a star of a given color
def star(color):
    turtle.pencolor(color)  # Set the pen color
    # Draw the star by moving forward and turning right
    turtle.forward(size)  # Move forward by the star size
    turtle.right(144)  # Turn right by 144 degrees to form the star angle

# Draw stars in different colors
star("red")    # Draw the first star in red
star("blue")   # Draw the second star in blue
star("yellow") # Draw the third star in yellow
star("green")  # Draw the fourth star in green
star("orange") # Draw the fifth star in orange

# Wait for a click before proceeding to the next shape
waitonclick()

# Position the turtle to start drawing the hexagon
turtle.penup()  # Lift the pen to avoid drawing while moving
turtle.goto(-size / 2, -size)  # Move to a new position for the hexagon
turtle.pendown()  # Lower the pen to start drawing

# Function to draw a hexagon side of a given color
def hex(color):
    turtle.pencolor(color)  # Set the pen color
    turtle.forward(size)  # Move forward by the hexagon side size
    turtle.left(60)  # Turn left by 60 degrees to form the hexagon angle

# Draw hexagon sides in different colors
hex("red")     # Draw the first side in red
hex("blue")    # Draw the second side in blue
hex("yellow")  # Draw the third side in yellow
hex("green")   # Draw the fourth side in green
hex("orange")  # Draw the fifth side in orange
hex("navy")    # Draw the sixth side in navy

# Wait for a click before proceeding to the next shape
waitonclick()

# Function to draw a side of the spiral
def spiral_side(size, color):
    turtle.pencolor(color)  # Set the pen color
    turtle.forward(size)  # Move forward by the specified size
    turtle.left(90)  # Turn left by 90 degrees to form the spiral angle

# Function to draw a spiral shape with decreasing sizes
def spiral(size, spacing):
    spiral_side(size, "red")  # Draw the first side in red
    spiral_side(size, "blue")  # Draw the second side in blue
    spiral_side(size - spacing, "yellow")  # Draw the third side in yellow with reduced size
    spiral_side(size - spacing, "green")  # Draw the fourth side in green with reduced size

# Position the turtle to start drawing the spiral
turtle.penup()  # Lift the pen to avoid drawing while moving
turtle.goto(-size / 2, -size / 2)  # Move to a new position for the spiral
turtle.pendown()  # Lower the pen to start drawing

spacing = size / 10  # Define the spacing for the spiral

# Draw multiple spirals with decreasing sizes
spiral(size, spacing)  # Draw the first spiral
size -= 2 * spacing  # Decrease size for the next spiral
spiral(size, spacing)  # Draw the second spiral
size -= 2 * spacing  # Decrease size for the next spiral
spiral(size, spacing)  # Draw the third spiral
size -= 2 * spacing  # Decrease size for the next spiral
spiral(size, spacing)  # Draw the fourth spiral

# Final size adjustment and drawing
size -= 2 * spacing  # Adjust size for the last line
turtle.pencolor("red")  # Set the pen color to red
turtle.forward(size)  # Draw the last line of the spiral

# Wait for a click before proceeding to the next shape
waitonclick()

# Draw the Olympic rings
radius = 100  # Define the radius for the rings
spacing = 2 * radius + radius / 5  # Calculate the spacing between the rings

# Position the turtle to start drawing the Olympic rings
turtle.penup()  # Lift the pen to avoid drawing while moving
turtle.backward(spacing)  # Move backward to position the first ring
turtle.pendown()  # Lower the pen to start drawing

# Function to draw an Olympic ring of a given color
def draw_olimpia_ring(color):
    turtle.pencolor(color)  # Set the pen color
    turtle.circle(radius)  # Draw a circle with the defined radius

# Function to move to the next Olympic ring position
def move_to_next_olimpia_ring():
    turtle.penup()  # Lift the pen to avoid drawing while moving
    turtle.forward(spacing)  # Move forward to the next ring position
    turtle.pendown()  # Lower the pen to start drawing

# Draw Olympic rings in different colors
draw_olimpia_ring("blue")  # Draw the first ring in blue
move_to_next_olimpia_ring()  # Move to the next position
draw_olimpia_ring("black")  # Draw the second ring in black
move_to_next_olimpia_ring()  # Move to the next position
draw_olimpia_ring("red")  # Draw the third ring in red

# Position for the bottom row of Olympic rings
turtle.penup()  # Lift the pen to avoid drawing while moving
turtle.backward(2 * spacing)  # Move backward to center the last two rings
turtle.right(90)  # Turn right to face downward
turtle.forward(radius)  # Move down by the radius to position the rings
turtle.left(90)  # Reset orientation to face right
turtle.forward(spacing / 2)  # Move forward to the correct position
turtle.pendown()  # Lower the pen to start drawing

# Draw the bottom row of Olympic rings
draw_olimpia_ring("yellow")  # Draw the first bottom ring in yellow
move_to_next_olimpia_ring()  # Move to the next position
draw_olimpia_ring("green")  # Draw the second bottom ring in green

# Wait for a click before proceeding to the next shape
waitonclick()

# Draw a chain of rings shape
turtle.pencolor("purple")  # Set the pen color to purple
turtle.circle(radius)  # Draw the first ring
turtle.left(60)  # Turn left to prepare for the next ring
turtle.pencolor("green")  # Change the pen color to green
turtle.circle(radius)  # Draw the second ring
turtle.left(60)  # Turn left to prepare for the next ring
turtle.pencolor("blue")  # Change the pen color to blue
turtle.circle(radius)  # Draw the third ring
turtle.left(60)  # Turn left to prepare for the next ring
turtle.pencolor("yellow")  # Change the pen color to yellow
turtle.circle(radius)  # Draw the fourth ring
turtle.left(60)  # Turn left to prepare for the next ring
turtle.pencolor("red")  # Change the pen color to red
turtle.circle(radius)  # Draw the fifth ring
turtle.left(60)  # Turn left to prepare for the next ring
turtle.pencolor("black")  # Change the pen color to black
turtle.circle(radius)  # Draw the sixth ring

# Hide the turtle cursor after all shapes are drawn
turtle.hideturtle()

# Finalize the turtle graphics
turtle.done()  # Keep the turtle graphics window open until it is closed by the user
