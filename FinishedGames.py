import requests
from API import API_KEY, API_URL

apikey = API_KEY
apiurl = API_URL

def getFinishedGames(teamId):
    url = f'{apiurl}/teams/{teamId}/matches?status=FINISHED'
    headers = {'X-Auth-Token': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    matches_data = response.json()  # Isso deve retornar um dicionário completo
    print(f"Os jogos passados do time com ID {teamId} são esses")
    return matches_data

def process_matches(matches):
    processed_data = []
    
    for match in matches:
        match_info = {
            "match_id": match["id"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "winner": "Draw" if match["score"]["winner"] == "DRAW" else (match["homeTeam"]["name"] if match["score"]["winner"] == "HOME_TEAM" else match["awayTeam"]["name"]),
            "full_time_score": match["score"]["fullTime"],
            "half_time_score": match["score"]["halfTime"],
            "home_team_id": match["homeTeam"]["id"],
            "away_team_id": match["awayTeam"]["id"],
            "competition": match["competition"]["name"],
            "match_date": match["utcDate"]
        }
        processed_data.append(match_info)
    
    return processed_data