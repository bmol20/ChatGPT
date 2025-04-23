# Neste exercicio pratiquei como adicionar uma nova coluna ao meu CSV

import pandas as pd

dfA = pd.read_csv("df_Pandas.csv")

# Para adicionar eu preciso criar um array simples
Profissao = ["Engenheiro", "Mecanico", "Nutricionista"]

# E agora eu inseri o meu novo array no meu Dataframe
dfA["PROFISSÃO"] = Profissao

# Salvei esse CSV em arquivos diferentes para eu achar as versões dele depois
dfA.to_csv("df_Pandas(Profissao).csv")

print(dfA)
