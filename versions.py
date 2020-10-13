import requests
from bs4 import BeautifulSoup
import sys

url = "https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page"
soup = BeautifulSoup(requests.get(url).content, features="html.parser")
table = soup.find_all("table", class_="table table-outline-border")[0]
releases = [
    i.string.replace("Release", "").strip().lower()
    for i in table.find_all("th")
    if "Release" in i.string
]

minior_lookup = {
    'a': 1,
    'b': 2, 
    'c': 3,
    'd': 4
}

if len(releases) > 1:
    # If more than 1 item in release
    # then there must be a UPAD present
    release=max(releases, key=len)
    if len(release) == 4:
        versions = dict(
            RELEASE=release[:3],
            MAJOR=release[:2],
            MINOR=minior_lookup.get(release[2]),
            PATCH=release[3]
        )
    if len(release) == 3:
        versions = dict(
            RELEASE=release[:3],
            MAJOR=release[:2],
            MINOR=minior_lookup.get(release[2]),
            PATCH=0
        )
    
    print(f"RELEASE={versions['RELEASE']} MAJOR={versions['MAJOR']} MINOR={versions['MINOR']} PATCH={versions['PATCH']}", file=sys.stdout)
