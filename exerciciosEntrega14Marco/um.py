def indiceMenorValor(lista):
    minimo = 0
    atual = 1
    
    while atual < len(lista):
        if lista[atual] < lista[minimo]:
            minimo = atual
        atual += 1
    return minimo

lista = [10, 5, 8, 3, 12, 6]
indice_menor = indiceMenorValor(lista)
print("O índice do menor valor na lista é", indice_menor)
print("O menor valor na lista é", lista[indice_menor])
