Create Virtual Environment
conda create --name py37 python=3.7.0
source activate py37

This will activate the virtual environment that has python 3.7 which allows you to run tensorflow=1.5.4

pip3 install --upgrade pip==20.2.2 wheel==0.34.2 setuptools==49.6.0
pip3 install --upgrade -e .

pip3 uninstall tensorflow
pip3 install 'tensorflow-gpu==1.15.4'

To Run Training (Be at DeepSpeech folder)
python DeepSpeech.py --train_files ./data/CV/en/clips/train.csv --dev_files ./data/CV/en/clips/dev.csv --test_files ./data/CV/en/clips/test.csv

Downgrade protobuf
pip3 install --upgrade protobuf==3.20.0

Good Reference
https://colab.research.google.com/github/acabunoc/Tutorial-train-dutch-model/blob/master/DeepSpeech_train_a_model%2C_CV_Dutch.ipynb#scrollTo=GQqoOP4RwRnG


deepspeech --model .local/share/deepspeech/checkpoints/best_dev-112 --scorer "" --audio DeepSpeech/data/CV/en/clips/pacific_ic_audio_11.wav


Train Your Own Model
virtualenv -p python3 $HOME/tmp/deepspeech-venv/
source $HOME/tmp/deepspeech-venv/bin/activate
pip3 install deepspeech
pip3 install --upgrade deepspeech
pip3 install deepspeech-gpu
pip3 install --upgrade deepspeech-gpu

deepspeech --model ../.local/share/deepspeech/checkpoints/best_dev-112 --scorer "" --audio ../DeepSpeech/data/CV/en/clips/pacific_ic_audio_11.wav