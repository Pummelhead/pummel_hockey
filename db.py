import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(f'''CREATE TABLE IF NOT EXISTS all_teams_info
            (
            abbr TEXT PRIMARY KEY,
            name TEXT,
            next_game_date_time TEXT,
            next_game_oponent TEXT,
            )''')