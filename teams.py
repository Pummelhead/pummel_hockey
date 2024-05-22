

nhl_team_abbreviations = [
    "ANA",  # Anaheim Ducks
    "ARI",  # Arizona Coyotes
    "BOS",  # Boston Bruins
    "BUF",  # Buffalo Sabres
    "CGY",  # Calgary Flames
    "CAR",  # Carolina Hurricanes
    "CHI",  # Chicago Blackhawks
    "COL",  # Colorado Avalanche
    "CBJ",  # Columbus Blue Jackets
    "DAL",  # Dallas Stars
    "DET",  # Detroit Red Wings
    "EDM",  # Edmonton Oilers
    "FLA",  # Florida Panthers
    "LAK",  # Los Angeles Kings
    "MIN",  # Minnesota Wild
    "MTL",  # Montreal Canadiens
    "NSH",  # Nashville Predators
    "NJD",  # New Jersey Devils
    "NYI",  # New York Islanders
    "NYR",  # New York Rangers
    "OTT",  # Ottawa Senators
    "PHI",  # Philadelphia Flyers
    "PIT",  # Pittsburgh Penguins
    "SEA",  # Seattle Kraken
    "SJS",  # San Jose Sharks
    "STL",  # St. Louis Blues
    "TBL",  # Tampa Bay Lightning
    "TOR",  # Toronto Maple Leafs
    "VAN",  # Vancouver Canucks
    "VGK",  # Vegas Golden Knights
    "WSH",  # Washington Capitals
    "WPG"   # Winnipeg Jets
]

nhl_teams_dict = {
    "ANA": "Anaheim Ducks",
    "ARI": "Arizona Coyotes",
    "BOS": "Boston Bruins",
    "BUF": "Buffalo Sabres",
    "CGY": "Calgary Flames",
    "CAR": "Carolina Hurricanes",
    "CHI": "Chicago Blackhawks",
    "COL": "Colorado Avalanche",
    "CBJ": "Columbus Blue Jackets",
    "DAL": "Dallas Stars",
    "DET": "Detroit Red Wings",
    "EDM": "Edmonton Oilers",
    "FLA": "Florida Panthers",
    "LAK": "Los Angeles Kings",
    "MIN": "Minnesota Wild",
    "MTL": "Montreal Canadiens",
    "NSH": "Nashville Predators",
    "NJD": "New Jersey Devils",
    "NYI": "New York Islanders",
    "NYR": "New York Rangers",
    "OTT": "Ottawa Senators",
    "PHI": "Philadelphia Flyers",
    "PIT": "Pittsburgh Penguins",
    "SEA": "Seattle Kraken",
    "SJS": "San Jose Sharks",
    "STL": "St Louis Blues",
    "TBL": "Tampa Bay Lightning",
    "TOR": "Toronto Maple Leafs",
    "VAN": "Vancouver Canucks",
    "VGK": "Vegas Golden Knights",
    "WSH": "Washington Capitals",
    "WPG": "Winnipeg Jets"
}

nhl_teams_tree = {
    "Eastern": {
        "Atlantic": {
            "BOS": "Boston Bruins",
            "BUF": "Buffalo Sabres",
            "DET": "Detroit Red Wings",
            "FLA": "Florida Panthers",
            "MTL": "Montreal Canadiens",
            "OTT": "Ottawa Senators",
            "TBL": "Tampa Bay Lightning",
            "TOR": "Toronto Maple Leafs"
        },
        "Metropolitan": {
            "CAR": "Carolina Hurricanes",
            "CBJ": "Columbus Blue Jackets",
            "NJD": "New Jersey Devils",
            "NYI": "New York Islanders",
            "NYR": "New York Rangers",
            "PHI": "Philadelphia Flyers",
            "PIT": "Pittsburgh Penguins",
            "WSH": "Washington Capitals"
        }
    },
    "Western": {
        "Central": {
            "ARI": "Arizona Coyotes",
            "CHI": "Chicago Blackhawks",
            "COL": "Colorado Avalanche",
            "DAL": "Dallas Stars",
            "MIN": "Minnesota Wild",
            "NSH": "Nashville Predators",
            "STL": "St Louis Blues",
            "WPG": "Winnipeg Jets"
        },
        "Pacific": {
            "ANA": "Anaheim Ducks",
            "CGY": "Calgary Flames",
            "EDM": "Edmonton Oilers",
            "LAK": "Los Angeles Kings",
            "SJS": "San Jose Sharks",
            "SEA": "Seattle Kraken",
            "VAN": "Vancouver Canucks",
            "VGK": "Vegas Golden Knights"
        }
    }
}

nhl_teams_web_prefix = {
    "ANA": "ANA",
    "ARI": "ARI",
    "BOS": "BOS",
    "BUF": "BUF",
    "CGY": "CGY",
    "CAR": "CAR",
    "CHI": "CHI",
    "COL": "COL",
    "CBJ": "CLB",
    "DAL": "DAL",
    "DET": "DET",
    "EDM": "EDM",
    "FLA": "FLA",
    "LAK": "LA",
    "MIN": "MIN",
    "MTL": "MON",
    "NSH": "NSH",
    "NJD": "NJ",
    "NYI": "NYI",
    "NYR": "NYR",
    "OTT": "OTT",
    "PHI": "PHI",
    "PIT": "PIT",
    "SEA": "SEA",
    "SJS": "SJ",
    "STL": "STL",
    "TBL": "TB",
    "TOR": "TOR",
    "VAN": "VAN",
    "VGK": "LV",
    "WSH": "WAS",
    "WPG": "WPG"
}

def abbr_to_site(abbr):
    return f"https://www.cbssports.com/nhl/teams/{nhl_teams_web_prefix[abbr]}/{nhl_teams_dict[abbr].replace(" ", "-").lower()}"

if __name__ == "__main__":
    print(abbr_to_site("VGK"))
    print(abbr_to_site("EDM"))