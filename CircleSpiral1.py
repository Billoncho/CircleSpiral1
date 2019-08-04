# CircleSpiral1.py
# Billy Ridgeway
# Draws a spiral of circles.

import turtle           # Imports turtle graphics.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the drawing speed to fast.
for x in range (100):   # Creates a loop of 100 times.
    t.circle(x)         # Tells the pen to draw circles.
    t.left(60)          # Moves the pen left by 60 pixels.
