from bs4 import BeautifulSoup
import requests
from teams import abbr_to_site, nhl_team_abbreviations
from threading import Thread

def scrape(abbr):
   page = requests.get(abbr_to_site(abbr))
   if page.status_code == 200:
      soup = BeautifulSoup(page.text, "html.parser")
      next_matchup_date = " ".join(soup.find("div", attrs={"class":"TeamMatchup-date"}).text.replace("\n","").split()).split('|')[0].strip()
      print("\033[92m" + f"{abbr} - {next_matchup_date}")
   else:
      print("\033[91m" + abbr)


if __name__ == "__main__":
   for abbr in nhl_team_abbreviations:
      Thread(target=scrape, args=(abbr,)).start()