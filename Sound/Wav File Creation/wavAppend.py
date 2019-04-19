import wave

def wavCombine(file1, file2):
    infiles = [file1+".wav",file2+".wav"]
    outfile = "combined.wav"

    data = []
    for infile in infiles:
        w = wave.open(infile, 'r')
        data.append([w.getparams(),w.readframes(w.getnframes())])
        w.close()

    output = wave.open(outfile,'w')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()
