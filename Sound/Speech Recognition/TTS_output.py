from gtts import gTTS
from os import startfile, remove, system
from time import sleep
#from mutagen.mp3 import MP3


def textToSpeech(words,filename="output.wav"):
    if words=="": textToSpeech(input("Say: "),"1")
    if filename[-4:]!=".wav": filename+=".wav"  #Appends .wav extenion if not present
    tts = gTTS(text=words,lang='en')    #Translates text to speech
    tts.save(filename)  #Saves speech as wav
    startfile(filename)  #plays wav file
    try: sleep(playtime(filename))
    except NameError: sleep(7)
    #remove(filename)    #deletes file


def playtime(filename):
    audio = MP3(filename)
    return audio.info.length

