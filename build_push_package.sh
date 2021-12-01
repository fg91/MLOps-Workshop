#!/bin/bash

REGISTRY="localhost:5000"
APP_NAME="workflow"
MODULE="flytesnacks.workflows"
VERSION=$(git rev-parse HEAD)-${RANDOM}

TAG=$REGISTRY/${APP_NAME}:${VERSION}-${RANDOM}

docker build --tag ${TAG} .
docker push ${TAG}

pyflyte --pkgs ${MODULE} package --image k3d-registry.${TAG} -f

echo "Docker image ${TAG} built and module ${MODULE} packaged with pyflyte"
