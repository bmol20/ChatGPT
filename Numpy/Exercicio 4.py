import numpy as np

arrayA = np.arange(1, 11)

for num in arrayA:
    if (num % 2) == 0:
        print(num)

media = np.mean(arrayA)

mediana = np.median(arrayA)

desvioP = np.std(arrayA)

print("Sua média é:", media)

print("Sua mediana é:", mediana)

print("Seu desvio padrão é:", desvioP)
