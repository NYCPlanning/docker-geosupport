#!/bin/bash
if [[ ${UPAD} = 0 ]]
    then
        echo "NO UPAD AVAILABLE YET ..."
    else
        echo "YES UPAD IS AVAILABLE linux_upad_tpad_${RELEASE}${UPAD}"
        mkdir linux_upad_tpad_${RELEASE}${UPAD}\
        && curl -o linux_upad_tpad_${RELEASE}${UPAD}/linux_upad_tpad_${RELEASE}${UPAD}.zip https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/linux_upad_tpad_${RELEASE}${UPAD}.zip\
        && unzip -o linux_upad_tpad_${RELEASE}${UPAD}/*.zip -d version-${RELEASE}_${MAJOR}.${MINOR}/fls/\
        && rm -r linux_upad_tpad_${RELEASE}${UPAD}
    fi