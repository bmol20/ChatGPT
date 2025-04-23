import os


def media(a, b):
    c = sum(a) / b
    return c


tam = 0
varMedia = []

while 1:
    os.system("cls")

    print("---- MÉDIA ----")
    print(
        "\n\nDigite os valores que deseja fazer a média ou digite 0 para encerrar a contagem"
    )

    num = int(input("\n\nDigite aqui: "))

    if num == 0:
        break
    else:
        varMedia.append(num)
        tam = tam + 1

resultado = media(varMedia, tam)

print("A média dos valores que você digitou é: ", resultado)
