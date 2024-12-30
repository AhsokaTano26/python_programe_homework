class Rect:
    def __init__(self, tl, br): 
        self.tl, self.br = tl, br 

    def width(self):
        t = self.br.x - self.tl.x 
        return t if t > 0 else -t
    
    def height(self):
        t = self.br.y - self.tl.y 
        return t if t > 0 else -t

    def area(self):
        return self.width() * self.height()

    def topRight(self):
        return Point(self.br.x,self.tl.y)
    
    def bottomLeft(self):
        return Point(self.tl.x,self.br.y)
    
    def diagonalLength(self): 
        return self.br - self.tl

class Point:
    def __init__(self,x,y):
        self.x, self.y = x, y
    
    def __sub__(self,p):
        return ((self.x - p.x)**2 + (self.y - p.y)**2) ** 0.5
    
    def __str__(self):
        return str((self.x,self.y))

rt = Rect(Point(1,6),Point(7,8))

print("Vertices of rectangle rt:")
print(f"{rt.tl}-----------------------------{rt.topRight()}")
print(f"{rt.bottomLeft()}-----------------------------{rt.br}")

print("Size information of rectangle rt:")
print(f"width - {rt.width()}\theight - {rt.height()}")
print(f"area - {rt.area()}\tdiagonal length - "\
    f"{rt.diagonalLength()}")

