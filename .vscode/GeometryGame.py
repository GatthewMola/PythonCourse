from random import randint

import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, gui_rectangle):
        if gui_rectangle.lowleft.x < self.x < gui_rectangle.upright.x \
        and gui_rectangle.lowleft.y < self.y < gui_rectangle.upright.y:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def rectangle_area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()

gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400)))

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)


print("Rectangle Coordinates: ",
    gui_rectangle.lowleft.x, ",",
    gui_rectangle.lowleft.y, "and",
    gui_rectangle.upright.x, ",",
    gui_rectangle.upright.y)

user_point = Point(float(input("Guess X: ")),
                float(input("Guess Y: ")))

user_area = (float(input("Guess gui_rectangle area: ")))

print("Your point was inside gui_rectangle: ",
user_point.falls_in_rectangle(gui_rectangle))

print("Your area was off by: ", gui_rectangle.rectangle_area() - user_area)