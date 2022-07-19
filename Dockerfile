FROM python:3.9-slim

ARG RELEASE=21c
ARG MAJOR=21
ARG MINOR=3
ARG PATCH=0

RUN apt update && apt install -y curl git unzip zip build-essential

WORKDIR /geocode

COPY . . 

RUN FILE_NAME=linux_geo${RELEASE}_${MAJOR}_${MINOR}{PATCH}.zip\
    && echo $FILE_NAME\
    && curl -O https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/$FILE_NAME\
    && unzip *.zip\
    && rm *.zip

RUN ./patch.sh

ENV GEOFILES=/geocode/version-${RELEASE}_${MAJOR}.${MINOR}{PATCH}/fls/
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/geocode/version-${RELEASE}_${MAJOR}.${MINOR}{PATCH}/lib/

RUN pip install --upgrade pip \
    && pip install -e python-geosupport/.\
    && pip install -r requirements.txt

WORKDIR /