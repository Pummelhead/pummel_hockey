import sqlite3
from teams import nhl_team_abbreviations

next_game = "next_game_date_time, next_game_opponent"
record = "record"
standing = "standing"

def query_team_overview(abbr, *args):
    columns = ", ".join(args)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    query = f"SELECT {columns} FROM all_teams_overview WHERE abbr = ?"
    items = cur.execute(query, (abbr,)).fetchall()
    for i in items:
         print(i)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    query_team_overview('EDM', next_game)
    query_team_overview('UTA', record, next_game, standing)
    #for abbr in nhl_team_abbreviations:
    #    query_team_overview(abbr, next_game)