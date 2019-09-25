'''

Xavi Standard Audio Service
Shell Service

Author:: Sam F // PyGoose // https://github.com/SimLoads
'''
Version = '092519.5x0005'
'''
Release Version:: 0.0.1

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

def xs_cmFormulate(npa,lv,pr):
    Args = {
        'dtype':'-d ',
        'ind':'-i ',
        'device1':'-fd ',
        'device2':'-sd ',
        'freq':'-r ',
        'length':'-l '
    }
    if 'device1' in lv:
        # Preparing for livebridge
        print("")
        command = []
        command.append(str(confItems[0] +' XaviSNS.py -c livebridge '))
        fname, ind, dty, dv1, dv2 = npa[0], npa[1], npa[2], npa[3], npa[4]
        if len(fname) > 0: command.append(str('-f ' + fname + " "))
        if not ind == '':
            command.append(str((Args["ind"]) + ind + " "))
        if not dty == '':
            command.append(str((Args["dtype"]) + dty + " "))
        if not dv1 == '':
            command.append(str((Args["device1"]) + dv1 + " "))
        if not dv2 == '':
            command.append(str((Args["device2"]) + dv2 + " "))
        os.system(''.join(command))
    elif 'freq' in lv:
        # Preparing for testwave
        print("")
        frq, lng, fname = npa[0], npa[1], npa[2]
        command = confItems[0] + ' XaviSNS.py -c testwave '
        command = (command + '-f ' + fname + " ")
        if not lng == '':
            command = (command + (Args["length"]) + lng + " ")
        if not frq == '':
            command = (command + (Args["freq"]) + frq + " ")   
        os.system(command)
    return
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
        cmList["livebridge"] =  Xavi.livebridge
        cmList["testwave"] =  Xavi.testwave
    else:
        errorHandle("Xavi Directory is missing.")
        exit()
    print(asLogo)
    takeInput()

def xs_help():
    print("XaviShell Help\n\nCommands:\n")
    for key, value in cmList.items():
        print(key)
def execdir():
    with open('.xaviconf', 'r') as xfc:
        current = xfc.read()
        print("Current command: " + (current.split(' >< ')[0]))
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
def force():
    import Xavi,XaviSNS
    direct = input("direct|>")
    run = ("python XaviSNS.py " + direct)
    os.system(run)

def arg(out, dcLookup, process):
    import Xavi
    nPosArgs = []
    sigvars = (str(inspect.signature(dcLookup)).replace("(","").replace(")","")).replace(' ','').split(',')
    lVars = len(sigvars)
    print("Arguments Required: %s" % lVars)
    for n,l in enumerate(sigvars):
        tVar = input("%s >> " %l)
        nPosArgs.append(tVar)
    if out == 'force_return':
        return nPosArgs, sigvars, process
    else:
        getattr(sys.modules[__name__], out)(nPosArgs, sigvars, process)

def takeInput():
    try:
        print("")
        process = input("xavi|>")
        # If command is recognized
        if process in cmList:
            dcLookup = (cmList[process])
            # If command is for Xavi
            if process in xs_reqPosArgs:
                xaviArgs(dcLookup, process)
                takeInput()
            elif "query" in process:
                com = input("command >> ")
                query(com)
                takeInput()
            # Else 
            else:
                if process == "exit":
                    exit()
                (dcLookup())
                takeInput()
        # Unknown command
        else:
            errorHandle(("Unrecognized Input: %s" % process))
            takeInput()
    except EOFError:
        exit()
    except KeyboardInterrupt:
        exit()
def xaviArgs(dcLookup, process):
    if process == "livebridge":
        if input("method >> ") == "device":
            os.system(confItems[0] +" XaviSNS.py -c livebridge")
            return()
        else:
            out = 'xs_cmFormulate'
            arg(out, dcLookup, process)
            return
cmList = {
    "exit": exit,
    "reboot": reboot,
    "force": force,
    "edir": execdir,
    "help": xs_help,
    "query": query
    }

helpdict = {
    "exit": "Closes the program.",
    "reboot": "Closes the program, then opens a new instance of it.",
    "force": "Forces a command to pass directly into XaviSNS. [experimental]",
    "edir": "Set where XaviShell calls python from, either $PATH or an absolute directoy.",
    "query": "Get help for specific command",
    "help": "Displays the help menu.",
    "livebridge": "See XaviSNS for help.",
    "testwave": "See XaviSNS for help."
}
xs_reqPosArgs = [
    'livebridge',
    'testwave'
]
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