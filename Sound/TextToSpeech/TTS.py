from gtts import gTTS
from os import startfile, remove, system
from time import sleep
#from mutagen.mp3 import MP3


def textToSpeech(words,filename):
    if words=="": textToSpeech(input("Say: "),"1")
    if filename[-4:]!=".wav": filename+=".wav"  #Appends .mp3 extenion if not present
    tts = gTTS(text=words,lang='en')    #Translates text to speech
    tts.save(filename)  #Saves speech as mp3
    startfile(filename)  #plays mp3 file
    try: sleep(playtime(filename))
    except NameError: sleep(7)
    remove(filename)    #deletes mp3 file
    textToSpeech(input("Say: "),"1")


def playtime(filename):
    audio = MP3(filename)
    return audio.info.length


print("Type what you want to say and press ENTER.")
textToSpeech(input("Say: "),"1")

