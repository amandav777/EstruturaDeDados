import random

lista = [random.randint(1, 30) for _ in range(150)]

individuais = []

i = 0
while i < len(lista):
    repetido = False
    indice_anterior = 0
    while indice_anterior < i:
        if lista[i] == lista[indice_anterior]:
            repetido = True
            break
        indice_anterior += 1
    if not repetido:
        individuais.append(lista[i])
    i += 1

print("Lista original:", lista)
print("Lista sem repetições:", individuais)
