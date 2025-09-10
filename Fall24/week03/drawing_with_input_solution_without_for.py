# Step 1: Create a file, write to it, and close it
file_name = "circle_log.txt"
with open(file_name, 'w') as f:
    f.write("Starting to draw concentric circles using turtle.\n")

# Step 2: Append more data to the file
with open(file_name, 'a') as f:
    f.write("Drawing concentric circles now.\n")

# Step 3: Draw concentric circles using turtle
import turtle

# Set up the turtle environment
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)  # Set the speed of the turtle

# Draw the first circle (Radius: 50)
pen.circle(50)  # Draw circle with the initial radius of 50
pen.penup()  # Lift the pen
pen.sety(pen.ycor() - 30)  # Move down by gap (30)
pen.pendown()  # Put the pen down

# Draw the second circle (Radius: 80)
pen.circle(80)  # Draw circle with radius increased by 30 (gap)
pen.penup()  # Lift the pen
pen.sety(pen.ycor() - 30)  # Move down by gap (30)
pen.pendown()  # Put the pen down

# Draw the third circle (Radius: 110)
pen.circle(110)  # Draw circle with radius increased by 30 again
pen.penup()  # Lift the pen
pen.sety(pen.ycor() - 30)  # Move down by gap (30)
pen.pendown()  # Put the pen down

# Draw the fourth circle (Radius: 140)
pen.circle(140)  # Draw circle with radius increased by 30 again
pen.penup()  # Lift the pen
pen.sety(pen.ycor() - 30)  # Move down by gap (30)
pen.pendown()  # Put the pen down

# Draw the fifth circle (Radius: 170)
pen.circle(170)  # Draw circle with radius increased by 30 again
pen.penup()  # Lift the pen
pen.sety(pen.ycor() - 30)  # Move down by gap (30)
pen.pendown()  # Put the pen down

# Step 4: Append information about the drawing process
with open(file_name, 'a') as f:
    f.write("Drew 5 concentric circles with a starting radius of 50 and a gap of 30 between them.\n")

# Close the turtle environment on click
screen.exitonclick()
