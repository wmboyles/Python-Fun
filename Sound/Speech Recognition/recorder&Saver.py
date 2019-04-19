import numpy
import sounddevice as sd
import soundfile as sf
import sys

sd.default.samplerate = 44100
sd.default.channels = 2
duration = 5

print("Recording")
myrecording = sd.rec(int(duration * sd.default.samplerate))
sd.wait()

print("Playing")
sd.play(myrecording)
sd.wait()

print("Saving")
filename = 'output.wav'
sf.write(filename, myrecording, sd.default.samplerate)
