#!/bin/bash
# export USE_BYTESCHEDULER=0
export BYTESCHEDULER_WITH_MXNET=1
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

cd ~ && git clone --recursive --branch v1.5.x https://github.com/apache/incubator-mxnet.git
cd incubator-mxnet && git reset --hard 75a9e187d00a8b7ebc71412a02ed0e3ae489d91f
# cd /usr/local/cuda/lib64 && sudo ln -s stubs/libcuda.so libcuda.so.1
cd ~/mine/bytescheduler &&  /home/ubuntu/anaconda3/envs/mxnet_p36/bin/python setup.py install

