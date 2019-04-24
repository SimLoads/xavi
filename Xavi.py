print("Modified using Mango 0218190101")
import sys
sys.path.insert(0, 'filetype')
'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 041319.1x0001

/NOTES/



'''
import filetype
def audtest(filename):
    try:
        fType = ((filetype.guess(filename)).mime)
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    print(fType)
    if "audio" in fType:
        print("This is a supported format.")
    else:
        print("Unsupported format.")