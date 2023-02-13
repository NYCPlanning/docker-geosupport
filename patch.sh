#!/bin/bash
if [[ ${PATCH} = 0 ]]
    then
        echo "NO UPAD AVAILABLE YET ..."
    else
        echo "YES UPAD IS AVAILABLE linux_upad_tpad_${RELEASE}${PATCH}"
        mkdir linux_upad_tpad_${RELEASE}${PATCH}\
        && curl -o linux_upad_tpad_${RELEASE}${PATCH}/linux_upad_tpad_${RELEASE}${PATCH}.zip https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/linux_upad_tpad_${RELEASE}${PATCH}.zip\
        && unzip -o linux_upad_tpad_${RELEASE}${PATCH}/*.zip -d version-${RELEASE}_${MAJOR}.${MINOR}/fls/\
        && rm -r linux_upad_tpad_${RELEASE}${PATCH}
    fi