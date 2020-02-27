# docker-geosupport

## About: 
This is a repository for dockerized [geosupport](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page) linux desktop version. 
Thanks to [python-geosupport](https://github.com/ishiland/python-geosupport) python binding package for geosupport, we are able to localize our geocoding process. 

## Instructions: 
### Build on your own machine
1. Make sure you have docker installed
2. 
    ```
    RELEASE=20a
    MAJOR=20
    MINOR=1
    PATCH=0
    docker build --file Dockerfile \
            --build-arg RELEASE=$RELEASE \
            --build-arg MAJOR=$MAJOR \
            --build-arg MINOR=$MINOR \
            --build-arg PATCH=$PATCH \
            --tag sptkl/docker-geosupport:$MAJOR.$MINOR.$PATCH .
    ````
### Build through CI
1. make sure you include version specifications in commit message
    ```
    git commit -m 'RELEASE=20a MAJOR=20 MINOR=1 PATCH=0'
    ```
## Note: 
1. if there's no UPAD available, set PATCH=0. 
2. You can find Geosupport desktop edition and UPAD related information on [Bytes of the Big Apple](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page)
