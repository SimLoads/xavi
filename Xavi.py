'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 042419.1x0002

/NOTES/

y(t) = A * sin(2 * pi * f * t)
A is the amplitude
f is the frequency.
t is our sample. Since we need to convert it to digital, we will divide it by the sampling rate.

fontconfig needs path insert current directory

'''
def audtest(filename):
    import sys
    sys.path.insert(0, 'xavi_filetype_mod')
    try:
        import filetype
    except:
        print("Import fail!")
        exit()
    try:
        fType = ((filetype.guess(filename)).mime)
    except FileNotFoundError:
        print("File does not exist!")
        exit()
    except AttributeError:
        print(filename + " is not supported. ")
        return()
    if "audio" in fType:
        print(filename + " is a supported format.")
        return()
    else:
        print("Unsupported format.")

def testwave(x):
    import os
    import numpy as np
    import wave
    import struct
    os.chdir('matplotlib')
    import matplotlib.pyplot as plt
    # frequency is the number of times a wave repeats a second
    frequency = 1000
    num_samples = 48000
    # The sampling rate of the analog to digital convert
    sampling_rate = 48000.0
    amplitude = 16000
    file = "test.wav"
