from bs4 import BeautifulSoup
import requests
from teams import abbr_to_site, abbr_to_site_roster, nhl_team_abbreviations
from threading import Thread
import sqlite3
import db

def scrape(abbr):
   page = requests.get(abbr_to_site(abbr))
   if page.status_code == 200:
      soup = BeautifulSoup(page.text, "html.parser")
      try:
         record = " ".join(soup.find("aside", attrs={"class":"PageTitle-description"}).text.replace("\n","").split()).split('|')[0].strip()
      except:
         record = "0-0-0"
      next_matchup_date = " ".join(soup.find("div", attrs={"class":"TeamMatchup-date"}).text.replace("\n","").split()).split('|')[0].strip()
      next_matchup_opponent = " ".join(soup.find("span", attrs={"class":"TeamName"}).text.replace("\n","").split()).split('|')[0].strip()
      conn = sqlite3.connect('database.db', check_same_thread=False)
      cur = conn.cursor()
      query = f"INSERT OR REPLACE INTO all_teams_overview (abbr, record, next_game_date_time, next_game_opponent) VALUES (?, ?, ?, ?)"
      cur.execute(query, (abbr, record, next_matchup_date, next_matchup_opponent)).fetchall()
      conn.commit()
      conn.close()
      print("\033[92m" + f"{abbr} scraped")
   else:
      print("\033[91m" + f"{abbr} could not be scraped")

def scrape_roster(abbr):
   page = requests.get(abbr_to_site_roster(abbr))
   if page.status_code == 200:
      soup = BeautifulSoup(page.text, "html.parser")
      roster = soup.find_all("tr", attrs={"class":"TableBase-bodyTr"})
      for player in roster:
         tds = player.find_all("td", attrs={"class":"TableBase-bodyTd"})
         number = tds[0].text.strip()
         names = tds[1].find_all("a", attrs={"class": ""})
         name = names[1].text
         position = tds[2].text.strip()
         try:
            injury_icon = tds[1].find("span", attrs={"class": "CellPlayerName-icon icon-moon-injury"})
            injury = injury_icon.find("div", attrs={"class": "Tablebase-tooltipInner"}).text.strip()
         except:
            injury = "Healthy"
         conn = sqlite3.connect('database.db', check_same_thread=False)
         cur = conn.cursor()
         query = f"INSERT OR REPLACE INTO {abbr}_roster (number, name, position, injury) VALUES (?, ?, ?, ?)"
         cur.execute(query, (number, name, position, injury)).fetchall()
         conn.commit()
         conn.close()
      print("\033[92m" + f"{abbr} roster scraped")
   else:
      print("\033[91m" + f"{abbr} roster could not be scraped")


if __name__ == "__main__":
   threads = []
   #for abbr in nhl_team_abbreviations:
   #   t1 = Thread(target=scrape, args=(abbr,))
   #   t1.start()
   #   threads.append(t1)
   #for t in threads:
   #   t.join()
   #threads.clear()
   for abbr in nhl_team_abbreviations:
      t2 = Thread(target=scrape_roster, args=(abbr,))
      t2.start()
      threads.append(t2)
   for t in threads:
      t.join()