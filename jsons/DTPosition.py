import json
import pandas as pd

# Função para carregar o JSON
def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Função para filtrar times pelo ID
def filter_teams_by_id(data, team_ids):
    filtered_teams = [team for team in data if team['team_id'] in team_ids]
    return filtered_teams

# Carregar os dados do JSON
filename = 'C:/Users/Gu_vi/OneDrive/Desktop/Projeto/ML-bets/jsons/tableProcessed.json'  # Altere conforme o nome do arquivo JSON
data = load_json(filename)

# Solicitar ao usuário os IDs dos times
team_ids_input = input("Digite os IDs dos times separados por vírgula: ")
team_ids = [int(id.strip()) for id in team_ids_input.split(',')]

# Filtrar os times
filtered_teams = filter_teams_by_id(data, team_ids)

# Criar o DataFrame
df = pd.DataFrame(filtered_teams)

# Exibir o DataFrame
print(df)