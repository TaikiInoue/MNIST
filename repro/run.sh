base=/mlflow/data

dvc run -n download \
        -d ${base}/repro/download.py \
        -d ${base}/raw_dataset/t10k-images-idx3-ubyte \
        -d ${base}/raw_dataset/t10k-labels-idx1-ubyte \
        -d ${base}/raw_dataset/train-images-idx3-ubyte \
        -d ${base}/raw_dataset/train-labels-idx1-ubyte \
        -o ${base}/dataset/images \
        python ${base}/repro/download.py
