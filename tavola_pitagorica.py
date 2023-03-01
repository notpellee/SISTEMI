lista = []

lista = [[i*n for i in range(1,11)] for n in range(1,11)]

file = open( "tavola_pitagorica.txt", "w")

for elemento in lista:
    file.write(f'{elemento}')
    file.write("\n")

file.close()
