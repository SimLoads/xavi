'''

Xavi Standard Audio Service
Stop and Swap System

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 051719.1x0009

/NOTES/



'''
global isLength
import sys
import os
def error(type, param=""):
    print("An error occured.")
    print("- Reason given:")
    if type == "import":
        print("-- Xavi or another tool could not be imported")
        print("-- Ensure Xavi is in the same directory")
    elif type == "call":
        print("-- " + param + ": invalid function")
        print("-- Use XaviSAS -h for help.")
    else:
        print("-- null")
    exit()
os.chdir('xavi')
sys.path.insert(0, os.getcwd())
try:
    import Xavi
except:
    error("import")
os.chdir('..')
Xavi.processorCheck()

if __name__ == "__main__":
    import argparse
    inps = argparse.ArgumentParser(description='Xavi Standard Audio Service // Stop n Swap')
    inps.add_argument('-c', type=str, metavar='function', required=True, 
            help='Function to call [audtest/livebridge/testwave]')
    inps.add_argument('-f', type=str, metavar='file', required=False, default='livebridge',
        help='Name of file')
    inps.add_argument('-l', type=int, metavar='length', required=False, default='1',
        help='Length of output (Certain functions only)')
    inps.add_argument('-r', type=int, metavar='frequency', required=False, default='4000',
        help='Frequency of output (Certain functions only)')
    inps.add_argument('-d', type=str, metavar='dtype', required=False, default='int16', 
        help='Select DType (Certain functions only)')
    inps.add_argument('-fd', type=str, metavar='device ID', required=False, default='blank',
        help='Specify first device (Certain functions only)')
    inps.add_argument('-sd', type=str, metavar='device ID', required=False, default='blank',
        help='Specify second device (Certain functions only)')
    ag = inps.parse_args()
    if (ag.c) == 'audtest':
        Xavi.audtest(ag.f)
        exit()
    if (ag.c) == 'livebridge':
        Xavi.livebridge(ag.f, ag.d, ag.fd, ag.sd)
        exit()
    if (ag.c) == 'testwave':
        if ag.f == 'livebridge':
            fnm = 'example'
        else:
            fnm = ag.f
        Xavi.testwave(ag.r, ag.l, fnm)
        exit()
    else:
        error("call", ag.c)
    exit()
