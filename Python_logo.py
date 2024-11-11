import turtle

# Initialize turtle and screen objects
t = turtle.Turtle()  # Turtle object to perform drawing
s = turtle.Screen()  # Screen object to set up the canvas properties
s.bgcolor("black")   # Set background color of the canvas to black
t.speed(10)          # Set drawing speed of the turtle
t.pensize(2)         # Set the pen size for drawing
t.pencolor("white")  # Set pen color to white

# Function to draw a small leftward curve
def s_curve():
    for i in range(90):  # Loop to create a smooth curve
        t.left(1)        # Turn turtle 1 degree to the left
        t.forward(1)     # Move turtle forward by 1 unit

# Function to draw a small rightward curve
def r_curve():
    for i in range(90):  # Loop to create a smooth curve
        t.right(1)       # Turn turtle 1 degree to the right
        t.forward(1)     # Move turtle forward by 1 unit

# Function to draw a leftward "S" curve with a forward segment in between
def l_curve():
    s_curve()            # Draw a left curve
    t.forward(80)        # Move forward by 80 units
    s_curve()            # Draw another left curve

# Variant of l_curve with a longer forward segment
def l_curve1():
    s_curve()            # Draw a left curve
    t.forward(90)        # Move forward by 90 units
    s_curve()            # Draw another left curve

# Function to draw half of the logo shape with curves and straight lines
def half():
    t.forward(50)        # Move forward by 50 units
    s_curve()            # Draw a left curve
    t.forward(90)        # Move forward by 90 units
    l_curve()            # Draw an "S" shaped curve with straight segment
    t.forward(40)        # Move forward by 40 units
    t.left(90)           # Turn turtle 90 degrees to the left
    t.forward(80)        # Move forward by 80 units
    t.right(90)          # Turn turtle 90 degrees to the right
    t.forward(10)        # Move forward by 10 units
    t.right(90)          # Turn turtle 90 degrees to the right
    t.forward(120)       # Move forward by 120 units
    l_curve1()           # Draw a longer "S" shaped curve with straight segment
    t.forward(30)        # Move forward by 30 units
    t.left(90)           # Turn turtle 90 degrees to the left
    t.forward(50)        # Move forward by 50 units
    r_curve()            # Draw a right curve
    t.forward(50)        # Move forward by 50 units
    t.end_fill()         # Complete the filled shape

# Function to reposition the turtle to the next starting point
def get_pos():
    t.penup()            # Lift the pen to move without drawing
    t.forward(20)        # Move forward by 20 units
    t.right(90)          # Turn turtle 90 degrees to the right
    t.forward(10)        # Move forward by 10 units
    t.right(90)          # Turn turtle 90 degrees to the right
    t.pendown()          # Put the pen down to resume drawing

# Function to draw the first eye dot
def eye():
    t.penup()            # Lift the pen to move without drawing
    t.right(90)          # Turn turtle 90 degrees to the right
    t.forward(160)       # Move forward by 160 units
    t.left(90)           # Turn turtle 90 degrees to the left
    t.forward(70)        # Move forward by 70 units
    t.pencolor("black")  # Change pen color to black for the eye
    t.dot(35)            # Draw a filled dot with a diameter of 35 units

# Function to draw the second eye dot
def sec_dot():
    t.left(90)           # Turn turtle 90 degrees to the left
    t.penup()            # Lift the pen to move without drawing
    t.forward(310)       # Move forward by 310 units
    t.left(90)           # Turn turtle 90 degrees to the left
    t.forward(120)       # Move forward by 120 units
    t.pendown()          # Put the pen down to draw
    t.dot(35)            # Draw another filled dot with a diameter of 35 units

# Draw the left half of the logo with a specific fill color
t.fillcolor("#306998")   # Set fill color to blue shade (commonly used in Python logo)
t.begin_fill()           # Begin the fill process
half()                   # Draw the half shape
t.end_fill()             # Complete the fill for this half

# Reposition the turtle and draw the right half of the logo with a yellow color
get_pos()                # Move turtle to starting point for second half
t.fillcolor("#FFD43B")   # Set fill color to yellow shade
t.begin_fill()           # Begin the fill process
half()                   # Draw the half shape
t.end_fill()             # Complete the fill for this half

# Draw the eyes on the logo
eye()                    # Draw the first eye dot
sec_dot()                # Draw the second eye dot

# Function to create a slow 90-degree left rotation, possibly to add a pause effect
def pause():
    t.speed(2)           # Set drawing speed to slower for effect
    for i in range(100): # Loop to rotate turtle in 90-degree steps
        t.left(90)       # Turn turtle 90 degrees to the left

pause()  # Call the pause function
