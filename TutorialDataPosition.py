#Tutorial de uso do Data Position
from DataPosition import getPositionsTeams, processTableData

competitionId = 'PD'

table = getPositionsTeams(competitionId)
tableProcessed = processTableData(table)

print(tableProcessed)