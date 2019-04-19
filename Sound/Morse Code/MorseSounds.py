from math import sin, pi
from time import sleep
from struct import pack
from wave import open
from os import startfile, remove

#Creates a .wav file of one note played at a certain frequency, time, type(sqaure,sine) and saves it to a file.
def wav(frequency, time, wavType, filename):
    period = 1/frequency
    sampSec = 44100*period
    timePeriods = time*sampSec
    
    x=range(int(sampSec))
    y=int(sampSec)*[0]

    if(wavType=="Square"):
        for i in x:
            if i<sampSec/2: y[i]=1.0
            else: y[i]=-1.0

    if(wavType=="Sin"):
        for i in x:
             y[i]=(4/pi)*sin(2*pi*i/sampSec)

    #if(wavType=="None"):

    y=int(44100*time/(sampSec))*y

    fout=open(str(filename)+".wav","w")
    fout.setnchannels(1) #mono audio
    fout.setsampwidth(2) #2 byte sample
    fout.setframerate(44100)
    fout.setcomptype('NONE','Not Compressed')
    BinStr=b''

    for i in range(len(y)):
        BinStr+=pack('h',round(y[i]*20000))

    fout.writeframesraw(BinStr)
    fout.close()


#combines .wav files sequentially in the order they are given as parameters.
def wavCombine(file1, file2):
    infiles = [file1,file2]   
    outfile = "morse.wav"

    data = []
    for infile in infiles:
        w = open(infile, 'r')
        frames = w.getnframes()
        data.append([(1,2,44100,frames,'NONE','Not Compressed'),w.readframes(frames)])
    w.close()

    output = open(outfile,'w')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

#Converts plaintext to morse code text
def MorseIt(plaintext):
    cyphertext2 = list(str(plaintext.lower()))
    MorseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----","/","..--.."]
    Lookup = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]
    for i3 in range(0,len(Lookup)):
        for i4 in range(0, len(cyphertext2)):
            if cyphertext2[i4]==Lookup[i3]:
                cyphertext2[i4]=str(MorseTable[i3])
    returntext2 = " ".join(cyphertext2)
    return returntext2

#Converts morse code into a number where each digit represents a morse code character.
def MorseNums(plaintext):
    morse = str(MorseIt(plaintext))
    print(morse)
    
    morsenum = []
    for i in range(0,len(morse)):
        if(morse[i]==" "): morsenum.append(0)
        if(morse[i]=="."): morsenum.append(1)
        if(morse[i]=="-"): morsenum.append(2)
        if(morse[i]=="/"): morsenum.append(3)
    return morsenum

#creates a .wav file of a given stirng in morse code as plays it if prompted.
def MorseSounds(plaintext,playsound):
    if(len(plaintext)>160):                                 #Keeps inputs short
        print("Input is too long. Max 160 characters.")
        plaintext=""
        MorseSounds(input("Input: "))
        
    datalist = MorseNums(plaintext)
    for i in range(0,len(datalist)+1):                      #Inserts spaces between characters
        datalist.insert(2*i -1,4)

    for i in range(0,len(datalist)):
        if(datalist[i]==0): wav(440,9/25,"None",str(i))     #Pause between letters
        elif(datalist[i]==1): wav(440,3/25,"Sin",str(i))    #Dit
        elif(datalist[i]==2): wav(440,9/25,"Sin",str(i))    #Dah
        elif(datalist[i]==3): wav(440,21/25,"None",str(i))  #Space between words
        elif(datalist[i]==4): wav(440,1/25,"None",str(i))   #Space between characters

        if(i==0): wavCombine("0.wav",str(i)+".wav")                    #Combine first two files
        else: wavCombine("morse.wav",str(i)+".wav")                    #Combine rest of files
        
        remove(str(i)+".wav")

    #Plays the file for enough time to play the entire file
    if(playsound==True):
        startfile("morse.wav")
        sleep(len(datalist)/5.5) #This line is useful if you want to automactically close the sound player.


MorseSounds(input("Input: "),True)
