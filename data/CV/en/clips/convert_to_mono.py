from pydub import AudioSegment
import os

import glob

# absolute path to search all text files inside a specific folder
path = r'./non-mono/*.wav'
files = glob.glob(path)

for i in range(len(files)):
    print(files[i][0:28])
    path = files[i][0:28]
    #print(path)
    print(files[i][28:30])
    num = files[i][28:30]
    if '.' in num:
        num = num[0]
    
    num = int(num)

    #print(path+str(num)+".wav")
    sound = AudioSegment.from_wav(path+str(num)+".wav")
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    path = path[11:]
    print(path)
    sound.export("./mono/"+path+str(num)+".wav", format="wav")