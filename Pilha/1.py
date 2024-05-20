# 1 - Crie uma pilha vazia e imprima uma mensagem indicando se ela está vazia ou não.
pilha = []

pilha.append(10)

if len(pilha) < 1:
    print(f"A lista está vazia")
else:
    print(f"A lista possui {len(pilha)} elementos.")
