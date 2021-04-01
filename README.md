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
