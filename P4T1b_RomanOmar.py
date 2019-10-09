# CTI-110 
# P4Tb - Turtle Graphics
# Omar Roman
# 9/18/2019
#

import turtle             
win = turtle.Screen()      

t = turtle.Turtle() 
t.shape("turtle")
t.color("blue")
t.pensize(5)


def my_Initials():
    t.circle(45)
    t.penup()
    t.forward(65)
    t.pendown()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.circle(-27, 180)
    t.left(130)
    t.forward(40)

my_Initials()

# Wait for user to close window.
win.mainloop()
