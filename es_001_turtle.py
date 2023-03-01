import math
def main():

    import turtle
    finsetra = turtle.Screen() #oggetto
    tartarughe = [turtle.Turtle() for _ in range(8)]
    
    triangolo(tartarughe[0])
    quadrato(tartarughe[1])
    pentagono(tartarughe[2])
    esagono(tartarughe[3])
    ettagono(tartarughe[4])
    ottagono(tartarughe[5])
    nonagono(tartarughe[6])

    poligono(tartarughe[7],100,200,5,"red")
    diz_pos={3 : (-400, 90,"red"), 4 : (-300, 90,"red"),5 : (-200, 90,"red"),6 : (-100, 10,"red"),
    7 : (-200, 10,"red"), 8 : (-300, 10,"red"),9 : (-400,10,"red")}
    for nLati,pos in diz_pos.items():
        poligono(tartarughe[nLati],pos[0], pos[1], nLati, "red")
    
def poligono(t,posx,posy,nlati,colore):
    t.color("black")
    t.begin_fill()
    t.penup()
    t.setposition(posx,posy)
    t.pendown()
    angolo = 360/nlati
    lato = 2*40*math.sin(angolo/2*3.1415/180)
    
    for _ in range(nlati):
        t.right(angolo)
        t.forward(lato)
        
    t.color(colore)
    t.end_fill()



def triangolo(t):
    t.goto(1,1)
    t.begin_fill()
    t.color("red")
    for i in range(3):
        t.forward(20)
        t.right(120)
    t.end_fill()


def quadrato(t):
    t.up()
    t.goto(25,1)
    t.down()

    for i in range(4):
        t.forward(20)
        t.right(90)

def pentagono(t):
    t.up()
    t.goto(55,1)
    t.down()

    for i in range(5):
        t.forward(20)
        t.right(72)

def esagono(t):
    t.up()
    t.goto(0,-40)
    t.down()

    for i in range(6):
        t.forward(20)
        t.right(60)

def ettagono(t):
    t.up()
    t.goto(60,-40)
    t.down()

    for i in range(7):
        t.forward(20)
        t.right(51)

def ottagono(t):
    t.up()
    t.goto(120,-40)
    t.down()

    for i in range(8):
        t.forward(20)
        t.right(45)

def nonagono(t):
    t.up()
    t.goto(1,-80)
    t.down()

    for i in range(9):
        t.forward(20)
        t.right(40)

    

if __name__ == "__main__":
    main()
    


