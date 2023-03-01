import turtle
COLONNA_UNO_X=1
COLONNA_DUE_X=200
COLONNA_UNO_Y = 200
COLONNA_DUE_Y = 100
LUNGHEZZA_COLONNE = 440
LUNGHEZZA_RIGHE = 480

t = turtle.Turtle()
finsetra = turtle.Screen()

def disegna(t):
    t.pensize(5)
    t.color("green")
    #colonna 1
    t.right(90)
    t.up()
    t.goto(COLONNA_UNO_X,COLONNA_UNO_Y)
    t.down()
    t.forward(LUNGHEZZA_COLONNE)
    #colonna 2
    t.up()
    t.goto(COLONNA_DUE_X,COLONNA_UNO_Y)
    t.down()
    t.forward(LUNGHEZZA_COLONNE)
    #riga 1
    
    t.up()
    t.goto(COLONNA_UNO_X-140,COLONNA_UNO_Y-146)
    t.down()
    t.left(90)
    t.forward(LUNGHEZZA_RIGHE)
    #riga 2
    t.up()
    t.goto(COLONNA_UNO_X-140,COLONNA_UNO_Y-293)
    t.down()
    t.forward(LUNGHEZZA_RIGHE)
    
def scelta():
    giocatore1 = input("giocatore 1 scegli X o O")
    if(giocatore1 == 'X'):
        return 'X','O' 
    else:
        return 'O','X'

def posizione(tavola):
    posizione = int(input("inserisci una posizione da 0 a 8"))
    return tavola[posizione]

def main():
    t = turtle.Turtle()
    finsetra = turtle.Screen()
    disegna(t)
    tavola_gioco = ['#','#','#','#','#','#','#','#','#']
    giocatore1,giocatore2 = scelta()
    print(f"sclte: \nGiocatore 1 = {giocatore1}\nGiocatore 2 = {giocatore2}")
    k = 0
    
    if( k % 2 == 0):
        
        while(posizione(tavola_gioco) == '#'):
            posizione(tavola_gioco)
    tavola_gioco[posizione] = giocatore1

        

        
    

if __name__ == "__main__":
    main()
    