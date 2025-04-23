idade = int(input("Digite sua idade: "))

if idade > 18 and idade < 65:
    print("Você é Adulto")
elif idade > 65:
    print("Você é velho!")
elif idade < 18 and idade >= 0:
    print("Você é menor de idade!")
else:
    print("VAI A MERDA!")
