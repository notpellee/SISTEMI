import turtle
costanti = (40, 90, 30, 20)
for i in range(0,4):
    turtle.forward(costanti[0])
    turtle.right(costanti[1])
turtle.up()
turtle.goto(10,-10)
turtle.down()
for i in range(0,4):
    turtle.forward(costanti[3])
    turtle.right(costanti[1])

turtle.done()