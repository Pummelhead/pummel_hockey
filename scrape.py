from bs4 import BeautifulSoup
import requests
from teams import abbr_to_site, nhl_team_abbreviations
from threading import Thread
import sqlite3
import db

def scrape(abbr):
   page = requests.get(abbr_to_site(abbr))
   if page.status_code == 200:
      soup = BeautifulSoup(page.text, "html.parser")
      #record = " ".join(soup.find("aside", attrs={"class":"PageTitle-description"}).text.replace("\n","").split()).split('|')[0].strip()
      next_matchup_date = " ".join(soup.find("div", attrs={"class":"TeamMatchup-date"}).text.replace("\n","").split()).split('|')[0].strip()
      next_matchup_opponent = " ".join(soup.find("span", attrs={"class":"TeamName"}).text.replace("\n","").split()).split('|')[0].strip()
      conn = sqlite3.connect('database.db', check_same_thread=False)
      cur = conn.cursor()
      cur.execute(f"INSERT OR REPLACE INTO all_teams_overview (abbr, next_game_date_time, next_game_opponent) VALUES ('{abbr}', '{next_matchup_date}', '{next_matchup_opponent}')")
      conn.commit()
      conn.close()
      print("\033[92m" + f"{abbr} - record - {next_matchup_date} against {next_matchup_opponent}")
   else:
      print("\033[91m" + abbr)


if __name__ == "__main__":
   #for abbr in nhl_team_abbreviations:
   #   Thread(target=scrape, args=(abbr,)).start()
   for abbr in nhl_team_abbreviations:
      conn = sqlite3.connect('database.db')
      cur = conn.cursor()
      items = cur.execute(f"SELECT * FROM all_teams_overview WHERE abbr = '{abbr}'").fetchall()
      for i in items:
         print(i)
      conn.commit()
      conn.close()