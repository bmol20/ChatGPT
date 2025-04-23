import pandas as pd

# Nesse exercicio eu devo usar o mesmo Dataframe criado no exercicio anterior
# E fazer com que o programa imprima algumas coisas especificas

# Comando para ler o dataframe gerado no outro exercicio
dfA = pd.read_csv("df_Pandas.csv")

# Nessa linha eu criei uma variável para armazenar o comando de busca do nome "João"
joao = dfA.loc[dfA["NOME"] == "João"]

print(dfA, "\n\n")

# Nessa linha eu solicitei que ele imprimisse os valores que estavam
# Na primeira linha, que dentro da biblioteca corresponde ao valor 0
print("A primeira linha é:\n", dfA.iloc[0])

# Nessa linha eu solicitei para que imprimisse apenas a coluna "Idade"
print("\nA segunda linha é:\n", dfA[["IDADE"]])

# Nessa linha eu pedi para que ele buscasse o nome "João"
# E me retornasse as informações dele
print("\nA terceira linha é:\n", joao)
