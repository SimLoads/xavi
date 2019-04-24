'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 042419.1x0002

/NOTES/



'''
import sys
sys.path.insert(0, 'xavi_filetype_mod')
try:
    import filetype
except:
    print("Import fail!")
    exit()
def audtest(filename):
    try:
        fType = ((filetype.guess(filename)).mime)
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    if "audio" in fType:
        print(filename + " is a supported format.")
    else:
        print("Unsupported format.")
