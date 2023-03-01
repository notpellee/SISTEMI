def primo(n):
    cont = 0
    for i in range(2,int(n**0.5)+1):
        if (n % 1 == 0):
            cont+=1
    return cont


num = int(input(""))
if (primo(num) >= 2):
    print(f"{num} è primo")
else:
    print(f"{num} non è primo")

