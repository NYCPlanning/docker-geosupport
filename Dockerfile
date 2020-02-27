FROM continuumio/miniconda3:4.7.12

ARG RELEASE=20a
ARG MAJOR=20
ARG MINOR=1
ARG PATCH=0

ENV RELEASE=${RELEASE}
ENV MAJOR=${MAJOR}
ENV MINOR=${MINOR}
ENV PATCH=${PATCH}

RUN apt update\
    && apt install -y\
    curl git unzip\
    && apt autoclean

WORKDIR /geocode
COPY . . 

RUN FILE_NAME=linux_geo${RELEASE}_${MAJOR}_${MINOR}.zip\
    && echo $FILE_NAME\
    && curl -O https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/$FILE_NAME\
    && unzip *.zip\
    && rm *.zip

RUN ./patch.sh

ENV GEOFILES=/geocode/version-${RELEASE}_${MAJOR}.${MINOR}/fls/
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/geocode/version-${RELEASE}_${MAJOR}.${MINOR}/lib/

RUN conda install -c conda-forge gdal\
    conda clean
RUN pip install --upgrade pip\
    && pip install python-geosupport pandas sqlalchemy psycopg2-binary usaddress

WORKDIR /
