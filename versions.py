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

minior_lookup = {"a": 1, "b": 2, "c": 3, "d": 4}

if len(releases) > 1:
    # If more than 1 item in release
    # then there must be a UPAD present
    # Check if they are the same release
    r1 = releases[0][:3]
    r2 = releases[1].split(" ")[-1][:3]  # expecting strings like "upad / tpad  22c4'"
    print("what are releases", releases)
    print("what is r1", r1)
    print("what is r2", r2)

    if r1 != r2:
        release = releases[0]
    else:
        release = max(releases, key=len)
    print("chosen release", release)

    if len(release) == 4:
        versions = dict(
            RELEASE=release[:3],
            MAJOR=release[:2],
            MINOR=minior_lookup.get(release[2]),
            PATCH=release[3],
        )
    if len(release) == 3:
        versions = dict(
            RELEASE=release[:3],
            MAJOR=release[:2],
            MINOR=minior_lookup.get(release[2]),
            PATCH=0,
        )

    print(
        f"RELEASE={versions['RELEASE']} MAJOR={versions['MAJOR']} MINOR={versions['MINOR']} PATCH={versions['PATCH']}",
        file=sys.stdout,
    )
