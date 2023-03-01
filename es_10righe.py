import turtle 

obj=turtle.Turtle()
fin=turtle.Screen()

diz = {"forward":obj.forward,"right":obj.right,"left":obj.left,"backward":obj.backward}

def leggi():
    file = open("file.csv","r")
    lista_righe=file.readlines()
    file.close()

    return lista_righe

def main():
    for riga in leggi():
        lista_campi = riga[:-1].split(",")
        
        diz[lista_campi[0]](int(lista_campi[1]))
    turtle.done()

if __name__=="__main__":
    main()