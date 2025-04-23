import random

num = random.randint(1, 10)
tentativa = 3
i = 1

print("---Jogo da Sorte---")
print("\nVocê tem 3 chances para acertar um número de 1 a 10, BOA SORTE!!")

while 1:
    if tentativa == 0:
        print(
            "Infelizmente você perdeu, execute novamente o programa para tentar de novo!"
        )
        break

    escolha = int(input("Digite um número: "))

    if escolha == num:
        print("VOCÊ ACERTOU, MEUS PARABÉNS!!")
        tentativa = 0
        break

    elif escolha != num and escolha > 0 and escolha < 11:
        print("Você errou, tente novamente!")

        if escolha < num:
            print("É maior!")
        else:
            print("é menor")

        tentativa = tentativa - 1

    else:
        print("Valor incorreto, por favor, utilize apenas números de 1 a 10")
