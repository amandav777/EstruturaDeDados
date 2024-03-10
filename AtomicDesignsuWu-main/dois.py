def encontrarMaiorValor(lista):
    maior_valor = lista[0] 
    indiceMaior = 0 

    for i in range(1, len(lista)):
        if lista[i] > maior_valor:
            maior_valor = lista[i]
            indiceMaior = i

    return maior_valor, indiceMaior

# Exemplo de uso
lista = [10, 5, 8, 3, 12, 6]
valor_maximo, indice_maximo = encontrarMaiorValor(lista)
print("O maior valor na lista é:", valor_maximo)
print("Este valor está na posição:", indice_maximo)
