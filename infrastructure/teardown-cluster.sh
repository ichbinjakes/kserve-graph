#!/bin/bash
set -ex

REGISTRY_NAME=registry.localhost
CLUSTER_NAME=default

k3d registry delete $REGISTRY_NAME

k3d cluster delete $CLUSTER_NAME
