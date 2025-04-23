# Exercicio proposto para me ensinar a criar um Dataframe usando a biblioteca pandas

import pandas as pd

dA = {
    "NOME": ["Bruno", "João", "Gabi"],
    "IDADE": [21, 33, 22],
    "CIDADE": ["P. de Lucas", "Caxias", "25 de Agosto"],
}

dfA = pd.DataFrame(data=dA)

# Nessa linha instrui o programa a salva a minha lista em .csv
# Para poder acessar a mesma lista em outros programas
dfA.to_csv("df_Pandas.csv")

print(dfA)
