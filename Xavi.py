'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 050719.1x0006

/NOTES/

//

y(t) = A * sin(2 * pi * f * t)
A is the amplitude
f is the frequency.
t is our sample. Since we need to convert it to digital, we will divide it by the sampling rate.

//

fontconfig needs path insert current directory

//

import threading
import time

def my_job():
	print(threading.current_thread().name)

t=threading.Thread(target=my_job)
t.start()

t1=threading.Thread(target=my_job)
t1.start()

t2=threading.Thread(target=my_job)
t2.start()

//
'''
import warnings
warnings.filterwarnings("ignore")
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
    if "wav" in fType:
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
    exit()

def convNumPy(filename, dtype):
    import sys
    import os
    sys.path.insert(0, os.getcwd())
    import numpy as np
    from scipy.io import wavfile
    try:
        file = wavfile.read(filename)
    except ValueError:
        print("Error with wav file.")
        print("Is it a converted mp3?")
        exit()
    except FileNotFoundError:
        print("File not found!")
        exit()
    try:
        waveArray = np.array(file[1],dtype=dtype)
    except:
        print("dtype : " + dtype + " is invalid.")
        exit()
    smlprate = file[0]
    return(waveArray,smlprate)

def threaded_player(waveArray,filename,device,smplrate):
    import sounddevice as sd
    import time
    import warnings
    import datetime
    warnings.filterwarnings("ignore")
    print("Playing " + filename + " on device " + str(device[-1]))
    try:
        sd.play(waveArray, smplrate, device=int(device))
    except:
        try:
            sd.play(waveArray, device=int(device[-1]))
        except:
            print("Device error!")
            exit()
    timewait = int(((len(waveArray)) / smplrate))
    minswait = str(datetime.timedelta(seconds=timewait))
    print("File legnth: " + minswait)
    input()
    sd.stop()

def livebridge(filename, dtype, device1, device2):
    import os
    import threading
    import sys
    import sounddevice
    if device1 == 'blank':
        player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,(sounddevice.default.device),(convNumPy(filename, dtype)[1])))
        player.start()
    else:
        if device2 == 'blank':
            player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device1,(convNumPy(filename, dtype)[1])))
            player.start()
        else:
            player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device1,(convNumPy(filename, dtype)[1])))
            player2 = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device2,(convNumPy(filename, dtype)[1])))
            player.start()
            player2.start()

def liveDeviceCheck():
    print("In development.")
    exit()
    import sounddevice as sd
    print("When selecting a device, use the numerical ID.")
    for number,letter in enumerate(sd.query_devices()):
        lVals = [v for v in letter.values() ]
        for number,letter in enumerate(lVals):
            if letter not in ('speaker', 'headphones', 'output'):
                continue
            print(letter)
        print(number, letter)
    exit()