#Tutorial de uso de Jogos futuros

from ScheduledGames import getScheduledGames
import json

teamId = 86

scheduledgamesfromteam = getScheduledGames(teamId)
print(scheduledgamesfromteam)

 # Salvando os dados em um arquivo JSON
arquivo = 'ScheduledGames.json'

with open(arquivo, 'w') as file:
    json.dump(scheduledgamesfromteam, file, indent=4)