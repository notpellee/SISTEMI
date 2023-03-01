def leggi_file(nome_file):

    file = open(nome_file, "r")
    lista_righe = file.readlines()
    file.close()

    diz_matematici = {"id":[], "nomi":[]}  #    id num e nomi stringhe
    print(diz_matematici)

    for riga in lista_righe[1:]:
        riga_senza_linefin = riga[:-1]
        lista_campi = riga_senza_linefin.split(",")
        id = int(lista_campi[0])
        nome = lista_campi[1]
        #print(id,nome)
        diz_matematici["id"].append(id)
        diz_matematici["nomi"].append(nome[1:])
    
    return diz_matematici

def main():
    diz = leggi_file("./file.csv")
    print(diz)

if __name__ == "__main__":
    main()


