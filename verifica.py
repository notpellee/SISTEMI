def Stampa_nomi(nome):
    file = open(nome, "r")
    lista_righe = file.readlines
    file.fclose()

    tot = 0
    diz = {}

    for riga in lista_righe:
        lista_campi = riga[:-1].split(";")

        tot += int(lista_campi[2])


Stampa_nomi("C:\Users\Demaria\Desktop\VERIFICA\4AROB_GITA.csv")