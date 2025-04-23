import pandas
import numpy as np

# Como não teve um contexto para criação do exemplo, criei uma tabela de vizualização de quilometragem por veículo bem simples

dA = {
    "placa": [
        "LRB",
        "LUL",
        "PUN",
    ],
    "km": [97, 22, 86],
}
dfA = pandas.DataFrame(data=dA)

arrayA = dfA.to_numpy()

dB = np.array([["placa", "Km"], ["LRB", 97], ["LUL", 22], ["PUN", 85]])

dfB = pandas.DataFrame(data=dB[1:], columns=dB[0])

print("O valor convertido de Dataframe para Numpy é:\n", dfA)
print("O valor convertido de Numpy para Dataframe é:\n", dfB)
