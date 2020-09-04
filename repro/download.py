import os
import shutil

import cv2
import numpy as np
import torchvision
from mnist import MNIST
from tqdm import tqdm


def main():

    shutil.rmtree("/mlflow/data/MNIST", ignore_errors=True)
    shutil.rmtree("/mlflow/data/raw_dataset", ignore_errors=True)
    shutil.rmtree("/mlflow/data/dataset/images", ignore_errors=True)

    os.mkdir("/mlflow/data/raw_dataset")
    os.makedirs("/mlflow/data/dataset/images", exist_ok=True)

    torchvision.datasets.MNIST("/mlflow/data", train=True, download=True)
    os.rename("/mlflow/data/MNIST/raw", "/mlflow/data/raw_dataset")

    dataset = MNIST("/mlflow/data/raw_dataset")
    imgs, labels = dataset.load_training()
    imgs = np.array(imgs)

    data_num = 30000
    for i in tqdm(range(data_num)):
        img = imgs[i].reshape(28, 28, 1)
        label = labels[i]
        cv2.imwrite(f"/mlflow/data/dataset/images/{i}_{label}.jpg", img)


if __name__ == "__main__":
    main()
