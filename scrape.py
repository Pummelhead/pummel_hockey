from bs4 import BeautifulSoup
import requests
from teams import abbr_to_site, nhl_team_abbreviations
from concurrent.futures import ThreadPoolExecutor

def scrape(abbr):
   page = requests.get(abbr_to_site(abbr))
   soup = BeautifulSoup(page.text, "html.parser")

   next_matchup_date = " ".join(soup.find("div", attrs={"class":"TeamMatchup-date"}).text.replace("\n","").split())
   return abbr, next_matchup_date


if __name__ == "__main__":
   with ThreadPoolExecutor(max_workers=32) as executor:
      futures = [executor.submit(scrape, abbr) for abbr in nhl_team_abbreviations]

      for future in futures:
         response = future.result()
         print(response)