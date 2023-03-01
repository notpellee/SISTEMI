diz = {"(": ")", "[": "]", "{":"}"}
stringa = "{[3+(a+b)] + 8}"
pila = [] 

for i,x in enumerate(stringa):
    if (x in diz):
        pila.append(x)
    if (x == diz["{"] or x == diz["["] or x == diz["("]):
        ritorno  = pila.pop()
        if diz[ritorno] != x:
            print(f"parentesi non uguali, ERRORE in posizione {i}")
    


if (len(pila) == 0):
    print("parentesi chiuse correttamente")
else:
    print("parentesi non chiuse correttamente")
