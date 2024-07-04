class Shape:
    def __init__(self):
        self.color = (1,2,3)

class Rectangle(Shape):
    def __init__(self, w,h):
        Shape.__init__(self) # Need to call constructor function in superclass
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height
    
rect1 = Rectangle(20,10)
print(rect1.height)
print(rect1.width)
print(rect1.area())
print(rect1.color)