'''

Xavi Standard Audio Service
Stop and Swap System

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 050719.1x0005

/NOTES/



'''
import sys
import os
def error(type, param=""):
    print("An error occured.")
    print("- Reason given:")
    if type == "argument":
        print("-- Missing parameters.")
        print("-- Use 'XaviSAS -h' for syntax.")
    elif type == "import":
        print("-- Xavi or another tool could not be imported")
        print("-- Ensure Xavi is in the same directory")
    elif type == "call":
        print("-- " + param + ": invalid function")
        print("-- Use XaviSAS -h for help.")
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
    print("  :: Available funcitons:")
    print("    :: audtest")
    print("       -f : File to use (str)")
    print("    :: testwave")
    print("       -f : Name of output (str)")
    print("       -r : Frequency (int)")
    print("       -l : Length in seconds (int)")
    print("     :: livebridge")
    print("        -f : File to use (str)")
    print("        -d : Select dtype (str) (not recommended)")
    print("        --first_device : First output device (int)")
    print("        --second_device : Second output device (int)")
    print("      : Note - do not specify device to auto select default.")

def run(fTC, filename='', length='', frq='', dtype='', device1='', device2=''):
    try:
        if fTC == "audtest":
            Xavi.audtest(filename)
        if fTC == "testwave":
            Xavi.testwave(frq, length, filename)
        if fTC == "livebridge":
            Xavi.livebridge(filename, dtype, device1, device2)
        else:
            error("call", fTC)
    except AttributeError:
        error("import")
        exit()
    exit()

if __name__ == "__main__":
    import sys
    del sys.argv[0]
    lj = ' '.join(sys.argv)
    if '-h' in lj:
        help()
        exit()

    if '-c' in lj:
        fTC = ((lj.split('-c', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(fTC) == 0:
            error("argument")
    else:
        error("argument")
    
    if '-f' in lj:
        filename = ((lj.split('-f', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        filename='exmp'

    if '-r' in lj:
        frq = ((lj.split('-r', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        frq='1000'

    if '-l' in lj:
        length = ((lj.split('-l', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        length='1'

    if '--first_device' in lj:
        device1 = ((lj.split('--first_device', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        device1='blank'

    if '--second_device' in lj:
        device2 = ((lj.split('--second_device', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        device2='blank'

    if '-b' in lj:
        dtype = ((lj.split('-b', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(filename) == 0:
            error("argument")
    else:
        dtype='int16'

    run(fTC, filename, frq, length, dtype, device1, device2)
