'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 050219.1x0003

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

def testwave(length, freq, fname):
    import os
    import numpy as np
    import wave
    import struct
    os.chdir('matplotlib')
    # import matplotlib.pyplot as plt
    # frequency is the number of times a wave repeats a second
    os.chdir('..')
    # Frequency
    try:
        fr = int(freq)
    except:
        print("Invalid argument: " + freq)
        exit()
    # Number of samples
    try:
        nsam = (int(length) * int(48000))
    except:
        print("Invalid argument: " + length)
        exit()
    # The sampling rate of the analog to digital convert
    srate = 48000.0
    # Amplitude
    amp = 18000
    file = (fname + ".wav")
    nframes=nsam
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2
    sine_wave = [np.sin(2 * np.pi * fr * x/srate) for x in range(nsam)]
    wav_file=wave.open(file, 'w')
    wav_file.setparams((nchannels, sampwidth, int(srate), nframes, comptype, compname))
    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amp)))
        
def readwav(filename):
    import os
    import sys
    sys.path.insert(0, os.getcwd())
    import numpy as np
    import sounddevice as sd
    import time
    from scipy.io import wavfile
    os.chdir('matplotlib')
    import matplotlib.pyplot as plt
    os.chdir('..')
    try:
        file = wavfile.read(filename)
    except ValueError:
        print("Error with wav file.")
        print("Is it a converted mp3?")
        exit()
    except FileNotFoundError:
        print("File not found!")
        exit()
    waveArray = np.array(file[1],dtype=np.int16)
    lengthArray = (len(waveArray))
    hiF = (np.amax(waveArray))
    loF = (np.amin(waveArray))
    sd.play(waveArray, 44100)
    input()
    sd.stop()

