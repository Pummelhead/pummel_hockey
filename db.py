import sqlite3
from teams import nhl_team_abbreviations

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(f'''CREATE TABLE IF NOT EXISTS all_teams_overview
            (
            abbr TEXT PRIMARY KEY,
            name TEXT,
            record TEXT,
            standing TEXT,
            next_game_date_time TEXT,
            next_game_oponent TEXT
            )''')

for team in nhl_team_abbreviations:
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {team}_roster
                (
                number INTEGERT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                position TEXT,
                goals INTEGER,
                assists INTEGER,
                points INTEGER,
                plus_minus INTEGER,
                injured BOOLEAN
                )''')