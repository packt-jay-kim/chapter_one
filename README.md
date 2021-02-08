# chapter_one

# Setting up Ray Dev environment 

1. using pip

pip install –U ray

2. using conda

conda create --name ray

conda activate ray

conda install --name ray pip

pip install ray

3. pull image of ray from dockerhub

docker pull rayproject/ray

docker run -i -t rayproject/ray:latest

4. using github

git clone https://github.com/ray-project/ray.git

cd ray

./build-docker.sh

5. Alternative ways + test function
- Ubuntu 

sudo apt-get update

sudo apt-get install –y build-essential curl unzip psmisc

pip install cython==0.29.0 pytes

- Mac

brew update

brew install wget

pip install cython==0.29.0 pytest

- Windows

git clone https://github.com/ray-project/ray.git

ray/ci/travis/install-bazel.sh

pushd ray/dashboard/client

npm install

npm run build

popd

cd ray

pip install –e . –verbosepython

