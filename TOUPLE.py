import math

triangolo = [(1.5, 3.6), (-1.0, 0.0), (5.1, 4.3)]
print(f"la cordinata y del secondo veritce è {triangolo[1][1]}")
val = 0.5 * abs(triangolo[0][1]*(triangolo[1][0]-triangolo[2][0])+ triangolo[1][1]*(triangolo[2][0] - triangolo[0][0])+ triangolo[2][1]*(triangolo[0][0]-triangolo[1][0]))
print(f" area = {val :.2f}")