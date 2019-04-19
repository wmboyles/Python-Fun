from json import load
import sys

def main(argv = None):
    if argv is None or len(argv) == 0: ac = input("Area Code: ")
    else: ac = argv

    for arg in ac: findAreaCode(arg)

def findAreaCode(ac):
    with open("northAmerica_areaCodes.json") as codes_Json:
        codes = load(codes_Json)
        for code in codes:
            if code['code'] == ac:
                printCode(code)
                return

        print("Could not find area code: "+ac+"\n")

def printCode(code):
    print("Code: "+code['code'])
    print("Location: "+code['state'])
    print("Overlapping Codes: "+code['overlapping'])
    print()
        
        
if __name__ == '__main__': main(sys.argv[1:])
