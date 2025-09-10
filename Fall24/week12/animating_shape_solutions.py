

### Question 1 - Moving Point Animation
import turtle
import time

def animate_point():
    screen = turtle.Screen()
    screen.tracer(0)  # Disable auto-updating
    screen.setup(width=800, height=600)

    point = turtle.Turtle()
    point.shape("circle")
    point.color("blue")
    point.penup()

    x = -400  # Start at the leftmost position (scaled for screen width)
    while True:
        point.goto(x, 0)  # y-coordinate is constant at the center
        screen.update()
        time.sleep(0.1)
        x += 10  # Increment position
        if x > 400:  # Reset after reaching the rightmost position
            x = -400

animate_point()






### Question 2 - Oscillating Sine Wave

import turtle
import math
import time

def oscillating_wave():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)

    wave = turtle.Turtle()
    wave.speed(0)
    wave.penup()

    frame = 0
    while True:
        wave.clear()
        wave.penup()
        for x in range(-400, 401, 10):  # x-coordinates scaled for screen width
            x_coord = x
            y_coord = 100 * math.sin(math.radians(x + frame * 5))  # Scaled sine wave
            wave.goto(x_coord, y_coord)
            wave.pendown()
        screen.update()
        time.sleep(0.1)
        frame += 1

oscillating_wave()




### Question 3: Bouncing Ball in a Box

import turtle
import time

def bouncing_ball():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()

    x, y = 0, 0
    dx, dy = 5, 3

    while True:
        x += dx
        y += dy

        if x > 400 or x < -400:  # Reflect on horizontal edges
            dx = -dx
        if y > 300 or y < -300:  # Reflect on vertical edges
            dy = -dy

        ball.goto(x, y)
        screen.update()
        time.sleep(0.01)

bouncing_ball()








### Question 4 - Circular Orbit Simulation



import turtle
import math
import time

def circular_orbit():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)

    center = turtle.Turtle()
    center.shape("circle")
    center.color("black")
    center.penup()
    center.goto(0, 0)

    inner_orbit = turtle.Turtle()
    outer_orbit = turtle.Turtle()
    for t in [inner_orbit, outer_orbit]:
        t.shape("circle")
        t.penup()

    for frame in range(20000):
        theta1 = math.radians(frame)  # Inner orbit
        theta2 = math.radians(frame * 0.5)  # Outer orbit
        inner_orbit.goto(50 * math.cos(theta1), 50 * math.sin(theta1))
        outer_orbit.goto(100 * math.cos(theta2), 100 * math.sin(theta2))
        screen.update()
        time.sleep(0.0005)

circular_orbit()







### Question 5 - Ball Following Sine Wave
import turtle
import math
import time

def ball_following_wave():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("purple")
    ball.penup()

    box_width = 800  # Width of the box in pixels
    box_height = 600  # Height of the box in pixels
    x = -box_width // 2  # Start at the left edge of the box
    dx = 5  # Horizontal step size

    while True:
        x += dx
        if x > box_width // 2:  # If ball exits the right edge
            x = -box_width // 2  # Wrap around to the left edge

        y = 100 * math.sin(math.radians(x))  # Calculate sine wave height
        ball.goto(x, y)
        screen.update()
        time.sleep(0.05)

ball_following_wave()







### Question 6 - Animation of Multiple Moving Points


import turtle
import time

def animate_multiple_points():
    screen = turtle.Screen()
    screen.tracer(0)

    colors = ["red", "blue", "green"]
    speeds = [0.1, 0.2, 0.3]
    turtles = []

    for i in range(3):
        t = turtle.Turtle()
        t.shape("circle")
        t.color(colors[i])
        t.penup()
        turtles.append(t)

    for frame in range(200000):  # Animate 200 frames
        for i, t in enumerate(turtles):
            x = (frame * speeds[i]) % 600  # Update the range for the x-axis (default 600 pixels)
            t.goto(x-350, 100 - i * 50)  # Adjust the x and y coordinates to fit the screen size
            # #these values might be different according to your wished point of starts
        '''
        #alternative for loop
        for i in turtles:
            x = (frame * speeds[i]) % 600 
            turtles[i].goto(x-350, 100 - i * 50)
        '''

        screen.update()
        time.sleep(0.0005)

    turtle.done()

animate_multiple_points()









### Question 7 - Bouncing Ball with Gravity
import turtle
import time
import random

def bouncing_ball_gravity():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=600, height=640)  # Set up the window size (600x600 pixels)

    # Create the ball object
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("orange")
    ball.penup()

    # Set random initial position within the box (not touching edges)
    x = random.uniform(-250, 250)
    y = random.uniform(-250, 250)

    # Initial velocity
    dx = random.uniform(-2, 2)  # Horizontal velocity (random)
    dy = random.uniform(-2, -1)  # Vertical velocity (going downward initially)

    gravity = -0.2  # Acceleration due to gravity (negative to accelerate downward)

    # The screen limits in pixels (300 pixels from the center)
    box_min_x = -300
    box_max_x = 300
    box_min_y = -300
    box_max_y = 300

    # Simulate the ball movement
    while True:
        # Apply gravity to the vertical velocity (dy)
        dy += gravity

        # Update position based on velocity
        x += dx
        y += dy

        # Bounce off the left and right walls (screen edges)
        if x <= box_min_x or x >= box_max_x:
            dx *= -1  # Reverse horizontal velocity

        # Bounce off the floor with energy loss, reflect off the ceiling
        if y <= box_min_y:
            dy = -dy * 0.8  # Reverse vertical velocity and lose energy on the floor
            y = box_min_y  # Ensure the ball stays above the floor

        # Reflect off the ceiling (top boundary)
        if y >= box_max_y:
            dy *= -1  # Reverse vertical velocity (bounce off the ceiling)
            y = box_max_y  # Ensure the ball stays below the top boundary

        # Move the ball to the new position
        ball.goto(x, y)
        screen.update()  # Manually update the screen
        time.sleep(0.01)  # Slow down the animation for visual effect

        # Stop if the vertical velocity is small enough and the ball is at the floor
        if abs(dy) < 0.1 and y == box_min_y:
            break

    turtle.done()

bouncing_ball_gravity()







### Question 8 - Pendulum Simulation

import turtle
import math
import time

def pendulum_simulation():
    screen = turtle.Screen()
    screen.tracer(0)

    # Pendulum components
    pendulum = turtle.Turtle()
    pendulum.shape("circle")
    pendulum.color("red")
    pendulum.penup()

    string = turtle.Turtle()  # For the string/rod
    string.hideturtle()
    string.pensize(2)

    pivot = (0, 200)  # Pivot point at the top of the screen

    # Initial angle and angular velocity
    angle = 30  # Starting angle (in degrees)
    angular_velocity = 0  # Initial angular velocity
    damping_factor = 0.99  # Damping to reduce amplitude over time

    # Animation loop
    while True:
        # Simple harmonic motion formula
        angle_acceleration = -0.05 * math.sin(math.radians(angle))  # Gravity acting on pendulum
        angular_velocity += angle_acceleration
        angle += angular_velocity

        # Apply damping to angular velocity
        angular_velocity *= damping_factor

        # Calculate the pendulum bob's position using trigonometry
        length = 200  # Length of the string
        x = pivot[0] + length * math.sin(math.radians(angle))
        y = pivot[1] - length * math.cos(math.radians(angle))

        # Update pendulum bob position
        pendulum.goto(x, y)

        # Draw the string (rod)
        string.clear()
        string.penup()
        string.goto(pivot)
        string.pendown()
        string.goto(x, y)

        screen.update()
        time.sleep(0.0005)  # Slow down the animation for better visual effect

        # Stop when the pendulum is near the bottom and has slowed down
        if abs(angle) == 0 and abs(angular_velocity) < 0.01 and y <= pivot[1]:
            break  # Stop the loop when the pendulum is near the vertical

    turtle.done()

pendulum_simulation()




### Question 9 - Color Changing Sine Wave

import turtle
import math
import time

def color_changing_sine_wave():
    screen = turtle.Screen()
    screen.tracer(0)  # Disable automatic screen updates for smoother animation
    wave = turtle.Turtle()
    wave.penup()
    wave.speed(0)

    # Colors to cycle through for the sine wave
    colors = ["red", "green", "blue", "orange", "purple", "yellow"]

    # Define the width and height of the screen
    screen_width = screen.window_width()  # Get the width of the screen
    screen_height = screen.window_height()  # Get the height of the screen

    for frame in range(2000):  # Animate 20 frames
        wave.clear()  # Clear previous frame
        wave.penup()
        wave.pencolor(colors[frame % len(colors)])  # Cycle through colors

        # Loop over x-values (which will map to screen width)
        for x in range(0, 361):  # x-values from 0 to 360 degrees, corresponding to 0 to 2π radians
            x_rad = math.radians(x)  # Convert degrees to radians
            y_coord = math.sin(x_rad + frame * 0.1)  # Apply sine function and create the wave

            # Map the x and y coordinates to screen space
            x_pos = (x / 360) * screen_width - screen_width / 2  # Scale x from 0 to screen width, centering on the screen
            y_pos = y_coord * (screen_height / 4)  # Scale y from -1 to 1, fitting within the screen's vertical space

            wave.goto(x_pos, y_pos)  # Move the turtle to the calculated position
            wave.pendown()  # Start drawing the wave

        screen.update()  # Update the screen manually
        time.sleep(0.1)  # Slow down the animation for better visual effect

    turtle.done()

color_changing_sine_wave()





### Question 10 - Expanding Circle

import turtle
import time

def expanding_circle():
    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)

    circle_drawer = turtle.Turtle()
    circle_drawer.hideturtle()

    radius = 10
    while radius <= 300:  # Stop when the circle reaches the box boundary
        circle_drawer.clear()
        circle_drawer.penup()
        circle_drawer.goto(0, -radius)  # Center the circle
        circle_drawer.pendown()
        circle_drawer.circle(radius)
        screen.update()
        time.sleep(0.1)
        radius += 10

    # Wait for user to close the window
    screen.mainloop()

expanding_circle()


