#!/bin/bash

# deploy knative
# https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/#install-the-knative-serving-component
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.10.2/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.10.2/serving-core.yaml


# deploy kourier networking layer
kubectl apply -f https://github.com/knative/net-kourier/releases/download/knative-v1.10.0/kourier.yaml
kubectl patch configmap/config-network \
  --namespace knative-serving \
  --type merge \
  --patch '{"data":{"ingress-class":"kourier.ingress.networking.knative.dev"}}'


# deploy cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml


# deploy kserve
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.10.2/kserve.yaml
