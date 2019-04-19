from random import randint
from os import startfile, remove
import struct
import wave
from math import sin, pi

deltaOct=False

notes = ["D2","E2","F#2","G2","A2","B2","C#2","D3","E3","F#3","G3","A3","B3","C#3","D4","E4","F#4","G4","A4","B4","C#4","D5"]

def nextNoteName(NN):
    dO=deltaOct
    for i in range(0,len(notes)):
        if(notes[i]==NN):
            cNI=i
            break
    
    ran = randint(0,99)

    #if(cNI=="R"): cNI=notes[randint(0,7)]
    
    if(ran<15):cNI=cNI  #15% chance stays same
    elif(ran<27):cNI+=1 #12% chance +1 (D3-->E3)
    elif(ran<39):cNI-=1 #12% chance -1 (F#3-->E3)
    elif(ran<54):cNI+=2 #15% chance +2 (D3-->F#3)
    elif(ran<69):cNI-=3 #15% chance -3 (D3-->A2)
    elif(ran<77):cNI+=4 #8% chance +4 (D3-->A3)
    elif(ran<85):cNI-=5 #8% chance -5 (D3-->F#2)
    elif(ran<90):cNI+=7 #5% chance +7 (Ocatave)
    elif(ran<95):cNI-=7 #5% chance -7 (Octave)
        
    if(cNI>=len(notes)):cNI-=7
    if(cNI<0):cNI+=7

    return notes[cNI]

def nextNoteLen(cNL): #cNL is current note length -- number of 16th notes
    ran = randint(0,99)
    
    if(cNL>2 and cNL<16):
        if(ran<50): cNL*=1    #50% chance same length
        elif(ran<75): cNL*=2    #25% change doubling
        else: cNL/=2            #25% chance halfing

    else:                       #Makes sure cNL doesn't fall below 1/16th note or abour whole note
        if(cNL==2):
            if(ran<50): cNL=cNL
            else: cNL*=2
        if(cNL==16):
            if(ran<50): cNL=cNL
            else: cNL/=2

    return int(cNL)
            

def wavCombine(file1, file2):   #Combines two wav files into one in order: file1+file2
    infiles = [file1,file2]   
    outfile = "Song.wav"

    data = []
    for infile in infiles:
        w = wave.open(infile, 'r')
        frames = w.getnframes()
        data.append([(1,2,44100,frames,'NONE','Not Compressed'),w.readframes(frames)]) #Compression on to save time
    w.close()

    output = wave.open(outfile,'w')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()

def wav(frequency, time, wavType, filename):    #Makes a .wav file of given frequency(Hz), time(sec), type(Sin/square), and name("1.wav")
    #period = 1/frequency
    sampSec = 44100/frequency
    timePeriods = time*sampSec
    
    x=range(int(sampSec)) #1,2,3,4,...,44100/frequency
    y=int(sampSec)*[0]

    if(wavType=="Sin"):
        for i in x: y[i]=(4/pi)*sin(2*pi*i/sampSec)

    elif(wavType=="None"):
        for i in x: y[i]=0

    y=int(44100*time/(sampSec))*y

    fout=wave.open(str(filename)+".wav","w")
    fout.setnchannels(1) #mono audio (faster?)
    fout.setsampwidth(2) #2 byte sample
    fout.setframerate(44100)
    fout.setcomptype('NONE','Not Compressed') #Compression on to save time
    BinStr=b''

    for i in range(len(y)):
        BinStr+=struct.pack('h',round(y[i]*20000))

    fout.writeframesraw(BinStr)
    fout.close()

    

def DoMusic(songLen):       #Uses functions above to create "random" music
    NoteName = notes[randint(1,len(notes)-1)]
    NoteLen = int(2**randint(0,4))

    f = open("Music_CSV.txt","a")
    f.write(str(NoteName)+", "+str(NoteLen)+'\n')
    f.close()
    
    for i in range(1,songLen):
        NoteName = nextNoteName(NoteName)
        NoteLen = nextNoteLen(NoteLen)
        f = open("Music_CSV.txt","a")
        f.write(str(NoteName)+", "+str(NoteLen)+'\n')
    f.close()

    
def Play(): #Turns list of note into .wav file and plays
    mult=2 #Doubles the note frequency (just sounded better to me)
    
    NoteNames = ["D","E","F#","G","A","B","C#"] #Correspond to frequencies
    Frequencies = [36.71,41.2,46.25,49,55,61.74,69.3] #D1,E1,F#1,G1,A1,B1,C#1 frequencies. (What I call C#1 is conventionally called C#2)

    i=0 #Sequential Filename counter
    
    f = open("Music_CSV.txt","r")
    for line in f:
        Name = line[:3].strip(',')
        Freq = Name[len(Name)-1]

        Name=Name.strip(Freq)
        Freq = round(mult*int(Freq)*float(Frequencies[NoteNames.index(Name)]))
        Length = int(line[4:].strip(' '))/32 #Although this number is out of 32, a note length can't go below 2/32=1/16th note
            
        wav(Freq,Length,"Sin",str(i))
        
        if(i==0):wavCombine("0.wav",str(i)+".wav")
        else: wavCombine("Song.wav",str(i)+".wav")

        remove(str(i)+".wav")
        i+=1

    startfile("Song.wav")

    
def mainT(notes): #This method is more easily called from the terminal
    deltaOct=False
    try:
        remove("Music_CSV.txt")
        remove("Song.wav")
        print("Removed Residual Files.")
    except FileNotFoundError:
        print("No Residual Files Found.")
    DoMusic(int(notes))
    Play()


def main():
    deltaOct=False
    try:
        remove("Music_CSV.txt")
        remove("Song.wav")
        print("Removed Residual Files.")
    except FileNotFoundError:
        print("No Residual Files Found.")
    DoMusic(int(input("Song Notes: ")))
    Play()

main()
#Play()
