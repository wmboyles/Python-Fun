from datetime import datetime
from gtts import gTTS
from os import startfile, remove, system
from random import randint, seed
from re import sub
from time import sleep
from winsound import Beep

chance = 1  # 1=100%


def textToSpeech(words, filename):
    if filename[-4:] != ".mp3": filename += ".mp3"  # Appends .mp3 extenion if not present

    tts = gTTS(text=words, lang='en')  # Translates text to speech
    tts.save(filename)  # Saves speech as mp3

    startfile(filename)  # plays mp3 file
    # remove(filename)    #deletes mp3 file -- interferes with playing process
 

def MorseToNums(morse):
    morsenum = []
    
    for i in range(0, len(morse)):
        if(morse[i] == " "): morsenum.append(0)
        if(morse[i] == "."): morsenum.append(1)
        if(morse[i] == "-"): morsenum.append(2)
        if(morse[i] == "/"): morsenum.append(3)
        
    return morsenum

    
def MorseSounds(plaintext):
    datalist = MorseToNums(plaintext)
    
    for i in range(0, len(datalist) + 1): datalist.insert(2 * i - 1, 4)  # Inserts spaces between characters

    for i in range(0, len(datalist)):
        if(datalist[i] == 0): sleep(.32)  # Pause between letters
        elif(datalist[i] == 1): Beep(550, 180)  # Dit
        elif(datalist[i] == 2): Beep(550, 360)  # Dah
        elif(datalist[i] == 3): sleep(.512)  # Space between words
        elif(datalist[i] == 4): sleep(.032)  # Space between characters


def MorseIt(plaintext):
    cyphertext2 = list(str(plaintext.lower()))
    MorseTable = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "/", "..--.."]
    Lookup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]

    for i3 in range(0, len(Lookup)):
        for i4 in range(0, len(cyphertext2)):
            if cyphertext2[i4] == Lookup[i3]: cyphertext2[i4] = str(MorseTable[i3])
                
    returntext2 = " ".join(cyphertext2)
    print(returntext2)
    
    MorseSounds(returntext2)


def LeetIt(plaintext):
    cyphertext = list(str(plaintext.lower()))
    HashTable = ["4", "13", "(", "[)", "3", "|=", "6", "|-|", "|", ".]", "|<", "1", "|Y|", "/\/", "0", "|>", "0,", "|2", "5", "7", "[_]", "\/", '\\v/', "}{", "`/", "2"]
    LookUp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for i1 in range (0, 26):
        for i2 in range(0, len(cyphertext)):
            if cyphertext[i2] == LookUp[i1] and randint(1, 100) % chance == 0: cyphertext[i2] = str(HashTable[i1])

    returntext = "".join(cyphertext)
    print(returntext)


def RandCap(hashtext):
    seed(datetime.now())
    cyphertext2 = list(str(hashtext))
    
    for i in range(len(cyphertext2)):
        if cyphertext2[i].islower():
            if randint(1, 100) % chance == 0: cyphertext2[i] = str(cyphertext2[i].upper())

    returntext = "".join(cyphertext2)
    return returntext


def FivebyFive(plaintext):
    cyphertext3 = list(str(plaintext.lower()))
    TapTable = [".", ".-", "..-", "...-", "..", "....-", ".....-", ".--", "...", "..--", "..-", "...--", "....--", ".....--", "....", ".---", "..---", "...---", "....---", ".....---", ".....", ".----", "..----", "...----", "....----", ".....----", " / "]
    LookUp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    for i5 in range(0, 27):
        for i6 in range(0, len(cyphertext3)):
            if cyphertext3[i6] == LookUp[i5]: cyphertext3[i6] = str(TapTable[i5])
                
    returntext3 = "  ".join(cyphertext3)
    print(returntext3)
    
    MorseSounds(returntext3)


def NATO(plaintext):
    cyphertext = list(str(plaintext.lower()))
    NATOTable = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu", "One", "Two", "Tree", "Four", "Fife", "Six", "Seven", "Eight", "Niner", "Zero"]
    Lookup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for i7 in range(0, 36):
        for i8 in range(0, len(cyphertext)):
            if(cyphertext[i8] == Lookup[i7]): cyphertext[i8] = str(NATOTable[i7])

    returntext = " ".join(cyphertext)
    print(returntext)
    
    textToSpeech(returntext.replace(' ', ', ').replace(', , , ', '. '), "NATO.mp3");

    sleep(int(len(cyphertext) / 1.4))
    system("TASKKILL /F /IM wmplayer.exe")


def ASCII(plaintext, string):
    List = list(plaintext)
    ASCII = []
    
    for i9 in range(0, len(str(plaintext))): ASCII.append(ord(List[i9]))

    if(string == True): print(str(ASCII).strip('[]'))
    else: return ASCII


def ASCII_Binary(plaintext):
    ASCII_int = []
    Binary = []
    
    for i10 in range(0, len(plaintext)): ASCII_int.append(int(ASCII(plaintext, False)[i10]))

    for i11 in range(0, len(ASCII_int)): Binary.append(bin(ASCII_int[i11]))

    print(str(Binary).strip('[]'))


def MorseNums(plaintext):
    morse = str(MorseIt(plaintext))
    morsenum = []
    
    for i in range(0, len(morse)):
        if(morse[i] == " " or morse[i] == "/"): morsenum.append(0)
        if(morse[i] == "."): morsenum.append(1)
        if(morse[i] == "-"): morsenum.append(2)
        
    print(morsenum)


def LetterChange(inp):
    out = []
    for char in inp:
        if ord(char) in range(31, 126): out.append(chr(ord(char) + 1))
        elif ord(char) < 31: out.append(chr(ord(char) + 31))
        else: out.append(chr((ord(char) + 1) % 127))
    return "".join(out)


def LetterChanges(orig, n):
    print("Change: {}".format(n))
    threshold = 97 if n == 97 else n % 97
    for i in range(threshold):
        if i == 0: out = LetterChange(orig)
        else: out = LetterChange(out)
    print(out)


def main():
    entry = input("Enter Text: ")
    
    print("1) Leet Speek")
    print("2) Morse Code")
    print("3) Simplified 5x5")
    print("4) NATO Phonetic Alphabet")
    print("5) ASCII")
    print("6) ASCII Binary")
    print("7) Morse Numbers")
    print("8) Random ASCII Caesar Cypher")
    
    choice = input("Entry: ")
    
    if choice == "1": LeetIt(entry)
    elif choice == "2": MorseIt(entry)
    elif choice == "3": FivebyFive(entry)
    elif choice == "4": NATO(entry)
    elif choice == "5": print(ASCII(entry, True))
    elif choice == "6": ASCII_Binary(entry)
    elif choice == "7": MorseNums(entry)
    elif choice == "8": LetterChanges(entry, randint(1, 96))
    else: print("ERROR")
    
    again = input("Again (Y/N): ")

    if again == "1" or again == "y" or again == "Y": main()


main()

# Morse Code Testing: http://inter.scoutnet.org/morse/morseform.html
