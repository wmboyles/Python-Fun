from gtts import gTTS
from os import startfile, remove, system
from time import sleep

def say(announcement, tempFile="say.wav", sleepTime=10):
    try:
        tts = gTTS(text=announcement, lang='en')
        tts.save(tempFile)
    
        startfile(tempFile)
        sleep(sleepTime)

        system("TASKKILL /F /IM vlc.exe")  # closes VLC player
        remove(tempFile)
    except Error:
        print("ERROR: Cannot TTS file")

def main():
    while True:
        announcement = input("Say: ")
        say(announcement)


if __name__ == "__main__":
    main()