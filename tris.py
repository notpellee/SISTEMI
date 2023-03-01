import turtle
import math

X_START = -290
Y_START = 250
LATO = 480

posizioni = {7:(X_START+(LATO/3)/2, Y_START-(LATO/3)/2), 8:(X_START+LATO/2, Y_START-(LATO/3)/2), 9:(X_START+(LATO-(LATO/3)/2), Y_START-(LATO/3)/2),
             4:(X_START+(LATO/3)/2, Y_START-LATO/2), 5:(X_START+LATO/2, Y_START-LATO/2), 6:(X_START+(LATO-(LATO/3)/2), Y_START-LATO/2),
             1:(X_START+(LATO/3)/2, Y_START-(LATO-(LATO/3)/2)), 2:(X_START+LATO/2, Y_START-(LATO-(LATO/3)/2)), 3:(X_START+(LATO-(LATO/3)/2), Y_START-(LATO-(LATO/3)/2))}

caselle = [{0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
            ,{0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}]

curs = turtle.Turtle()
finesta = turtle.Screen()

def disegnaCroce(x,y):
    curs.penup()
    curs.setposition(x,y)
    curs.pendown()
    curs.width(9)
    curs.color("black")

    curs.right(45)
    curs.forward(70)
    curs.backward(140)
    curs.forward(70)
    curs.left(90)
    curs.forward(70)
    curs.backward(140)
       
    curs.right(45)
    curs.penup()
    curs.setposition(x,y)
    curs.pendown()
    curs.width(3)
    curs.color("red")

    curs.right(45)
    curs.forward(70)
    curs.backward(140)
    curs.forward(70)
    curs.left(90)
    curs.forward(70)
    curs.backward(140)

    curs.right(45)

def disegnaCerchio(x,y):
    curs.penup()
    curs.setposition(x,y-(LATO/4)/2)
    curs.pendown()

    curs.width(9)
    curs.color("black")
    curs.circle(60)

    curs.penup()
    curs.setposition(x,y-(LATO/4)/2)
    curs.pendown()

    curs.width(3)
    curs.color("blue")
    curs.circle(60)

def winOriz(i):
    curs.penup()
    curs.setposition(posizioni[i*3][0]+20,posizioni[i*3][1])
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.backward(LATO*4/6 + 40)

    curs.penup()
    curs.setposition(posizioni[i*3][0]+20,posizioni[i*3][1])
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.backward(LATO*4/6 + 40)


def winVert(i):
    curs.penup()
    curs.setposition(posizioni[6+i][0],posizioni[6+i][1]+20)
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.right(90)
    curs.forward(LATO*4/6 + 40)

    curs.left(90)

    curs.penup()
    curs.setposition(posizioni[6+i][0],posizioni[6+i][1]+20)
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.right(90)
    curs.forward(LATO*4/6 + 40)

def winObl1():
    curs.penup()
    curs.setposition(posizioni[7][0]-15,posizioni[7][1]+15)
    curs.pendown()

    curs.speed(1)
    curs.width(15)
    curs.color("black")
    curs.right(45)
    curs.forward(LATO + 15)

    curs.left(45)

    curs.penup()
    curs.setposition(posizioni[7][0]-15,posizioni[7][1]+15)
    curs.pendown()

    curs.speed(1)
    curs.width(8)
    curs.color("lime")
    curs.right(45)
    curs.forward(LATO + 15)

def winObl2():
    curs.penup()
    curs.setposition(posizioni[9][0]+15,posizioni[9][1]+15)
    curs.pendown()

    curs.width(15)
    curs.color("black")
    curs.right(135)
    curs.forward(LATO + 15)

    curs.left(135)

    curs.penup()
    curs.setposition(posizioni[9][0]+15,posizioni[9][1]+15)
    curs.pendown()

    curs.width(8)
    curs.color("lime")
    curs.right(135)
    curs.forward(LATO + 15)


def win(k):
        for i in range(1,4):#controllo vittoria orizzontale
            if caselle[k][1+(3*(i-1))] and caselle[k][2+(3*(i-1))] and caselle[k][3+(3*(i-1))]:
                winOriz(i)
                turtle.done()
        
        for i in range(1,4):#controllo vittoria verticale
            if caselle[k][i] and caselle[k][3+i] and caselle[k][6+i]:
                winVert(i)
                turtle.done()

        if caselle[k][7] and caselle[k][5] and caselle[k][3]:
            winObl1()
            turtle.done()

        if caselle[k][1] and caselle[k][5] and caselle[k][9]:
            winObl2()
            turtle.done()
    
    
class Tris():

    def disegnaCampo(self):
        curs.speed(0)
        curs.penup()
        curs.setposition(X_START,Y_START)           #coordinate iniziali campo
        curs.pendown()
        curs.width(10)                              #setta spessore del
        
        curs.begin_fill()                           #colorare il campo
        for _ in range(0,4):                        #disegna il campo
            curs.forward(LATO)
            curs.right(90)

        curs.color("#FCFF8D")                       #colora il quadrato
        curs.end_fill()                             #fine colore 

        curs.color("black")
        curs.right(90)  
        for i in range(1,3):                        #caselle campo(righe verticali)
            curs.penup()
            curs.setposition(X_START+((LATO/3)*i), Y_START)
            curs.pendown()
            curs.forward(LATO)

        curs.left(90)
        for i in range(1,3):                        #caselle campo(righe orizzontali)
            curs.penup()
            curs.setposition(X_START, Y_START-((LATO/3)*i))
            curs.pendown()
            curs.forward(LATO)

        curs.penup()
        curs.setposition(X_START,Y_START)           #coordinate iniziali campo
        curs.pendown()
        curs.width(5)                              #setta spessore del
        curs.color("gold")

        for _ in range(0,4):                        #disegna il campo
            curs.forward(LATO)
            curs.right(90)

        curs.right(90)  
        for i in range(1,3):                        #caselle campo(righe verticali)
            curs.penup()
            curs.setposition(X_START+((LATO/3)*i), Y_START)
            curs.pendown()
            curs.forward(LATO)

        curs.left(90)
        for i in range(1,3):                        #caselle campo(righe orizzontali)
            curs.penup()
            curs.setposition(X_START, Y_START-((LATO/3)*i))
            curs.pendown()
            curs.forward(LATO)

    def tris(self):

        funzioni = {0:disegnaCerchio, 1:disegnaCroce}
        
        i=0
        while i<9:
            
            n = (int)(input("Inserisci: "))
            
            if n<1 or n>9:
                print("casella errata")
            else:
                if not caselle[0][n] and (not caselle[1][n]):
                    funzioni[i%2](posizioni[n][0],posizioni[n][1])
                    caselle[i%2][n]=True
                    i+=1
                    win(i%2-1)
                else:
                    print("Gia inserita")
        
        turtle.done()
        
def main():
    tris = Tris()

    tris.disegnaCampo()
    tris.tris()

if __name__=="__main__":
    main()