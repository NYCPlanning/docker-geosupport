#!/bin/bash

function docker_tag_exists() {
    curl --silent -f -lSL https://index.docker.io/v1/repositories/$1/tags/$2 > /dev/null
}

VERSIONSTRING=$(python3 versions.py)
export $(echo "$VERSIONSTRING" | sed 's/#.*//g' | xargs)
export VERSION=$MAJOR.$MINOR.$PATCH

if docker_tag_exists nycplanning/docker-geosupport $VERSION; then
    echo "nycplanning/docker-geosupport:$VERSION already exist"
else 
    # State version name
    echo "$VERSIONSTRING"
    echo "$VERSION"

    # Log into Github registry
    echo "$GITHUB_TOKEN" | docker login docker.pkg.github.com -u $GITHUB_ACTOR --password-stdin
    
    # Build image
    docker build \
        --build-arg RELEASE=$RELEASE \
        --build-arg MAJOR=$MAJOR \
        --build-arg MINOR=$MINOR \
        --build-arg PATCH=$PATCH \
        --tag docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:${VERSION} .
    docker push docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:${VERSION}

    # Push image
    docker tag docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:${VERSION} \
        docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:latest
    docker push docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:latest

    # Log into Docker registry
    echo "$DOCKER_PASSWORD" | docker login -u $DOCKER_USER --password-stdin
    # Update Dockerhub
    docker tag docker.pkg.github.com/nycplanning/docker-geosupport/geosupport:${VERSION} \
        nycplanning/docker-geosupport:${VERSION}
    docker push nycplanning/docker-geosupport:${VERSION}
    docker tag nycplanning/docker-geosupport:${VERSION} nycplanning/docker-geosupport:latest
    docker push nycplanning/docker-geosupport:latest
fi