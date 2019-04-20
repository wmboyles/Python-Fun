from random import choice
import pickle
from os import mkdir

'''
Generates a Markov-based nGram list for a given String and size
'''


def nGrams(txtIn, n):
    grams = []
    counts = []
    for i in range(len(txtIn) - n):
        gram = txtIn[i:i + n]
        if not txtIn[i:i + n] in grams:
            grams.append(gram)
            counts.append([txtIn[i + n]])
        else:
            counts[grams.index(gram)].append(txtIn[i + n])

    out = []
    for i in range(len(counts)):
        out.append((grams[i], counts[i]))

    return out

'''
Opens a UTF-8 encoded file and returns the contents as a string
'''


def getText(filename):
    # with open(filename, 'r', encoding="utf8") as file: return ''.join(line for line in file)
    return ''.join(line for line in open(filename, 'r', encoding="utf8"))

'''
Given a already-generated n-gram list called ngram and a text string called txt,
this generates text of length m from n-sized grams.
'''


def markovIt(n, m):
    currentGram = txt[:n]
    
    result = currentGram
    for i in range(m):
        possibilities = []
        for l in ngrams:
            if l[0] == currentGram:
                possibilities = l[1]
                break
            
        if(len(possibilities) == 0):
            break
        
        nextChar = choice(possibilities)
        result = result + nextChar
        currentGram = result[-1 * n::]

    print(result)

'''
Loads a serialized .p file that represents a generate ngram list and returns the list.
'''


def pickle_load(filename):
    with open(filename, 'rb') as fp: return pickle.load(fp)

'''
Saves a given list to a given location for serialization as a .p file
'''


def pickle_save(filename, itemlist):
    with open(filename, 'wb') as fp: pickle.dump(itemlist, fp)
    print("Saved List")

'''
Gets the filename, gram size, and text length that the user wants.
This function will try to use serilization to load a markov ngram list,
otherwise it will generate it. This generation can be very time-consuming
for large gram-sizes and text files. However, this function will also
serialize the list so the user only has to do generation once.
'''


def getUserInfo():
    global n
    global filename
    global  txt
    global ngrams
    global m
    
    n = int(input("Gram Size: "))

    filename = input("Filename: ")

    txt = getText("Works/" + filename + ".txt")
    print("Loaded Text")
    
    try:
        ngrams = pickle_load("Serialized_ngrams/" + filename + "/" + filename + "_" + str(n) + ".p")
    except FileNotFoundError:
        print("Generating N-grams")
        ngrams = nGrams(txt, n)

        try: mkdir("Serialized_ngrams/" + filename)
        except FileExistsError: next  # If the directory already exists, we don't need to make it

        pickle_save("Serialized_ngrams/" + filename + "/" + filename + "_" + str(n) + ".p", ngrams)
    
    m = int(input("Output Size: "))

'''
Runs through getting user preferences and generating text.
'''


def main():
    global n
    global filename
    global  txt
    global ngrams
    global m
    
    getUserInfo()
    print()
    markovIt(n, m)
    if input("\nAgain(Y/N)?") == "Y": main()

'''
Temporary setup for pre-generating computationally expensive lists
'''
if __name__ == '__main__': main()
