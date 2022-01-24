import pandas as pd

data = pd.read_csv('../data/teams.csv')
filtered = data[['Team', 'W', 'L', 'PW', 'PL', 'MOV', 'SOS', 'SRS', 'ORtg', 'DRtg', 'NRtg', 'Pace',
'FTr', '3PAr', 'TS%', "eFG%", 'TOV%', 'ORB%', "FT/FGA", "Arena", "Attend.", "Attend./G"]]

filtered.to_csv("../data/processed_teams.csv")