'''

Xavi Standard Audio Service
Stop and Swap System

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 041219.2x0002

/NOTES/



'''
import sys
import os
def error(type):
    print("An error occured.")
    print("- Reason given:")
    if type == "argument":
        print("-- Missing parameters.")
        print("-- Use 'XaviSAS -h' for syntax.")
    elif type == "import":
        print("-- Xavi or another tool could not be imported")
        print("-- Ensure Xavi is in the same directory")
    else:
        print("-- null")
    exit()
sys.path.insert(0, (os.getcwd))
try:
    import Xavi
except:
    error("import")

def help():
    print("XaviSNS Help\n")
    print("  -h : Displays this")
    print("  -c : Specify funciton to call")
    print("  -f : Specify file to use")

def run(functionToCall, filename):
    try:
        result = getattr(Xavi, functionToCall)(filename)
    except AttributeError:
        error("call")
    exit()

if __name__ == "__main__":
    import sys
    del sys.argv[0]
    lj = ' '.join(sys.argv)
    if '-h' in lj:
        help()
        exit()
    if '-c' in lj:
        functionToCall = ((lj.split('-c', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(functionToCall) == 0:
            error("argument")
    else:
        error("argument")
    if '-f' in lj:
        filename = ((lj.split('-f', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    run(functionToCall, filename)
