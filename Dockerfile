FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime
# FROM tensorflow/tensorflow:2.5.1-gpu
 
WORKDIR /app

# RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/es.archive.ubuntu.com/' /etc/apt/sources.list

# RUN apt-get install wget
# RUN  apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub


# RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
#       && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey |  gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
#       && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
#             sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
#              tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


# RUN  wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb 
# RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt-get update  && apt-get install -y git && pip install jupyterlab && apt-get install wget
#RUN ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6  
RUN pip install ultralytics
#(base) armando@armando:~/retinanet/docker$ sudo docker run --gpus all -v $PWD:/test -p 8888:8888 -it tensorflow/tensorflow:2.9.2-gpu
