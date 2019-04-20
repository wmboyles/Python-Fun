from winsound import Beep
from time import sleep
from random import choice


def playNote(note):
    name, ocatave, playTimeMS = note
    
    if name.lower() != 'r':
        noteNames = ['d', 'e', 'f#', 'g', 'a', 'b', 'c#']
        frequencies = [36.71, 41.2, 46.25, 49, 55, 61.74, 69.3]

        freqMult = 2 ** (ocatave - 1)
        myFreq = round(freqMult * frequencies[noteNames.index(name.lower())])
        
        Beep(myFreq, playTimeMS)
        
    else:
        sleep(playTimeMS / 1000)


def nextNameOct(name, octave):
    notes = ['d', 'e', 'f#', 'g', 'a', 'b', 'c#', 'r']
    noteIndex = notes.index(name)

    rand = choice(list(range(0, 100)))

    if rand < 15: noteIndex += 0
    elif rand < 27: noteIndex += 1
    elif rand < 39: noteIndex -= 1
    elif rand < 54: noteIndex += 2
    elif rand < 69: noteIndex -= 3
    elif rand < 77: noteIndex += 4
    elif rand < 85: noteIndex -= 5
    elif rand < 90: noteIndex += 7
    elif rand < 95: noteIndex -= 7

    if noteIndex >= len(notes):
        noteIndex = noteIndex % len(notes)
        if rand < 50 and octave < 6: octave += 1
        elif octave > 4: octave -= 1
        
    return (notes[noteIndex], octave)


def nextTime(time):
    mults = [-4, -3, -2, -1, -1, 0, 0, 0, 0, 1, 1, 2, 3]
    mult = choice(mults)
    if mult < 0 and time > -256 * mult: return time + (256 * mult)
    elif mult > 0 and time + (256 * mult) < 1280: return time + (256 * mult)
    elif time >= 512: return time - 256
    return time


def nextNote(note):
    name, octave, playTimeMS = note

    newName, newOctave = nextNameOct(name, octave)
    newPlayTimeMS = nextTime(playTimeMS)

    return (newName, newOctave, newPlayTimeMS)


def randSong(numNotes):
    myNote = ('d', 4, 256)
    
    for i in range(numNotes):
        myNote = nextNote(myNote)
        
        playNote(myNote)
        print(myNote)

