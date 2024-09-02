#Como usar Confrontos Direto

from HeadToHead import find_head_to_head_between_teams, extract_teams_from_head_to_head
import json

timeid1 = 524 #PSG
timeid2 = 86 #Real Madrid
BruteData = find_head_to_head_between_teams(timeid1, timeid2)

print (extract_teams_from_head_to_head(BruteData))

arquivo = 'HeadtoHead.json'

with open(arquivo, 'w') as file:
    json.dump(BruteData, file, indent=4)