import random
l1 = [random.randint(1, 6) for _ in range(10)]
l2 = [random.randint(1, 6) for _ in range(10)]
file = open("dadi.txt","w")

for lista1, lista2 in zip(l1, l2):
    file.write(f'{lista1}, {lista2}\n')
    print(f'{lista1}, {lista2}\n')

file.close()