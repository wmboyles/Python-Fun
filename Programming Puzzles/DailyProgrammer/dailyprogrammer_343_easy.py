Chrom2 =["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
Chrom2+=Chrom2

solf = ["Do","Re","Mi","Fa","So","La","Ti","Do"]
Maj = [0,2,4,5,7,9,11]
Min = [0,2,3,5,7,8,10]
HMin = [0,2,3,5,7,8,11]
MMin = [0,2,3,5,7,9,11]

def Note(root, solf, scaleType):
    rootPlus=0
    
    if(scaleType.lower()=="major"): #Ionian???
        if(solf=="Do"): rootPlus=Maj[0]
        elif(solf=="Re"): rootPlus=Maj[1]
        elif(solf=="Mi"): rootPlus=Maj[2]
        elif(solf=="Fa"): rootPlus=Maj[3]
        elif(solf=="So"): rootPlus=Maj[4]
        elif(solf=="La"): rootPlus=Maj[5]
        elif(solf=="Ti"): rootPlus=Maj[6]
        
    elif(scaleType.lower()=="minor"): #Aeolian??? Dorian?-ish??
        if(solf=="Do"): rootPlus=Min[0]
        elif(solf=="Re"): rootPlus=Min[1]
        elif(solf=="Mi"): rootPlus=Min[2]
        elif(solf=="Fa"): rootPlus=Min[3]
        elif(solf=="So"): rootPlus=Min[4]
        elif(solf=="La"): rootPlus=Min[5]
        elif(solf=="Ti"): rootPlus=Min[6]

    elif(scaleType.lower()=="harmonic minor"):
        if(solf=="Do"): rootPlus=HMin[0]
        elif(solf=="Re"): rootPlus=HMin[1]
        elif(solf=="Mi"): rootPlus=HMin[2]
        elif(solf=="Fa"): rootPlus=HMin[3]
        elif(solf=="So"): rootPlus=HMin[4]
        elif(solf=="La"): rootPlus=HMin[5]
        elif(solf=="Ti"): rootPlus=HMin[6]

    elif(scaleType.lower()=="melodic minor"):
        if(solf=="Do"): rootPlus=MMin[0]
        elif(solf=="Re"): rootPlus=MMin[1]
        elif(solf=="Mi"): rootPlus=MMin[2]
        elif(solf=="Fa"): rootPlus=MMin[3]
        elif(solf=="So"): rootPlus=MMin[4]
        elif(solf=="La"): rootPlus=MMin[5]
        elif(solf=="Ti"): rootPlus=MMin[6]

    rootIndex=0
    for i in range(0,len(Chrom2)//2):
        if(Chrom2[i]==root):
            rootIndex=i

    print(Chrom2[rootIndex+rootPlus])

def main():
    st = input("Scale Type: ")
    rt = input("Root Note: ")
    for s in solf: Note(rt,s,st)

    agn = input("Again: ")
    if(agn.lower()=="y" or agn.lower()=="yes" or agn.lower()=="1"): main() 
main()
