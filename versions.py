# Get the relevant release details from the Geosupport Open Data page
# and set an environment variable
import requests
from bs4 import BeautifulSoup
import os

IGNORE_UPAD_RELEASE = False  # TODO this is temporary while 2022 UPAD needs to be built

CALLER_ENVIRONMENT_VARIABLE_NAME = "VERSIONSTRING"
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

    if len(releases) == 1:
        # only one release section present
        # no UPAD to incorporate
        release = releases[0]
        versions = dict(
            RELEASE=release[:3],
            MAJOR=release[:2],
            MINOR=MINOR_LETTER_LOOKUP.get(release[2]),
            PATCH=0,
        )
    else:
        # If more than 1 item in release
        # then there must be a UPAD present
        # Check if they are the same release
        primary_release = releases[0]
        upad_release = releases[1].split(" ")[-1][:3]  # expecting "upad / tpad  22c4"
        upad_primary_release = upad_release[:2]
        print(f"{primary_release=}")
        print(f"{upad_release=}")

        if primary_release == upad_primary_release:
            print("Matching Primary and UPAD releases")
            # UPAD should be incorporated
            release = upad_release
        else:
            print("WARNING! Mismatch between posted Primary and UPAD releases")
            # posted UPAD is not meant for current release
            # TODO this is temporary while 2022 UPAD needs to be built
            if IGNORE_UPAD_RELEASE:
                print("Ignoring UPAD release")
                release = primary_release
            else:
                # build for the posted UPAD
                print("Prioritizing UPAD release")
                release = upad_release

        print(f"{release=}")
        if len(release) == 4:  # is a UPAD version
            versions = dict(
                RELEASE=release[:3],
                MAJOR=release[:2],
                MINOR=MINOR_LETTER_LOOKUP.get(release[2]),
                PATCH=release[3],
            )
        elif len(release) == 3:
            versions = dict(
                RELEASE=release[:3],
                MAJOR=release[:2],
                MINOR=MINOR_LETTER_LOOKUP.get(release[2]),
                PATCH=0,
            )
        else:
            raise ValueError(f"Got release string with unexpected length: {release=}")

    version_string = f"RELEASE={versions['RELEASE']} MAJOR={versions['MAJOR']} MINOR={versions['MINOR']} PATCH={versions['PATCH']}"
    os.environ[CALLER_ENVIRONMENT_VARIABLE_NAME] = version_string

    raise InterruptedError(f"DEBUG\n\t{version_string=}")
