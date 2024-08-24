#Como usar Confrontos Direto

from ConfrontosDireto import find_head_to_head_between_teams, extract_teams_from_head_to_head

timeid1 = 524 #PSG
timeid2 = 86 #Real Madrid
BruteData = find_head_to_head_between_teams(timeid1, timeid2)

print (extract_teams_from_head_to_head(BruteData))