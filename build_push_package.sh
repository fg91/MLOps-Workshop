#!/bin/bash

REGISTRY="localhost:5000"
APP_NAME="workflow"
VERSION=$(git rev-parse HEAD)-${RANDOM}

TAG=$REGISTRY/${APP_NAME}:${VERSION}-${RANDOM}

docker build --tag ${TAG} .
docker push ${TAG}

pyflyte --pkgs iris_pipeline.workflows package --image k3d-registry.${TAG} -f

echo "Docker image ${TAG} built and workflow packaged with pyflyte"
