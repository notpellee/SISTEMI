ip =input("inserisci l'ip adress")
broadcast = int(input("inserisci il broadcast") [1:])
ip = [int (ip) for ip in ip.split(".")]
l = []
lnew = []
ldef = []
i = 0
for n in ip:
    stringa = str(bin(n))
    l.append(stringa[2:]) 

host = 32-broadcast

for a in range(broadcast):
    lnew.append(1)

for a in range(host):
    lnew.append(0)
    
intero = broadcast % 8

for a in range(0, 33):
    if lnew[a] == 1:
        ldef[a]=l[intero][a]
    elif lnew[a] == 0:
        ldef[a] == 0

    if a == 8 or a == 16 or a == 24:
        intero+=1

print(lnew)
print(l)
