'''

Xavi Standard Audio Service
Stop and Swap System

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 050819.1x0007

/NOTES/



'''
global isLength
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
Xavi.processorCheck()
def help():
    print("XaviSNS Help\nParameters marked with a star are required")
    print("  -h : Displays this")
    print(" *-c : Specify funciton to call")
    print("  :: Available funcitons:")
    print("    :: audtest")
    print("      *-f : File to use (str)")
    print("    :: testwave")
    print("      *-f : Name of output (str)")
    print("       -r : Frequency (int)")
    print("       -l : Length in seconds (int)")
    print("     :: livebridge")
    print("        -l : Return suggested devices to use")
    print("           :: use -l all to see all available devices")
    print("       *-f : File to use (str)")
    print("        -d : Select dtype (str) (not recommended, will use default)")
    print("        --first_device : First output device (int)")
    print("        --second_device : Second output device (int)")
    print("           :: Do not specify device to auto select default.")

def run(fTC, filename='',frq='', length='', dtype='', device1='', device2=''):
    try:
        if fTC == "audtest":
            Xavi.audtest(filename)
        if fTC == "testwave":
            Xavi.testwave(frq, length, filename)
        if fTC == "livebridge":
            if isLength:
                Xavi.liveDeviceCheck(length)
            else:
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
        if len(frq) == 0:
            error("argument")
    else:
        frq='1000'

    if '-l' in lj:
        if fTC == 'livebridge':
            isLength = True
            length = ((lj.split('-l', 1)[1]).split('-', 1)[0]).replace(' ','')
            if len(length) == 0:
                length='devcheck'
        else:
            length = ((lj.split('-l', 1)[1]).split('-', 1)[0]).replace(' ','')
            if len(length) == 0:
                error("argument")
    else:
        length='1'

    if '--first_device' in lj:
        device1 = ((lj.split('--first_device', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(device1) == 0:
            error("argument")
    else:
        device1='blank'

    if '--second_device' in lj:
        device2 = ((lj.split('--second_device', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(device2) == 0:
            error("argument")
    else:
        device2='blank'

    if '-b' in lj:
        dtype = ((lj.split('-b', 1)[1]).split('-', 1)[0]).replace(' ','')
        if len(dtype) == 0:
            error("argument")
    else:
        dtype='int16'
    try:
        if isLength:
            print("")
    except:
        isLength = False
    run(fTC, filename, frq, length, dtype, device1, device2)
