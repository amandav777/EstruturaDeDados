from time import perf_counter
import adsbusca

# lista = adsbusca.gera_lista(10)
# print(lista)


# Gera lista com 50000 valores
print("Gerando a lista....")
lista = adsbusca.gera_lista(50000)
print("Lista gerada!")
valor = 26789

print("Iniciando a busca...")
inicio = perf_counter()
# Coloca a posição que quer achar
posicao = adsbusca.buscaSequencial(valor, lista)
fim = perf_counter()
print("Busca realizada!")

tempo = fim - inicio

print(f"Valor {valor} encontrado em {tempo:.6f} segundos.")



