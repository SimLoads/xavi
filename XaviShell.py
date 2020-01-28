'''

Xavi Standard Audio Service
Shell Service

Author:: Sam F // PyGoose // https://github.com/SimLoads
'''
Version = '012820.5x0008'
'''
Release Version:: 0.0.2

/NOTES/



'''
import os,sys,cmd,inspect,ctypes
asLogo='''
__  __           _ ____    _    ____  
\ \/ /__ ___   _(_) ___|  / \  / ___| 
 \  // _` \ \ / / \___ \ / _ \ \___ \ 
 /  \ (_| |\ V /| |___) / ___ \ ___) |
/_/\_\__,_| \_/ |_|____/_/   \_\____/ 
'''
def reboot():
    print("Restarting shell...")
    os.startfile(sys.argv[0])
    exit()

def errorHandle(error):
    print("An error occured.")
    print("Reason given:")
    print("")
    print(error)
    return()

def query(command):
    try:
        print(helpdict.get(command))
    except:
        print("Unrecognized command")
        
def startupCheck():
    print("Xavi Shell Service")
    print("Version %s" % Version)
    ctypes.windll.kernel32.SetConsoleTitleW("Xavi Shell %s" % Version)
    print("")
    if os.path.exists("xavi"):
        sys.path.insert(0, 'xavi')
        import Xavi,XaviSNS
    else:
        errorHandle("Xavi Directory is missing.")
        input()
        exit()
    print(asLogo)
    takeInput()

def xs_help():
    print("XaviShell Help\n\nCommands:\n")
    for key, value in cmList.items():
        print('%s: %s' %(key, value))

def execdir(request=False):
    if request:
        with open('.xaviconf', 'r') as xfc:
            current = xfc.read()
            xfc.close()   
        return(current.split(' >< ')[0])

    with open('.xaviconf', 'r') as xfc:
        current = xfc.read()
        print("Current directory: " + (current.split(' >< ')[0]))
        xfc.close()
    with open('.xaviconf', 'w') as xfc:
        ndir = input("Enter absolute directory of Python executable or 'python' to reset: ")
        if os.path.exists(ndir) and '.exe' in ndir or ndir == 'python':
            cr = current.split(' >< ')
            del cr[0]
            cr.insert(0,ndir)
            toWrite = ' >< '.join(cr)
            xfc.write(toWrite)
        else:
            xfc.write(current)
            print("Invalid")

def cmod():
    os.startfile('.xaviconf')

def execCm(process):
    run = ("%s XaviSNS.py -c %s" %((execdir(True)), process))
    os.system(run)
    return

def forceExec(process):
    run = ("%s XaviSNS.py %s" %((execdir(True)), process))
    os.system(run)
    return

def takeInput():
    try:
        print("")
        process = input("xavi|>")
        if "query" in process:
            com = input("command >> ")
            query(com)
            takeInput()
        elif process in cmList:
            (cmList[process])()
        else:
            if process == "exit":
                exit()
            if process[:2] == '--':
                forceExec(process[1:])
            execCm(process)
            takeInput()
    except EOFError:
        exit()
    except KeyboardInterrupt:
        exit()

cmList = {
    "exit": exit,
    "reboot": reboot,
    "edir": execdir,
    "help": xs_help,
    "query": query
    }

helpdict = {
    "exit": "Closes the program.",
    "reboot": "Closes the program, then opens a new instance of it.",
    "force": "Forces a command to pass directly into XaviSNS. Use 'return' to return.",
    "edir": "Set where XaviShell calls python from, either $PATH or an absolute directoy.",
    "query": "Get help for specific command",
    "help": "Displays the help menu.",
    "livebridge": "See XaviSNS for help.",
    "testwave": "See XaviSNS for help.",
    "tempo": "See XaviSNS for help.",
    "getsamples": "See XaviSNS for help."
}

if __name__ == "__main__":
    defaultItems = "python >< true >< true"
    if os.path.exists(".xaviconf"):
        with open('.xaviconf', 'r') as xfc:
            confItems = (xfc.read()).split(" >< ")
    else:
        with open('.xaviconf', 'w') as xfc:
            xfc.write(defaultItems)
            confItems = defaultItems.split(" >< ")
    startupCheck()