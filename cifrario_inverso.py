dizionario = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g","g":"h", "h":"i", "l":"m","m":"n", "n":"o","o":"p", 
     "p":"q", "q":"r", "r":"s", "s":"t","t":"u","u":"v", "v":"z","z":"a", " ":" "}

lettera = input("inserisci una stringa")
messaggio = ""
dizionario2 = {}

for chiave , valore in dizionario.items(): #ciclo for su due variabili contemporaneamente
    print(chiave, valore)
    dizionario2[valore] = chiave 
print(dizionario2)

for elemento in lettera:
    messaggio = messaggio + dizionario2[elemento]
    
print(messaggio)