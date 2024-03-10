# a. Quando um nome “vazio” for fornecido, pare de adicionar os nomes e exiba a lista.
# b. Em seguida, ordene a lista usando a função sort() do Python e, mais uma vez, exiba a
# lista (agora ordenada) na tela. ok
# c. Solicite então ao usuário um nome a ser buscado na lista. Realize uma busca binária
# pelo nome fornecido e, se encontrado, exiba na tela a posição do nome na lista.

def chamadaOrdenada():
    
    lista_chamada = []

    while True:
        aluno = input("Insira o nome do aluno (ou deixe em branco para sair): ")
        if aluno == "":
            break
        lista_chamada.append(aluno)


   