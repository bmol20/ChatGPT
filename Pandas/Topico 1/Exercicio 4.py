import pandas as pd

dfA = pd.read_csv("df_Pandas.csv")

filtroDFA = dfA.loc[(dfA["IDADE"] > 30)]

print(filtroDFA)
