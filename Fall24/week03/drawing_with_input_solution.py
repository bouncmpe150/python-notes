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

# Function to draw concentric circles
def draw_concentric_circles(pen, start_radius, num_circles, gap):
    for i in range(num_circles):
        pen.circle(start_radius + i * gap)  # Draw a circle
        pen.penup()  # Lift the pen
        pen.sety(pen.ycor() - gap)  # Move the turtle down for next circle
        pen.pendown()  # Put the pen down

'''
# Alternative concentric circles
def draw_concentric_circles(pen, start_radius, num_circles, gap):
    for i in range(num_circles):
        # Move to the center and draw a circle
        pen.penup()  # Lift the pen
        pen.goto(0, -start_radius - i * gap)  # Move to the correct position
        pen.pendown()  # Put the pen down
        pen.circle(start_radius + i * gap)  # Draw a circle
'''

# Draw 5 concentric circles with a starting radius of 50 and a gap of 30 between them
draw_concentric_circles(pen, 50, 5, 30)

# Step 4: Append information about the drawing process
with open(file_name, 'a') as f:
    f.write("Drew 5 concentric circles with a starting radius of 50 and a gap of 30 between them.\n")

# Close the turtle environment on click
screen.exitonclick()
