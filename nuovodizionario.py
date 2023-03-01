dizionario = {"w": "avanti", "a":"sinistra", "s":"indietro", "d":"destra",
"i": "avanti", "j":"sinistra", "k":"indietro", "l":"destra"}


avanti = []

for chiave in dizionario:
    if dizionario[chiave] == "avanti":
        avanti.append(chiave)

print(avanti)

l =  ["ciao", print, 1, 3.24]
for k ,v in enumerate(l):
    print(k,v)