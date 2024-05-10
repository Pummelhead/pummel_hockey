from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.cbssports.com/nhl/teams/EDM/edmonton-oilers/')
soup = BeautifulSoup(page.text, "html.parser")

next_matchup_date = soup.find_all("div", attrs={"class":"CellGame"})
grab_table = soup.find_all("h4", attrs={"class":"TableBase-title"})
for table in grab_table:
   print(table.text.replace("\n", "").strip())
   if table.text.replace("\n", "").strip() == "Schedule":
      schedule = table.find_next_sibling('div')
      next_matchup_team = schedule.find_all("span", attrs={"class":"CellLogoNameLockup"})



if __name__ == "__main__":
    #for a in grab_table:
    #    print(a.text.replace("\n", " ").strip())
    print(next_matchup_team)
    #for a, b in zip(next_matchup_team, next_matchup_date):
    #    print(a.text.replace('\n',' ').strip(), b.text.replace('\n',' ').strip())
