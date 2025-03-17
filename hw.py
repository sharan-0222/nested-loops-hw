import turtle 
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400,450)
t=turtle.Turtle()
side=4
length=55
angle=360/side
for i in range(side) :
    t.forward(length)
    t.right(angle)
turtle.done()