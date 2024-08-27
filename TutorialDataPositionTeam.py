#Tutorial de uso do Data Position Team que serve para saber os dados de 1 único time
from DataPosition import getPositionsTeams, processTableData

competitionId = ''
teamId = 86

if teamId in [
        57, 58, 61, 62, 63, 64, 65, 66, 67, 73, 76, 338, 340, 349, 351, 354, 397, 402, 563, 1044
    ]:
        competitionId = 'PL'
elif teamId in [
       77, 78, 79, 80, 81, 82, 86, 87, 89, 90, 92, 94, 95,250, 263, 275, 298, 558, 559, 745
    ]:
        competitionId = 'PD'    
else:
        competitionId = 'CL'

table = getPositionsTeams(competitionId)
tableProcessed = processTableData(table)



for team in tableProcessed:
    if team['team_id'] == teamId:
        team_data = {
            "ID" : team['team_id'],
            "Team Name": team['team_name'],
            "Position": team['position'],
            "Played Games" :team['played_games'],
            "Won" :team['won'],
            "Draw" :team['draw'],
            "Lost" :team['lost'],
            "Points" :team['points'],
            "Goals for" :team['goals_for'],
            "Goals against" :team['goals_against'],
            "Goals difference" :team['goal_difference'],
            "form" :team['form']
        }
        if team_data["ID"] == teamId:
            print(f"para o Time {team['team_name']}")
            print(team_data)
        else:
            ...
        break
    else:
        ...