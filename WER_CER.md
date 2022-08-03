(py37) jovyan@jupyter-k6cheng-40ucsd-2eedu:~/DeepSpeech$ python DeepSpeech.py --test_files data/CV/en/clips/test.csv --checkpoint_dir /home/jovyan/.local/share/deepspeech/checkpoints
I Loading best validating checkpoint from /home/jovyan/.local/share/deepspeech/checkpoints/train-3262
I Loading variable from checkpoint: cudnn_lstm/rnn/multi_rnn_cell/cell_0/cudnn_compatible_lstm_cell/bias
I Loading variable from checkpoint: cudnn_lstm/rnn/multi_rnn_cell/cell_0/cudnn_compatible_lstm_cell/kernel
I Loading variable from checkpoint: global_step
I Loading variable from checkpoint: layer_1/bias
I Loading variable from checkpoint: layer_1/weights
I Loading variable from checkpoint: layer_2/bias
I Loading variable from checkpoint: layer_2/weights
I Loading variable from checkpoint: layer_3/bias
I Loading variable from checkpoint: layer_3/weights
I Loading variable from checkpoint: layer_5/bias
I Loading variable from checkpoint: layer_5/weights
I Loading variable from checkpoint: layer_6/bias
I Loading variable from checkpoint: layer_6/weights
Testing model on data/CV/en/clips/test.csv
Test epoch | Steps: 12 | Elapsed Time: 0:07:08                                                                       
Test on data/CV/en/clips/test.csv - WER: 1.000000, CER: 0.835150, loss: 209.617264
--------------------------------------------------------------------------------
Best WER: 
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.844660, loss: 359.894348
 - wav: file://data/CV/en/clips/pacific_ic_audio_28.wav
 - src: "[Pacifico] IC. Pacifico IC, go ahead. (chirp) Engine 30?, you can bring him on down. Go ahead and start"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.846154, loss: 350.056366
 - wav: file://data/CV/en/clips/pacific_ic_audio_27.wav
 - src: "5, we're gonna cancel the comp? line? and update it to a brush comp? line? Stand by. LA, from [Pacifico]"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.827957, loss: 295.566040
 - wav: file://data/CV/en/clips/pacific_ic_audio_38.wav
 - src: "wind from the north east 10 to 15 miles an hour. 5 acres creeping downhill. And we do have uh"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.833333, loss: 274.233582
 - wav: file://data/CV/en/clips/pacific_ic_audio_29.wav
 - src: "a, uh, second ambulance, and, uh, an additional squad. We do have one burn [patient]"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.813559, loss: 193.728485
 - wav: file://data/CV/en/clips/pacific_ic_audio_36.wav
 - src: "north east approximately 10 15 miles an hour, we do have uh"
 - res: "                "
--------------------------------------------------------------------------------
Median WER: 
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.813559, loss: 193.728485
 - wav: file://data/CV/en/clips/pacific_ic_audio_36.wav
 - src: "north east approximately 10 15 miles an hour, we do have uh"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.824561, loss: 181.142792
 - wav: file://data/CV/en/clips/pacific_ic_audio_32.wav
 - src: "copy yea afirm cannot make a notification now for the ???"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.818182, loss: 156.975143
 - wav: file://data/CV/en/clips/pacific_ic_audio_33.wav
 - src: "copy we are assign 69 bravo, afirm thank you"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.815789, loss: 154.383850
 - wav: file://data/CV/en/clips/pacific_ic_audio_30.wav
 - src: "[patient]. Copy. LA, this is 67. 6 [7]"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.888889, loss: 152.458466
 - wav: file://data/CV/en/clips/pacific_ic_audio_39.wav
 - src: "structure threaten. Copy with structure alert"
 - res: "                "
--------------------------------------------------------------------------------
Worst WER: 
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.815789, loss: 154.383850
 - wav: file://data/CV/en/clips/pacific_ic_audio_30.wav
 - src: "[patient]. Copy. LA, this is 67. 6 [7]"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.888889, loss: 152.458466
 - wav: file://data/CV/en/clips/pacific_ic_audio_39.wav
 - src: "structure threaten. Copy with structure alert"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.804878, loss: 141.853012
 - wav: file://data/CV/en/clips/pacific_ic_audio_35.wav
 - src: "Pacifico ic go ahead. okay we do have one"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.861111, loss: 134.901291
 - wav: file://data/CV/en/clips/pacific_ic_audio_37.wav
 - src: "5 acres creeping downhill. Copy that"
 - res: "                "
--------------------------------------------------------------------------------
WER: 1.000000, CER: 0.833333, loss: 120.213943
 - wav: file://data/CV/en/clips/pacific_ic_audio_34.wav
 - src: "??????? LA this is pacifico ic"
 - res: "                "
--------------------------------------------------------------------------------
(py37) jovyan@jupyter-k6cheng-40ucsd-2eedu:~/DeepSpeech$ 