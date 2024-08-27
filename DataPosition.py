import requests
from API import API_KEY, API_URL

apikey = API_KEY
apiurl = API_URL

def getPositionsTeams(competitionId):
    url = f'{apiurl}/competitions/{competitionId}/standings'
    headers = {'X-Auth-Token': apikey}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    table_data = response.json() 
    print(f"A tabela da competição de ID {competitionId} é essa:")
    return table_data



def processTableData (table_data):
    extracted_data = []
    if 'standings' in table_data and len(table_data['standings']) > 0:
        for team_data in table_data['standings'][0]['table']:  
            teams_data = {
                "position": team_data["position"],
                "team_id": team_data["team"]["id"],
                "team_name": team_data["team"]["name"],
                "played_games": team_data["playedGames"],
                "won": team_data["won"],
                "draw": team_data["draw"],
                "lost": team_data["lost"],
                "points": team_data["points"],
                "goals_for": team_data["goalsFor"],
                "goals_against": team_data["goalsAgainst"],
                "goal_difference": team_data["goalDifference"],
                "form": team_data["form"]
            }
            extracted_data.append(teams_data)
    else:
        print("Não foi possível encontrar a chave 'standings' ou a tabela está vazia nos dados.")
    return extracted_data