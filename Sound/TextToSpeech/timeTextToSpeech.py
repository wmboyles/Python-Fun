from gtts import gTTS   #text to speech
from os import startfile, remove, system
from time import sleep, strftime    #wait and get time/date

#Mutagen is  module that can calculate MP3 playtime
try: from mutagen.mp3 import MP3
except ModuleNotFoundError: pass

def textToSpeech(words):
    tts = gTTS(text=words, lang='en')    #Generate speech file
    tts.save("time.mp3")
    startfile("time.mp3")   #run file
    sleep(playtime("time.mp3"))
    system("TASKKILL /F /IM vlc.exe")  #closes VLC player
    sleep(.01) #This is needed (>.001) for some reason
    remove("time.mp3")  #delete file 
    
def playtime(filename):
    try: #Must have Mutagen module
        audio = MP3(filename)
        return audio.info.length
    except NameError:
        return 7 #7 secs should cover most cases

def SpeakDate():
    MY = strftime("%B")+" "+strftime("%Y")  #Month,Year eg November 2017
    day = str(int(strftime("%d")))          #day, eg "29" or "3"
    dayName = strftime("%A")                #day name, eg "Wednesday"    
    HM = strftime("%H:%M%p")                #Hour,minute,AM/PM eg 12:15PM
    
    if(day[-1:]=="1"): dayApp = "st"        #Appends the ordinality to the day, 1st, 2nd, 3rd, ..., 9th
    elif(day[-1:]=="2"): dayApp = "nd"
    elif(day[-1:]=="3"): dayApp = "rd"
    else: dayApp = "th"
    day+=dayApp

    textToSpeech("It is "+dayName+", the "+day+" of "+MY+", at "+HM)   #Text to speech
    #This turns to "It is Friday, the 1st of December 2017 at 12:33AM"


SpeakDate()
