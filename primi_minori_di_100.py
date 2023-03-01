def primo(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

lista = [i for i in range(2,101) if primo(i)] 

print(lista)
