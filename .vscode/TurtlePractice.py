import turtle

myturtle = turtle.Turtle()

# Go to a certain coordinate (50 pixels on x axis, 75 on y)
myturtle.penup() # Picks up the pen so that it does not draw the "goto" line
myturtle.goto(50, 75)

myturtle.pendown() # Puts the pen back down on the canvas
myturtle.forward(100) # Move 100 pixels
myturtle.left(90) # Turn left 90 degrees
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()