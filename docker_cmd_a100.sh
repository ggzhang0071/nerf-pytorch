#img="pytorch/pytorch:1.4-cuda10.1-cudnn7-devel" 

img="nvcr.io/nvidia/pytorch:22.01-py3"


sudo docker run --gpus all  --privileged=true   --workdir /git --name "nerf_pytorch"  -e DISPLAY --ipc=host -d --rm  -p 6602:4452  \
-v /localhome/local-vili/git/nerf-pytorch:/git/nerf-pytorch \
 -v /localhome/local-vili/git/datasets:/git/datasets \
 $img sleep infinity

sudo docker exec -it nerf_pytorch /bin/bash

#docker images  |grep "pytorch"  |grep "21."

#docker stop  nerf_pytorch