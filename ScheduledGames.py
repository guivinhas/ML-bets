#Código para extrair os jogos futuros

import requests
from datetime import datetime
from API import API_KEY, API_URL

apikey = API_KEY
apiurl = API_URL

def getScheduledGames(teamId):
    url = f'{apiurl}/teams/{teamId}/matches?status=SCHEDULED'
    headers = {'X-Auth-Token': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    filtered_data = []
    for match in data['matches']:
        filtered_match = {
            'date': datetime.strptime(match['utcDate'], "%Y-%m-%dT%H:%M:%SZ").isoformat(),  # Convert to ISO format for JSON
            'home_team': match['homeTeam']['name'],
            'away_team': match['awayTeam']['name'],
            'competition': match['competition']['name']
        }
        filtered_data.append(filtered_match)

    return filtered_data
    # Exibindo os dados filtrados
    for match in filtered_data:
        print(f"Date: {match['date']}, Home Team: {match['home_team']}, Away Team: {match['away_team']}, Competition: {match['competition']}")

