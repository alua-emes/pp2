#4. Write the definition of a Point class. Objects from this class should have a

       # a method show to display the coordinates of the point
       # a method move to change these coordinates
       # a method dist that computes the distance between 2 points
import math
class Point(object):
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def show(self):
         return self.x, self.y
     def move(self, x, y):
         self.x += x
         self.y += y
     def dist(self, pt):
         dx = pt.x - self.x
         dy = pt.y - self.y
         return math.sqrt(dx ** 2 + dy ** 2)

pt = Point(1, 0)
p = Point(0, 0)

print(p.move(1, 2))
print(p.show())
print(p.dist(pt))
