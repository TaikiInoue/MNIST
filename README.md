# MNIST
Version Controlled MNIST with DVC


## How to get a specific version of MNIST

```
git clone https://github.com/TaikiInoue/MNIST.git
cd MNIST
git checkout <commit_hash>
make docker_build
make docker_run
dvc repro
```
- MNIST v.1.0 - 30,000 images are available (commit_hash = 4c8f24e22ce9ef8bce10fe28c2eb91b9cfebbc55)
- MNIST v.2.0 - 60,000 images are available (commit_hash = b0bcf145eb08aa4725c801703f8bf56686fcca63)
