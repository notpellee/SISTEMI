vocali = ["a","e","i","o","u"]

s = input("inserisci una stringa")
l = [c for c in s if not(c in vocali)]

print(l)