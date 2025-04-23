# Neste exercicio estou usando o mesmo csv para me gerar os dados que preciso do meu Dataframe

import pandas as pd

dfA = pd.read_csv("avengers.csv", encoding="ISO-8859-1")

# Nessa linha filtrei as colunas para informações que eu queria
dfA = dfA[["Name/Alias", "Appearances", "Gender"]]

# Comando para filtrar apenas os homens do meu dataframe
homens_dfA = dfA.loc[dfA["Gender"] == "MALE"]

# Calculo da média de aparições
mediaAparicoes = dfA["Appearances"].mean()

# Calculo da mediana de aparições
medianaAparicoes = dfA["Appearances"].median()

# Calculo do desvio padrão de aparições
desviopAparicoes = dfA["Appearances"].std()

print("Sua lista resumida com apenas 10 homens: ", homens_dfA.head(10))

print("\n\nA média de aparições dos heróis é: ", mediaAparicoes)

print("\n\nA mediana das aparições dos heróis é: ", medianaAparicoes)

print("\n\nO desvio padrão das aparições dos heróis é: ", desviopAparicoes)
