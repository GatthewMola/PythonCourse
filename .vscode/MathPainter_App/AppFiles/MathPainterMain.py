class Square:

    def __init__(self, x, y, s, color):
        self.x = x
        self.y = y
        self.s = s
        self.color = color
    
    def draw(self, canvas):
        pass

class Rectangle:

    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, canvas):
        pass

class Canvas:
    
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color
    
    def make(self):
        pass