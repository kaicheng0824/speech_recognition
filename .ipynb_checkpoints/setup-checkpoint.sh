# conda create --name py37 python=3.7.0
# source activate py37
cd DeepSpeech
pip3 install numpy==1.7.0
pip3 install --upgrade pip==20.2.2 wheel==0.34.2 setuptools==49.6.0
pip3 install --upgrade -e .

pip3 uninstall tensorflow
pip3 install 'tensorflow-gpu==1.15.4'
pip3 install --upgrade protobuf==3.20.0