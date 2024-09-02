#Tutorial de uso do Data Position
import json
from DataPosition import getPositionsTeams, processTableData

competitionId = 'PD'

table = getPositionsTeams(competitionId)
tableProcessed = processTableData(table)

print(tableProcessed)


arquivo = 'tableProcessed.json'

# Salvar os dados processados em um arquivo JSON
with open(arquivo, 'w') as file:
    json.dump(tableProcessed, file, indent=4)