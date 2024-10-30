import sqlite3
from teams import nhl_team_abbreviations

full = "*"
next_game = "next_game_date_time, next_game_opponent"
division = "division"
record = "record"
standing = "standing"
number = "number"
name = "name"
position = "position"
injury = "injury"
goalies = "G"
centers = "C"
left_wingers = "LW"
right_wingers = "RW"
defensemen = "D"

def query_team_overview(abbr, *args):
    columns = ", ".join(args)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    query = f"SELECT {columns} FROM all_teams_overview WHERE abbr = ?"
    items = cur.execute(query, (abbr,)).fetchall()
    print(abbr)
    for i in items:
         print(i)
    conn.commit()
    conn.close()

def query_team_roster(abbr, *args):
    columns = ", ".join(args)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    query = f"SELECT {columns} FROM {abbr}_roster"
    items = cur.execute(query).fetchall()
    print(abbr)
    for i in items:
         print(i)
    conn.commit()
    conn.close()
    
def query_team_positions(abbr, *positions, **kwargs):
    conn = sqlite3.connect('database.db')
    if kwargs:
        columns = kwargs.get("columns", "*")
    else:
        columns = full
    placeholders = ', '.join('?' for _ in positions)
    cur = conn.cursor()
    query = f"SELECT {columns} FROM {abbr}_roster WHERE position IN ({placeholders})"
    items = cur.execute(query, positions).fetchall()
    print(abbr)
    for i in items:
         print(i)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    query_team_overview('EDM', next_game, record, standing, division)
    query_team_overview('UTA', record, next_game, standing)
    query_team_roster('CHI', number, name, position)
    #query_team_positions('EDM', 'C', number, name)
    query_team_positions('UTA', 'G', number, name)
    #query_team_positions('VGK', 'D', number, name)
    #query_team_positions('CHI', left_wingers, defensemen, columns="number, name, injury")