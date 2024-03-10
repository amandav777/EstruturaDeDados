def encontrarTresMaiores(lista):
    primeiro_maior = segundo_maior = terceiro_maior = float('-inf')

    for numero in lista:
        if numero > primeiro_maior:
            terceiro_maior = segundo_maior
            segundo_maior = primeiro_maior
            primeiro_maior = numero
        elif numero > segundo_maior:
            terceiro_maior = segundo_maior
            segundo_maior = numero
        elif numero > terceiro_maior:
            terceiro_maior = numero

    return primeiro_maior, segundo_maior, terceiro_maior

# Exemplo de uso
lista = [10, 5, 8, 3, 12, 6]
maior1, maior2, maior3 = encontrarTresMaiores(lista)
print("Os três maiores valores são:", maior1, ",", maior2, "e", maior3)

