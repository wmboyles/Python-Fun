def deBruijn(word_length, alphabet_size=2):
    seq = [0]
    str_seq = ""
    str_size = (alphabet_size)**(word_length)
    #generate list of w' indexes
    while max(seq) < str_size - 1:
        str_seq += str(seq[-1]//(str_size//alphabet_size))
        
        next_num = (seq[-1]*alphabet_size)%(str_size - 1)

        if next_num in seq[-word_length:]:
            i=0
            while i in seq: i+=1
            seq.append(i) 
        else:
            seq.append(next_num)

    str_seq += str(seq[-1]//(str_size//alphabet_size))

    return str_seq

def main():
    wl = int(input("Word Length: "))
    ab = int(input("Alphabet Size: "))
    print(deBruijn(wl,ab))
    main()

main()



    
