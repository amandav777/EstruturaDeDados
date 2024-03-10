def inverterLista(lista):
    tamanho = len(lista)
    for i in range(tamanho // 2):
        lista[i], lista[tamanho - i - 1] = lista[tamanho - i - 1], lista[i]

# Exemplo de uso
lista = [1, 3, 8, 9, 13]
print("Lista normal:", lista)

inverterLista(lista)
print("Lista invertida:", lista)

