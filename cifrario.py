d = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g","g":"h", "h":"i","i":"l","l":"m","m":"n", "n":"o","o":"p", 
     "p":"q", "q":"r", "r":"s", "s":"t","t":"u","u":"v", "v":"z","z":"a", " ":" ",}

lettera = input("inserisci una stringa")
messaggio = ""

for elemento in lettera:
    messaggio = messaggio + d[elemento]

print(messaggio)