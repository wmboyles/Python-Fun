def FandR(find,replace,filename,save):
    print(filename)
    print("-------------------------------")

    infile = open(str(filename),'r')
    contents = infile.read()
    print(contents)
    print("-------------------------------")
    
    with open(str(filename),'r') as infile:
        contents = infile.read()
        contents = contents.replace(str(find),str(replace))
        print(contents)
        print("")
        
    if(save==True):  
        raw = open(str(filename),'w')
        raw.write(contents)
        raw.close()

'''
This program will find and replace thing in text files that a normal
find and replace function cannot, like adding in new lines.
It will then print the entire text file to the screen, where it can be copied
and saved. The find and replace parameters are as follows:

contents = contents.replace('FIND','REPLACE')

The escape characters like \n are useable.

The file t read from is on the firsst line as follows:

with open("filename.txt") as infile
'''


FandR("o","0","example.txt",True)
print("")
FandR("O","()","example.txt",True)
