from tkinter import *
from tkinter import ttk
import random


def main(): 
    # """Fornece os limites de um intervalo de números e deixa o usuário adivinhar o número do computador atéa suposição estar correta."""
    smaller = int(input("Entre com o número inicial: "))
    larger = int(input("Entre com o número final: "))
    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Digite seu palpite: "))
        if userNumber < myNumber:
            print("Muito pequeno…")
        elif userNumber > myNumber: 
            print("Muito grande!")
        else:
            print("Você acertou após", count, "tentativas!")
            break

if __name__ == "__main__":
    main()

janela = Tk()
janela.title("ADIVINHE OU SMT") # título da janela
janela.resizable(False, False)

frame = ttk.Frame(janela, padding="20 20 20 20") # padding: margem interna
frame.grid()

estilo = ttk.Style()
estilo.configure('my.TButton', font=('Arial', 18))

userNumber = StringVar() # variável string específica do tkinter
myNumber = StringVar() # variável string específica do tkinter


# criamos um Label para exibir ADIVINHE OU SMT
ttk.Label(frame, padding="10 10 10 10", font=("Arial", 18), text="ADIVINHE OU SMT")


# o campo de entrada é criada com largura para 10 caracteres (width)
# e seu conteúdo é vinculado à variável (textvariable) userNumber criada anteriormente
entrada = ttk.Entry(frame, width=10, textvariable=userNumber, font=("Arial", 18))
entrada.grid(column=1, row=0, padx=10, sticky=(N, W))


# botão que aciona a conversão, chamando a função main()
botao = ttk.Button(frame, padding="10 10 10 10", text="ADIVINHE OU SMT", style='my.TButton', command=main).grid(column=2, row=0)

# label para exibição do resultado (que será armazenado) pela função main
ttk.Label(frame, padding="10 10 10 10", textvariable=myNumber, font=("Arial", 18)).grid(column=1, row=1, sticky=(N, W))

# colocamos o cursos no campo de entrada
entrada.focus()

# associamos a tecla ENTER com a execução do jogo
janela.bind("<Return>", main)

# iniciamos o loop principal da inteface
janela.mainloop()
