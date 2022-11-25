import turtle

draw = turtle.Turtle()
for i in range(1, 5 + 1, 1):
    draw.forward(50)
    draw.right(144)
draw.left(90)
draw.penup()
draw.forward(75)
draw.pendown()
draw.left(90)
draw.penup()
draw.forward(40)
draw.pendown()
draw.right(90)
for i in range(1, 200 + 1, 1):
    draw.forward(1)
    draw.right(1)


