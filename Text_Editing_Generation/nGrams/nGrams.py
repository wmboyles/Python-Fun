from random import choice
import pickle
from os import mkdir


def nGrams(txtIn, n):
    '''
    Generates a Markov-based nGram list for a given String and size
    '''

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


def getText(filename):
    '''
    Opens a UTF-8 encoded file and returns the contents as a string
    '''
    # with open(filename, 'r', encoding="utf8") as file: return ''.join(line for line in file)
    return ''.join(bytes(line, 'utf-8').decode('utf-8', 'ignore') for line in open(filename, 'r'))


def markovIt(n, m):
    '''
    Given a already-generated n-gram list called ngram and a text string called txt,
    this generates text of length m from n-sized grams.
    '''
    
    currentGram = ngrams[0][0]
    resetGram = currentGram

    #print(currentGram)
    #print(ngrams)

    result = ""
    for i in range(m):
        nextGrams = []
        for gram in ngrams:
            if gram[0] == currentGram:
                nextGrams = gram[1]
                break

        if len(nextGrams) == 0:
            nextChar = resetGram[0]
        else:
            nextChar = choice(nextGrams)
        result += nextChar
        currentGram = currentGram[1:]+nextChar

    print(result)

def pickle_load(filename):
    '''
    Loads a serialized .p file that represents a generate ngram list and returns the list.
    '''
    with open(filename, 'rb') as fp: return pickle.load(fp)


def pickle_save(filename, itemlist):
    '''
    Saves a given list to a given location for serialization as a .p file
    '''
    with open(filename, 'wb') as fp: pickle.dump(itemlist, fp)
    print("Saved List")


def getUserInfo():
    '''
    Gets the filename, gram size, and text length that the user wants.
    This function will try to use serilization to load a markov ngram list,
    otherwise it will generate it. This generation can be very time-consuming
    for large gram-sizes and text files. However, this function will also
    serialize the list so the user only has to do generation once.
    '''

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
