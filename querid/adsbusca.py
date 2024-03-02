import random

def gera_lista(tamanho, embaralhar=True):
    lista = []
    for i in range(1, tamanho + 1):
        lista.append(i)
    if embaralhar:
        random.shuffle(lista)

    return lista


def buscaSequencial(valor, lista):
    # busca por um valor em uma lista de forma sequencial, se encontrar, retorna o indice. se nao achar, retorna -1
    indice_Atual = 0
    while indice_Atual < len(lista):
        if lista[indice_Atual] == valor:
            return indice_Atual
        indice_Atual += 1

    return -1


def gera_lista_aleatoria(tamanho, inicial, final):
    if tamanho > final - inicial + 1:
        print("O tamanho deve ser menor ou igual ao intervalo")
        return
    lista = []
    atual = 0
    while atual < tamanho:
        valor = random.randint(inicial, final)
        if valor not in lista:
            lista.append(valor)
            atual += 1
    return lista

def busca_binaria(valor, lista_ordenada):
    esquerda = 0
    direita = len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if valor == lista_ordenada[meio]:
            return meio
        elif valor < lista_ordenada[meio]:
            direita = meio - 1  # Ajuste: Mudei "direita = meio + 1" para "direita = meio - 1"
        else:
            esquerda = meio + 1
    return -1  # Coloquei o "return -1" fora do loop
