# Exercicio para utilizar um Dataset da internet no meu programa
# Utilizei um csv contendo dados dos heróis da Marvel

import pandas as pd

# Utilizei o comando encoding pois a biblioteca estava com problemas para reconhecer meu arquivo gerado no excel
dfA = pd.read_csv("avengers.csv", encoding="ISO-8859-1")

# Utilizei o head() para apresentar apenas as primeiras linhas do meu csv
print(dfA.head())
