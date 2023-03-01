import turtle
finsetra = turtle.Screen() #oggetto
alice=turtle.Turtle() #oggetto
alice.color("red")
bob=turtle.Turtle() #oggetto
bob.color("black")
bob.penup()
bob.setposition(-50,50)
bob.pendown()

for i in range(8):
    alice.forward(100)
    alice.right(45)
    bob.forward(100)
    bob.right(-45)

turtle.done()