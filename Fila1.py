# 1. Crie uma lista vazia chamada "fila".
fila = []
# 2. Adicione o elemento "10" à fila utilizando o método "append".
fila.append(10)
# 3. Adicione o elemento "20" à fila utilizando o método "append".
fila.append(20)
# 4. Adicione o elemento "30" à fila utilizando o método "append".
fila.append(30)

# 5. Imprima a fila utilizando o comando "print".
print(f"Fila antes de remover: {fila}")

# 6. Remova o primeiro elemento da fila utilizando o método "pop(0)" e armazene-o na variável "x".
x = fila.pop(0)

# 7. Imprima a variável "x".
print(f"Fila depois de remover: {fila}")
print(f"Removidos na primeira remoção: {x}")

# 8. Remova o próximo elemento da fila utilizando o método "pop(0)" earmazene-o na variável "y".
y = fila.pop(0)

# 9. Imprima a variável "y".
print(f"Removidos na segunda remoção: {y}")

# 10. Adicione o elemento "40" à fila utilizando o método "append".
fila.append(40)

# 11. Imprima a fila utilizando o comando "print".
print(fila)
