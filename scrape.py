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
      standing_titles = soup.find_all("div", attrs={"class":"GlobalSubnav_overviewItemTitle__oCNrO"})
      division = standing_titles[1].text.strip()
      standing_values = soup.find_all("div", attrs={"class":"GlobalSubnav_overviewItemValue__byIm_"})
      record = standing_values[0].text.strip()
      standing = standing_values[1].text.strip()
      next_matchup_date = " ".join(soup.find("div", attrs={"class":"TeamMatchup-date"}).text.replace("\n","").split()).split('|')[0].strip()
      next_matchup_opponent = " ".join(soup.find("span", attrs={"class":"TeamName"}).text.replace("\n","").split()).split('|')[0].strip()
      conn = sqlite3.connect('database.db', check_same_thread=False)
      cur = conn.cursor()
      query = f"INSERT OR REPLACE INTO all_teams_overview (abbr, division, record, standing, next_game_date_time, next_game_opponent) VALUES (?, ?, ?, ?, ?, ?)"
      cur.execute(query, (abbr, division, record, standing, next_matchup_date, next_matchup_opponent)).fetchall()
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
         player_page_link = names[1]["href"]
         name = names[1].text
         position = tds[2].text.strip()
         player_page = requests.get("https://www.cbssports.com" + player_page_link)
         print(player_page_link)
         if player_page.status_code == 200:
            player_soup = BeautifulSoup(player_page.text, "html.parser")
            player_page_main_column = player_soup.find("div", attrs={"class": "Page-colMain"})
            player_stat_table = player_page_main_column.find("table", attrs={"class": "TableBase-table"})
            print(player_stat_table)
            player_stats = player_stat_table.find_all("td", attrs={"class": "TableBase-bodyTd TableBase-bodyTd--number"})
            print(player_stats)
            assists = int(player_stats[0].text.strip())
            print(assists)
            points = int(player_stats[1].text.strip())
            print(points)
            plus_minus = int(player_stats[2].text.strip())
            print(plus_minus)
            goals = points - assists
         else:
            print("\033[91m" + f"{name} individual stats could not be scraped")
         try:
            injury_icon = tds[1].find("span", attrs={"class": "CellPlayerName-icon icon-moon-injury"})
            injury = injury_icon.find("div", attrs={"class": "Tablebase-tooltipInner"}).text.strip()
         except:
            injury = "Healthy"
         conn = sqlite3.connect('database.db', check_same_thread=False)
         cur = conn.cursor()
         query = f"INSERT OR REPLACE INTO {abbr}_roster (number, name, position, injury, goals, assists, points, plus_minus) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
         cur.execute(query, (number, name, position, injury, goals, assists, points, plus_minus)).fetchall()
         conn.commit()
         conn.close()
      print("\033[92m" + f"{abbr} roster scraped")
   else:
      print("\033[91m" + f"{abbr} roster could not be scraped")


if __name__ == "__main__":
   #threads = []
   #for abbr in nhl_team_abbreviations:
   #   t1 = Thread(target=scrape, args=(abbr,))
   #   t1.start()
   #   threads.append(t1)
   #for t in threads:
   #   t.join()
   #threads.clear()
   #for abbr in nhl_team_abbreviations:
   #   t2 = Thread(target=scrape_roster, args=(abbr,))
   #   t2.start()
   #   threads.append(t2)
   #for t in threads:
   #   t.join()
   scrape_roster("UTA")