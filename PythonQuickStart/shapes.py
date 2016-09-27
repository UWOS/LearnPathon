#! python3

# shapes.py

"""a collection of functions
for printing basic shapes.
"""

CHAR = '*'

def rectangle(height, width):
    """prints a rectangle."""
    for row in range(height):
        for col in range(width):
            print(CHAR, end = '')
        print()

def square(side):
    """prints a square."""
    rectangle(side, side)

def triangle(height):
    """prints a right triangle."""
    for row in range(height):
        for col in range(1, row + 2):
            print(CHAR, end = '')
        print()
