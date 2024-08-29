import sqlite3
from teams import nhl_team_abbreviations

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(f'''CREATE TABLE IF NOT EXISTS all_teams_overview
            (
            abbr TEXT PRIMARY KEY,
            name TEXT,
            division TEXT,
            record TEXT,
            standing TEXT,
            next_game_date_time TEXT,
            next_game_opponent TEXT
            )''')

for team in nhl_team_abbreviations:
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {team}_roster
                (
                number INTEGERT,
                name TEXT,
                position TEXT,
                goals INTEGER,
                assists INTEGER,
                points INTEGER,
                plus_minus INTEGER,
                injury TEXT,
                PRIMARY KEY(number, name)
                )''')

conn.commit()
conn.close()