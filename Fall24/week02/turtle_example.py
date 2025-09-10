
import turtle
import time

clicked = False
def on_click(x, y):
    global clicked
    clicked = True

turtle.onscreenclick(on_click)

def waitonclick():
    global clicked
    turtle.update()
    clicked = False
    while not clicked:
        turtle.update()
        time.sleep(.1)
    clicked = False
    turtle.clear()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pendown()

turtle.update()
turtle.speed("fastest")

# Draw your star shape in the following editable code block
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
waitonclick()

# Draw your Hexagon shape in the following editable code block
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
waitonclick()

# Draw your Spiral shape in the following editable code block
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
waitonclick()

# Draw your Olimpia shape in the following editable code block
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
waitonclick()

# Draw your Chain of Rings shape in the following editable code block
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

turtle.done()

