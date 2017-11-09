import math

class Vector():
    def __init__(self, x, y):
        self.x = y
        self.y = x
        
    def getAngle(self):
        rad = math.atan(self.x/self.y)
        return math.degrees(rad)

    def getMagnitude(self):
        sx = self.x**2
        sy = self.y**2
        return math.sqrt(sx + sy)