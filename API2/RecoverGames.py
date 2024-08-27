import requests

apiurl = 'https://v3.football.api-sports.io'
apikey = '3517d77c47bf179114ced99abc7b9a1c'
teamId = 50  # ID do Manchester City
league = 39  # Premier League

def getGames(league):
    url = f'{apiurl}/fixtures?league={league}&season=2024'
    print(f"URL: {url}")
    headers = {'x-apisports-key': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    recover = response.json()  # Converte a resposta em um dicionário
    print(f"Os jogos recuperados são esses:")
    return recover

def getRecoverGames(teamId, recover):
    recovered_games = []  # Lista para armazenar os jogos recuperados

    # Acessa a lista de partidas dentro da chave 'response'
    for match in recover['response']:
        if match['teams']['home']['id'] == teamId or match['teams']['away']['id'] == teamId:
            fixtureInfo = {
                "fixture_id": match['fixture']['id'],
                "date": match['fixture']['date'],
                "venue": match['fixture']['venue']['name'],
                "city": match['fixture']['venue']['city'],
                "home_team": match['teams']['home']['name'],
                "away_team": match['teams']['away']['name'],
                "home_score": match['goals']['home'],
                "away_score": match['goals']['away'],
                "status": match['fixture']['status']['long']
            }
            recovered_games.append(fixtureInfo)  # Adiciona o jogo à lista
    
    return recovered_games

# Executa as funções
a = getGames(league)
b = getRecoverGames(teamId, a)

# Imprime os jogos recuperados
for game in b:
    print(game)
