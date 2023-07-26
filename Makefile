build:
	docker build -t k3d-registry.localhost:12000/test-model:latest -f model/Dockerfile ./model

push:
	docker push k3d-registry.localhost:12000/test-model:latest

run:
	docker run --rm -it -p 8080:8080 k3d-registry.localhost:12000/test-model:latest

deploy-k8s:
	bash ./infrastructure/deploy-cluster.sh
	bash ./infrastructure/deploy-kserve.sh

deploy-graph:
	cd ./infrastructure && bash ./deploy-graph.sh

teardown:
	bash ./infrastructure/teardown-cluster.sh
