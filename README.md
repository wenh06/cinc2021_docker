# cinc2021_docker

PyTorch1.6.0+cu101 docker file for building docker images

## Why this docker file?
pytorch in
```
pytorch/pytorch:x.x.x-cudax.x-cudnnx-devel
```
is the CPU version, hence one has to perform
```
RUN pip install torch==x.x.x+cuxxx -f https://download.pytorch.org/whl/torch_stable.html
```
to enable the usage of GPU

One can use
```
FROM wenh06/cinc2021_docker:pytorch1.6.0-cuda10.1-cudnn7-devel
```
in his cinc2021 Dockerfile, or use
```
docker pull wenh06/cinc2021_docker:pytorch1.6.0-cuda10.1-cudnn7-devel
```
to pull the image
