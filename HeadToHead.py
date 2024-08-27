import requests
from API import API_URL, API_KEY

apikey = API_KEY
apiurl = API_URL

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
    url = f'{apiurl}/competitions/{competition_code}/matches?season={season}'
    headers = {'X-Auth-Token': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"Retorno das partidas para a temporada {season} na competição {competitions.get(competition_code, 'Desconhecida')}: ")
    return data

def find_head_to_head_matches(matches, team_id1, team_id2):
    return [
        match for match in matches
        if (match['homeTeam']['id'] == team_id1 and match['awayTeam']['id'] == team_id2) or
           (match['homeTeam']['id'] == team_id2 and match['awayTeam']['id'] == team_id1)
    ]

def get_head_to_head_details(match_id):
    url = f'{apiurl}/matches/{match_id}/head2head?limit=100'
    headers = {'X-Auth-Token': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data

def find_head_to_head_between_teams(team_id1, team_id2):
    if team_id1 not in team_ids.values() or team_id2 not in team_ids.values():
        return "Um ou ambos os times não estão na lista."

    # Determinar as competições de cada time
    if team_id1 in [
        57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 349, 351, 354, 397, 402, 563, 1044
    ]:
        team1_competition = 'PL'
    elif team_id1 in [
       77, 78, 79, 80, 81, 82, 86, 87, 89, 90, 92, 94, 95,250, 263, 275, 298, 558, 559, 745
    ]:
        team1_competition = 'PD'
    else:
        team1_competition = 'CL'
    
    team2_competition = 'PL' if team_id2 in [
        57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 349, 351, 354, 397, 402, 563, 1044
    ] else 'PD'
    
    
    if team1_competition == team2_competition:
        competition_code = team1_competition
    else:
        competition_code = 'CL' 

    print(f"Competições selecionadas: Time 1 - {competitions.get(team1_competition, 'Desconhecida')}, Time 2 - {competitions.get(team2_competition, 'Desconhecida')}")
    
    start_season = 2020
    end_season = 2023

    for season in range(start_season, end_season + 1):
        print(f"Buscando partidas para a temporada {season} na competição {competition_code}...")
        # Buscar partidas da competição
        matches_data = get_competition(season, competition_code)
        matches = matches_data.get('matches', [])
    
        
        head_to_head_matches = find_head_to_head_matches(matches, team_id1, team_id2)
        
        if head_to_head_matches:
            print(f"Confrontos diretos encontrados!")
            break
    else:
        return "Nenhum confronto direto encontrado entre os times."

    
    head_to_head_details = []
    for match in head_to_head_matches:
        match_id = match['id']
        details = get_head_to_head_details(match_id)
        head_to_head_details.append(details)
    
    if isinstance(head_to_head_details, list):
        return head_to_head_details
    else:
        head_to_head_details = None
        return head_to_head_details

def extract_teams_from_head_to_head(head_to_head_details):
    
    teams_details = []

    if head_to_head_details and isinstance(head_to_head_details, list):
        
        for head_to_head_detail in head_to_head_details:
            aggregates = head_to_head_detail.get('aggregates', {})

            
            home_team = aggregates.get('homeTeam', {})
            home_team_details = {
                'id': home_team.get('id'),
                'name': home_team.get('name'),
                'wins': home_team.get('wins'),
                'draws': home_team.get('draws'),
                'losses': home_team.get('losses')
            }

            # Extraindo detalhes do time visitante
            away_team = aggregates.get('awayTeam', {})
            away_team_details = {
                'id': away_team.get('id'),
                'name': away_team.get('name'),
                'wins': away_team.get('wins'),
                'draws': away_team.get('draws'),
                'losses': away_team.get('losses')
            }

            # Adicionando os detalhes extraídos à lista
            teams_details.append({'homeTeam': home_team_details, 'awayTeam': away_team_details})
    else:
        print('Não foram encontrados jogos')
        return []

    return teams_details