# We are learing how to make codes in to picture.
# 9/4/2019
# CTI-110 P2HW2 - Turtle Graphic
# Omar Roman Jr


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)           # sets the size of the shape
t.pencolor("Blue")     # set pencolor (takes string)
t.shape("turtle")
win.bgcolor("lightblue")


# Big Triangle commands
t.forward(300)          
t.left(120)            
t.forward(300)
t.left(120)
t.forward(300)

# The little triangle with color 
t.fillcolor('pink')
t.begin_fill()
t.right(200)            
t.forward(200)
t.right(81)
t.forward(200)
t.end_fill()

t.right(139)
t.forward(300)
# end commands
win.mainloop()             # Wait for user to close window
