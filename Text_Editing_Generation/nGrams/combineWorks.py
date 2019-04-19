import shutil
import os

def combine(outName):
    with open(outName, 'wb') as outfile:
        for filename in os.listdir():
            if filename == outName or filename == "combineworks.py":
                continue
            else:
                with open(filename, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)

if __name__ == '__main__':
    combine(input("Output Name: "))
