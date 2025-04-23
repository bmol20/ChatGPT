# Exercicio para utilizar um Dataset da internet no meu programa
# Utilizei um data base do site do governo com a localização de todos os CRAS do Rio de Janeiro

import pandas as pd

# Utilizei o comando encoding pois a biblioteca estava com problemas para reconhecer meu arquivo gerado no excel
dfA = pd.read_csv("CRAS_RJ.csv", encoding="ISO-8859-1")

# Utilizei esse comando pois o programa não tinha lido as vírgulas do meu csv direito
dfA = dfA["id_equipamento"].str.split(",", expand=True)

# Utilizei esse comando para corrigir a falta de nomes nas colunas gerada pelo uso do ultimo comando
dfA.columns = [
    "id_equipamento",
    "ibge",
    "uf",
    "cidade",
    "nome",
    "responsavel",
    "telefone",
    "endereco",
    "numero",
    "complemento",
    "referencia",
    "bairro",
    "cep",
    "georef_location",
    "data_atualizacao",
    "SLA",
    "SLA2",
    "SLA3",
]

# Utilizei o head() para apresentar apenas as primeiras linhas do meu csv
print(dfA.head())
