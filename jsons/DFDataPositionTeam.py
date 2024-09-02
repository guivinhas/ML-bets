import pandas as pd
import json

# Caminho para o arquivo JSON
arquivo = 'C:/Users/Gu_vi/OneDrive/Desktop/Projeto/ML-bets/jsons/DataPositionTeam.json'


# Lendo o conteúdo do arquivo JSON
with open(arquivo, 'r') as file:
    data = json.load(file)

# Criando um DataFrame a partir dos dados JSON
df = pd.DataFrame([data])

# Exibindo o DataFrame
print(df)
