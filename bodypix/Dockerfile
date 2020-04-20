FROM nvcr.io/nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

ENV TF_FORCE_GPU_ALLOW_GROWTH=true

RUN \
    apt update -y && \
    apt install -y curl make build-essential && \
    # apt install -y python3 python3-dev
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get -y install nodejs && \
    mkdir /.npm && \
    chmod 777 /.npm

WORKDIR /src

COPY package.json /src/

RUN npm install

COPY app.js /src/

ENTRYPOINT node /src/app.js