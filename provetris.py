def posizione(tavola):
    posizione = int(input("inserisci una posizione da 0 a 8"))
    return tavola[posizione]
def main():
    tavola_gioco = ['#','#','#','#','#','#','#','#','#']
    k = 0
    while(posizione(tavola_gioco) == '#'):
        posizione(tavola_gioco)
    tavola_gioco[posizione] = gicatore1

    
    
    

if __name__ == "__main__":
    main()
    