from time import sleep
from winsound import Beep

'''
This version of the program does not create or save a .wav file.
Instead it just tells the computer to beep when it needs to.
This version is faster than creating a .wav file, but sound
quality is reduced.
'''

def MorseIt(plaintext):
    cyphertext2 = list(str(plaintext.lower()))
    MorseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----","/","..--.."]
    Lookup = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]

    for i1 in range(len(Lookup)):
        for i2 in range(len(cyphertext2)):
            if cyphertext2[i2]==Lookup[i1]:
                cyphertext2[i2]=str(MorseTable[i1])
    returntext2 = " ".join(cyphertext2)
    
    return returntext2


def MorseToNums(plaintext):
    morse = str(MorseIt(plaintext))
    print(morse)
    
    morsenum = []
    for i in range(0,len(morse)):
        if(morse[i]==" "): morsenum.append(0)
        if(morse[i]=="."): morsenum.append(1)
        if(morse[i]=="-"): morsenum.append(2)
        if(morse[i]=="/"): morsenum.append(3)
        
    return morsenum


def MorseSounds(plaintext):
    datalist = MorseToNums(plaintext)
    
    for i in range(len(datalist)+1):        #Inserts spaces between characters
        datalist.insert(2*i -1,4)

    for i in range(len(datalist)):
        if(datalist[i]==0): sleep(.36)     #Pause between letters
        elif(datalist[i]==1): Beep(440,180)    #Dit
        elif(datalist[i]==2): Beep(440,360)    #Dah
        elif(datalist[i]==3): sleep(.84)  #Space between words
        elif(datalist[i]==4): sleep(.05)   #Space between characters


MorseSounds(input("Input: "))
