

# 2 - Crie uma pilha e empilhe os números 5, 10 e 15. Em seguida, desempilhe e imprima cada número

pilha = []

pilha.extend([5, 10, 15])

print(f"A pilha é: {pilha}")

while len(pilha) > 0:
    print(f"Removendo {pilha.pop(0)}")  
    
    print(f"A pilha agora é: {pilha}")
