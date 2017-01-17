class Canvas:
    def __init__(self, width, length):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(length)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print ("\n" .join(["".join(row) for row in self.data]))

class Shape:
    def paint(self, canvas): pass

class Rectangle(Shape):
    def __init__(self, x, y, z, a):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

    def hline(self, x, y, z):
        pass

    def vline(self, x, y, a):
        pass

    def paint(self, canvas):
        hline(self.x, self.y, self.z)
        hline(self.x, self.y + self.a, self.z)
        vline(self.x, self.y, self.a)
        vline(self.x + self.z, self.y, self.a)

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)
