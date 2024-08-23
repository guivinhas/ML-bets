import requests
import pandas as pd

# Sua chave de API
api_token = 'f816f15a4f814724adeb813ae587ee39'
headers = {
    'X-Auth-Token': api_token
}

# URLs das competições
competitions = {
    'CL': 'https://api.football-data.org/v4/competitions/CL/teams?season=2023'   # Champions League
}

# Lista para armazenar os dados
teams_data = []

for competition, url in competitions.items():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams = response.json().get('teams', [])
        for team in teams:
            teams_data.append({
                'Competition': competition,
                'Team Name': team['name'],
                'Team ID': team['id']
            })
    else:
        print(f'Erro ao acessar os dados da competição {competition}: {response.status_code}')

# Criando um DataFrame
df = pd.DataFrame(teams_data)

# Salvando em um arquivo Excel
df.to_excel('teams_CL.xlsx', index=False)

print('Arquivo Excel gerado com sucesso: team_ids.xlsx')
