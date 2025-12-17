# geometry.py

import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Take user input
shape = input("Calculate area of circle or rectangle? (c/r): ").lower()

if shape == 'c':
    r = float(input("Enter radius of the circle: "))
    print("Area of the circle:", area_circle(r))
elif shape == 'r':
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    print("Area of the rectangle:", area_rectangle(l, w))
else:
    print("Invalid choice!")