lista1 = ["a","b","c","d"]
lista2 = [1,2,3,4]

#c-style con lista1
for i in range(0,len(lista1)):
    print (lista1[i])

print("\n")
#python-style con lista1
for i in lista1:
    print(i)
print("\n")
#enumerate su lista1
for i,e in enumerate(lista1):
    print(f"lemento {i} = {e}")

#lista1 e lista2 python-style (zip)
for a,b in zip(lista1,lista2):
    print(a,b)
print("\n")
#lista1 e lista2 in c-style (range)
for a in range(0,len(lista1)):
    print(lista1[a], lista2[a])

print("\n")
diz = {1: "a", 2: "b", 3: "c"}

#for su diz usando items()
for k,v in diz.items():
    print(f'chiave = {k}, valore = {v}')

print("\n")
#for su diz non usando items()

for k in diz:
    print(f'chiave = {k}, valore = {diz[k]}')