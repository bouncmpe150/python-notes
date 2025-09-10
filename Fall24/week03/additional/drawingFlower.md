# Drawing a Flower with Turtle Graphics and File I/O
Create a program that uses the turtle graphics library to draw a flower with six petals. In addition to drawing, the program should demonstrate file input/output (I/O) operations by recording the coordinates of the turtle's position during the drawing process.

### Requirements:

#### Turtle Graphics

* Utilize the turtle module to draw a flower with six petals.

* Each petal should be created using arcs, and the turtle should rotate appropriately between petals to form a complete flower shape.

#### File I/O Operations

* Create a new text file named flower_coordinates.txt.

* Write to this file the starting and ending coordinates (x, y) of the turtle for each petal drawn.

* After all petals are drawn, add a message to the file stating that the flower drawing is complete.

#### Code Structure

* Implement a function to draw a single petal and record its coordinates in the file.
  
* Ensure that file handles are properly managed and closed after writing and appending data to prevent resource leaks.

#### Additional Details

* Use turtle.hideturtle() to hide the turtle cursor after the drawing is complete.
  
* The program should be executed in an environment where the turtle graphics window can be displayed.

### Hints:

* You can use t.circle(radius, angle) to draw arcs for the petals.
  
* To get the current position of the turtle, use t.xcor() and t.ycor().
  
* Use the with open(...) statement for file handling to ensure proper closure of the file.

### Expected Output:

* A window displaying a flower with six petals drawn by the turtle.
  
* A text file (flower_coordinates.txt) containing the coordinates of the turtle's position at the start and end of each petal, as well as a completion message.
