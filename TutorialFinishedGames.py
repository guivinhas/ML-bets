from FinishedGames import getFinishedGames, process_matches

teamId = 61


finished_games_from_team = getFinishedGames(teamId)
processed_matches = process_matches(finished_games_from_team["matches"])

# Exibindo os dados tratados
for match in processed_matches:
    print(f"Match ID: {match['match_id']}")
    print(f"Home Team: {match['home_team']} (ID: {match['home_team_id']})")
    print(f"Away Team: {match['away_team']} (ID: {match['away_team_id']})")
    print(f"Winner: {match['winner']}")
    print(f"Full Time Score: Home {match['full_time_score']['home']} - Away {match['full_time_score']['away']}")
    print(f"Half Time Score: Home {match['half_time_score']['home']} - Away {match['half_time_score']['away']}")
    print(f"Competition: {match['competition']}")
    print(f"Match Date: {match['match_date']}")
    print("-" * 30)