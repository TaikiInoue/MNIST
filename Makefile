docker_build:
		docker build -t mnist:latest -f docker/Dockerfile .

docker_run:
		docker run -it --rm \
			--runtime nvidia \
			--network host \
			--workdir /mlflow/data \
			--volume ${PWD}:/mlflow/data \
			--name mnist-docker \
			--hostname mnist-docker \
			mnist:latest \
			/bin/bash

dvc_repro:
		dvc run -n download \
				-d /mlflow/data/repro/download.py \
				-o /mlflow/data/dataset/images \
				python /mlflow/data/repro/download.py
