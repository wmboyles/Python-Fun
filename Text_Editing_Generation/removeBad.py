def FandR(filename,find,replace):
    infile = open(str(filename),'r')
    contents = infile.read()
    
    for char in contents: contents = contents.replace(str(find),str(replace))

    #Save
    raw = open(str(filename),'w')
    raw.write(contents)
    raw.close()

def lineCount(filename):
    lines, contents = 0, open(str(filename),'r').read()
    
    for i in range(0,len(contents)):
        char = contents[i]
        if "\n" in char: lines+=1
        
    if "\n" not in char: lines+=1 #Last character check

    return lines

def lineList(filename):
    contents=open(str(filename),'r').read()
    line, lines = "", []
    
    for char in contents:
        if char!="\n": line+=char
        else:
            lines.append(line)
            line=""
            
    lines.append(line)
    
    return lines
            
def alphabetizeLines(filename):
    sortedLines = sorted(lineList(filename))
    contents=""
    
    for line in sortedLines: contents += line+"\n"

    #Save
    raw = open(str(filename),'w')
    raw.write(contents)
    raw.close()
