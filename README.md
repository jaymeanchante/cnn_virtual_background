# cnn_virtual_background

## Setup

Make sure you have [git](https://git-scm.com/) and [docker](https://www.docker.com/), then clone the repo:

```
git clone https://github.com/jaymeanchante/cnn_virtual_background && cd cnn_virtual_background
```

and run everything:

```
docker-compose up
```

## Aditional steps

Adding support for Nvidia GPU in [docker-compose](https://docs.docker.com/compose/) tool using the legacy runtime command by installing [nvidia-container-runtime](https://github.com/NVIDIA/nvidia-container-runtime)

If you are using a recent Linux kernel version you might need to compile *v4l2loopback*& from source using the [repo](https://github.com/umlaeute/v4l2loopback)

## Attribution

Code improved from elder.dev blog [post](https://elder.dev/posts/open-source-virtual-background/) under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.