# docker-geosupport
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/NYCPlanning/docker-geosupport) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/NYCPlanning/docker-geosupport/Create%20geosupport%20docker%20image)

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
    PATCH=2
    docker build --file Dockerfile \
            --build-arg RELEASE=$RELEASE \
            --build-arg MAJOR=$MAJOR \
            --build-arg MINOR=$MINOR \
            --build-arg PATCH=$PATCH \
            --tag sptkl/docker-geosupport:$MAJOR.$MINOR.$PATCH .
    ```
### Build through CI
1. make sure you include version specifications in commit message
    ```
    git commit -m 'RELEASE=20a MAJOR=20 MINOR=1 PATCH=0'
    ```
## Note: 
1. if there's no UPAD available, set PATCH=0. 
2. You can find Geosupport desktop edition and UPAD related information on [Bytes of the Big Apple](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page)

## Build log
### 2020/03/10
    RELEASE=20a MAJOR=20 MINOR=1 PATCH=1


## Try it now!

Fire up an geosupport api on [Heroku](https://www.heroku.com/) with a single click:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Instructions
1. Using Docker:
    if you like to specify your own port:
    ```
    docker run -d -e PORT={YOUR_PORT} -p {YOUR_PORT}:{YOUR_PORT} sptkl/api-geosupport:latest
    ```
    if no port specified, by default, the flask app will run on 5000:
    ```
    docker run -d -p 5000:5000 sptkl/api-geosupport:latest
    ```
2. Examples: 
    + Geocode using borough: 
        ```
        http://0.0.0.0:5000/geocode/1b?house_number=120&street_name=broadway&borough=MN
        ```
    + Goecode using zipcode: 
        ```
        http://0.0.0.0:5000/geocode/1b?house_number=120&street_name=broadway&zip_code=10271
        ```
    + Get address suggestions with minimal input: 
        ```
        http://0.0.0.0:5000/suggest?address=100 Gold
        ```
3. Notes:
    + All Geosupport functions and parameters are supported. 

4. Next Steps:
    + write tests
    + figure out a better way to structure code