import pandas as pd
import json

# Função para carregar dados de um arquivo JSON
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Carregar dados dos arquivos JSON
finished_matches = load_json('C:/Users/Gu_vi/OneDrive/Desktop/Projeto/ML-bets/jsons/FinishedMatches.json')
head_to_head = load_json('C:/Users/Gu_vi/OneDrive/Desktop/Projeto/ML-bets/jsons/HeadtoHead.json')
table_position_team = load_json('C:/Users/Gu_vi/OneDrive/Desktop/Projeto/ML-bets/jsons/tableProcessed.json')

# Verificar o tipo de dados carregados
print(type(finished_matches))  # Esperado: <class 'list'>

# Criar DataFrame a partir dos jogos finalizados
df_finished_matches = pd.DataFrame(finished_matches)  # Usar diretamente a lista de jogos

# Criar DataFrame a partir da tabela do campeonato
df_position_team = pd.DataFrame(table_position_team)

# Renomear colunas para diferenciar as informações de time da casa e de fora
df_home_team = df_position_team.rename(columns=lambda x: f'home_{x}')
df_away_team = df_position_team.rename(columns=lambda x: f'away_{x}')

# Ajustar colunas e renomear ID para juntar com os dados dos jogos
df_home_team = df_home_team.rename(columns={'home_team_id': 'team_id'})
df_away_team = df_away_team.rename(columns={'away_team_id': 'team_id'})

# Merge das informações de casa e fora com os jogos finalizados
df_merged = df_finished_matches.merge(df_home_team, left_on='home_team_id', right_on='team_id', how='left')
df_merged = df_merged.merge(df_away_team, left_on='away_team_id', right_on='team_id', how='left', suffixes=('_home', '_away'))

# Adicionar a variável target com base no resultado do jogo
df_merged['target'] = df_merged['winner'].apply(lambda x: 'win' if x == 'home_team' else ('lose' if x == 'away_team' else 'draw'))

# Reorganizar as colunas conforme necessário
columns = [
    'match_id', 'home_team', 'home_team_id', 'away_team', 'away_team_id', 'winner',
    'full_time_score.home', 'full_time_score.away', 'half_time_score.home', 'half_time_score.away',
    'competition', 'match_date', 'target',
    
    # Colunas do time da casa
    'home_team_name', 'home_position', 'home_played_games', 'home_won', 'home_draw', 'home_lost',
    'home_points', 'home_goals_for', 'home_goals_against', 'home_goal_difference',
    
    # Colunas do time de fora
    'away_team_name', 'away_position', 'away_played_games', 'away_won', 'away_draw', 'away_lost',
    'away_points', 'away_goals_for', 'away_goals_against', 'away_goal_difference'
]

# Verificar quais colunas estão presentes no DataFrame
missing_columns = [col for col in columns if col not in df_merged.columns]
if missing_columns:
    print("As seguintes colunas estão faltando no DataFrame:")
    print(missing_columns)

# Ajustar colunas para incluir apenas as disponíveis
columns = [col for col in columns if col in df_merged.columns]

df_final = df_merged[columns]

# Exibir o DataFrame resultante
print(df_final.head())

# Salvar o DataFrame final em um arquivo CSV
df_final.to_csv('final_data.csv', index=False)
