#Código para gerar o Confronto Direto entre os times

import requests

# Configurações da API
API_URL = 'https://api.football-data.org/v4'
API_KEY = 'f816f15a4f814724adeb813ae587ee39'

# IDs dos times
team_ids = {
    'Arsenal FC': 57,
    'Aston Villa FC': 58,
    'Chelsea FC': 61,
    'Everton FC': 62,
    'Fulham FC': 63,
    'Liverpool FC': 64,
    'Manchester City FC': 65,
    'Manchester United FC': 66,
    'Newcastle United FC': 67,
    'Tottenham Hotspur FC': 73,
    'Wolverhampton Wanderers FC': 76,
    'Leicester City FC': 338,
    'Southampton FC': 340,
    'Ipswich Town FC': 349,
    'Nottingham Forest FC': 351,
    'Crystal Palace FC': 354,
    'Brighton & Hove Albion FC': 397,
    'Brentford FC': 402,
    'West Ham United FC': 563,
    'AFC Bournemouth': 1044,
    'Athletic Club': 77,
    'Club Atlético de Madrid': 78,
    'CA Osasuna': 79,
    'RCD Espanyol de Barcelona': 80,
    'FC Barcelona': 81,
    'Getafe CF': 82,
    'Real Madrid CF': 86,
    'Rayo Vallecano de Madrid': 87,
    'RCD Mallorca': 89,
    'Real Betis Balompié': 90,
    'Real Sociedad de Fútbol': 92,
    'Villarreal CF': 94,
    'Valencia CF': 95,
    'Real Valladolid CF': 250,
    'Deportivo Alavés': 263,
    'UD Las Palmas': 275,
    'Girona FC': 298,
    'RC Celta de Vigo': 558,
    'Sevilla FC': 559,
    'CD Leganés': 745,
    'FC Bayern München': 5,
    'Borussia Dortmund': 4,
    '1. FC Union Berlin': 28,
    'AC Milan': 98,
    'FC Internazionale Milano': 108,
    'SS Lazio': 110,
    'SSC Napoli': 113,
    'FC Porto': 503,
    'Paris Saint-Germain FC': 524,
    'Racing Club de Lens': 546,
    'Galatasaray SK': 610,
    'PSV': 674,
    'Feyenoord Rotterdam': 675,
    'RB Leipzig': 721,
    'Celtic FC': 732,
    'Royal Antwerp FC': 1864,
    'BSC Young Boys': 1871,
    'FC København': 1876,
    'FC Red Bull Salzburg': 1877,
    'FK Shakhtar Donetsk': 1887,
    'Sport Lisboa e Benfica': 1903,
    'Sporting Clube de Braga': 5613,
    'FK Crvena Zvezda': 7283
}

competitions = {
    'PL': 'Premier League',
    'PD': 'La Liga',
    'CL': 'Champions League',
}

def get_competition(season, competition_code):
    url = f'{API_URL}/competitions/{competition_code}/matches?season={season}'
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def find_head_to_head_matches(matches, team_id1, team_id2):
    return [
        match for match in matches
        if (match['homeTeam']['id'] == team_id1 and match['awayTeam']['id'] == team_id2) or
           (match['homeTeam']['id'] == team_id2 and match['awayTeam']['id'] == team_id1)
    ]

def get_head_to_head_details(match_id):
    url = f'{API_URL}/matches/{match_id}/head2head?limit=50'
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def find_head_to_head_between_teams(team_id1, team_id2):
    if team_id1 not in team_ids.values() or team_id2 not in team_ids.values():
        return "Um ou ambos os times não estão na lista."

    # Determinar as competições de cada time
    team1_competition = 'PL' if team_id1 in [
        57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 349, 351, 354, 397, 402, 563, 1044
    ] else 'PD'
    
    team2_competition = 'PL' if team_id2 in [
        57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 349, 351, 354, 397, 402, 563, 1044
    ] else 'PD'
    
    # Escolher a competição correta para a pesquisa
    if team1_competition == team2_competition:
        competition_code = team1_competition
    else:
        competition_code = 'CL'  # Se os times estão em competições diferentes, buscar na Champions League

    season = 2023  # Altere para o ano da temporada desejada
    
    # Buscar partidas da competição
    matches_data = get_competition(season, competition_code)
    matches = matches_data.get('matches', [])
    
    # Encontrar partidas entre os dois times
    head_to_head_matches = find_head_to_head_matches(matches, team_id1, team_id2)
    
    if not head_to_head_matches:
        return "Nenhum confronto direto encontrado entre os times."

    # Detalhes dos confrontos diretos
    head_to_head_details = []
    for match in head_to_head_matches:
        match_id = match['id']
        details = get_head_to_head_details(match_id)
        head_to_head_details.append(details)
    
    return head_to_head_details

# Exemplo de uso
team_id1 = 57  # Manchester City FC
team_id2 = 65  # Real Madrid CF
result = find_head_to_head_between_teams(team_id1, team_id2)
print(result)
