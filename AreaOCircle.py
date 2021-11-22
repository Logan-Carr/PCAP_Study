################################################
## Program name: AreaOCircle.py

# Author: Logan Carr
# Course: Python Essentials
# Date 11/20/2021
# Assignment: Module 4 - Area of a Circle
###Purpose: The following forumla gives the 
##distance between two points, 
#(x1, y1) and (x2, y2) in the Cartesian plane:
################################################



import math
  
x = float(input("Enter x of circle center: "))
y = float(input("Enter y of circle center: "))

x1 = float(input("Enter x of a point on the circle: "))
y1 = float(input("Enter y of a point on the circle: "))
  
calculateRadius = ((x-x1)*(x-x1) + (y-y1)*(y-y1) )** 0.5

print("This is the Radius:", calculateRadius)

calculateArea = math.pi * calculateRadius ** 2
  
print("This is the Area:", round(calculateArea, 2))

calculatePerimeter = 2 * (math.pi * calculateRadius)
  
print("This is the Perimeter:", round(calculatePerimeter, 2))