from math import sin, pi
import wave, struct


def wav(frequency, time, wavType, filename):
    if(wavType != "None"): period = 1 / frequency
    else: period = 1
    sampSec = 44100 * period
    timePeriods = time * sampSec
    
    x = range(int(sampSec))
    y = int(sampSec) * [0]

    if(wavType == "Square"):
        for i in x:
            if i < sampSec / 2: y[i] = 1.0
            else: y[i] = -1.0

    if(wavType == "Sin"):
        for i in x:
             y[i] = (4 / pi) * sin(2 * pi * i / sampSec)

    if(wavType == "None"):
        for i in x:
            y[i] = 0

    y = int(44100 * time / (sampSec)) * y

    fout = wave.open(str(filename) + ".wav", "w")
    fout.setnchannels(1)  # mono audio
    fout.setsampwidth(2)  # 2 byte sample
    fout.setframerate(44100)
    fout.setcomptype('NONE', 'Not Compressed')
    BinStr = b''

    for i in range(len(y)):
        BinStr += struct.pack('h', round(y[i] * 20000))

    fout.writeframesraw(BinStr)
    fout.close()
