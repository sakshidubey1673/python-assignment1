#A wire is the form of Arc at an angle of 60 degrees
#and the radius of the arc is 42
#the wire is converted into a square.Find the area of the square

import math
radius = 42
theta = 60
length = (theta/360)*2*radius*math.pi
side = length/4
area = side*side
print("Area of the square is :",area)
print("side of the square is :",side)
print("length of the square is :",length)