# Get the relevant release details from the Geosupport Open Data page
# and set an environment variable
import requests
from bs4 import BeautifulSoup
import os

GEOSUPPORT_RELEASE_URL = (
    "https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page"
)
# to convert a release letter to a number for the docker image tag
MINOR_LETTER_LOOKUP = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

if __name__ == "__main__":
    soup = BeautifulSoup(
        requests.get(GEOSUPPORT_RELEASE_URL).content, features="html.parser"
    )
    table = soup.find_all("table", class_="table table-outline-border")[0]
    releases = [
        i.string.replace("Release", "").strip().lower()
        for i in table.find_all("th")
        if "Release" in i.string
    ]

    print(f"Release titles from Open Data table: {releases}")

    if len(releases) > 1:
        # If more than 1 item in release
        # then there must be a UPAD present
        # Check if they are the same release
        r1 = releases[0][2]
        r2 = releases[1][2]
        print(f"{r1=}")
        print(f"{r2=}")
        # r1 = releases[0][:3]
        # r2 = releases[1].split(" ")[-1][:3]  # expecting strings like "upad / tpad  22c4'"
        if r1 != r2:
            # posted UPAD is not meant for current release
            release = releases[0]
        else:
            # UPAD should be incorporated
            release = releases[1]
        print(f"{release=}")

        if len(release) == 4:
            versions = dict(
                RELEASE=release[:3],
                MAJOR=release[:2],
                MINOR=MINOR_LETTER_LOOKUP.get(release[2]),
                PATCH=release[3],
            )
        if len(release) == 3:
            versions = dict(
                RELEASE=release[:3],
                MAJOR=release[:2],
                MINOR=MINOR_LETTER_LOOKUP.get(release[2]),
                PATCH=0,
            )

        version_string = f"RELEASE={versions['RELEASE']} MAJOR={versions['MAJOR']} MINOR={versions['MINOR']} PATCH={versions['PATCH']}"
        os.environ["VERSIONSTRING"] = version_string
