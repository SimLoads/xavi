'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 071919.1x0013
Release Version:: 0.0.1

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
def processorCheck():
    import platform
    if "amd" in (str(platform.processor())).lower():
        print("Sorry! There's been an error.")
        print("AMD Machines are currently not supported.")
        print("Check the GitHub for more info.")
        exit()
    else:
        return()
import warnings
warnings.filterwarnings("ignore")

def audtest(filename):
    processorCheck()
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

def testwave(freq, length, fname):
    processorCheck()
    import os, numpy as np, wave, struct
    try:
        os.chdir('matplotlib')
    except:
        print("Installation Error")
        exit()
    os.chdir('..')
    if('xavi' in os.getcwd()):
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
    srate = 48000.0
    amp = 18000
    file = (fname + ".wav")
    nframes=nsam
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2
    print("Calculating...")
    sine_wave = [np.sin(2 * np.pi * fr * x/srate) for x in range(nsam)]
    wav_file=wave.open(file, 'w')
    wav_file.setparams((nchannels, sampwidth, int(srate), nframes, comptype, compname))
    print("Generating...")
    print("This should take about " + str(length) + " Seconds")
    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amp)))
    print("Saved " + str(length) + " second(s) tone to " + file)
    exit()

def convNumPy(filename, dtype):
    processorCheck()
    import sys, os
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
    processorCheck()
    import sounddevice as sd, time, warnings, datetime, sys, select
    warnings.filterwarnings("ignore")
    print("Playing " + filename + " on device " + str(device[-1]))
    try:
        sd.play(waveArray, smplrate, device=int(device))
    except:
        try:
            sd.play(waveArray, device=int(device[-1]))
        except sd.PortAudioError:
            print("Device error!")
            print("This is an input device.")
            if (input("Enter [e] to raise. ")).lower() == "e":
                raise
            exit()
    timewait = int(((len(waveArray)) / smplrate))
    minswait = str(datetime.timedelta(seconds=timewait))
    print("File legnth: " + minswait)
    input()
    sd.stop()

def livebridge(filename, dtype, device1, device2):
    processorCheck()
    import os, threading, sys, sounddevice
    if ("xavi" in os.getcwd()):
        os.chdir('..')
    if filename == 'livebridge':
        liveDeviceCheck('')
    if device1 == 'blank':
        print("Fallback to default device...")
        player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,(sounddevice.default.device),(convNumPy(filename, dtype)[1])))
        player.start()
    else:
        if device2 == 'blank':
            print("Using first device...")
            player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device1,(convNumPy(filename, dtype)[1])))
            player.start()
        else:
            print("Using both devices...")
            player = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device1,(convNumPy(filename, dtype)[1])))
            player2 = threading.Thread(target=threaded_player, args=((convNumPy(filename, dtype)[0]),filename,device2,(convNumPy(filename, dtype)[1])))
            player.start()
            player2.start()

def liveDeviceCheck(lType):
    processorCheck()
    import sounddevice as sd
    recList = []
    if lType == "all":
        print(sd.query_devices())
    else:
        print("When selecting a device, use the device number.")
        print("Xavi thinks the following devices will work best for output:")
        print("")
        for number,letter in enumerate(sd.query_devices()):
            lVals = [k for k in letter.values() ]
            if number < 10:
                deviceName = lVals[0]
                if "head" in str(deviceName).lower():
                    print("Device " + str(number) + ": " + deviceName)
                if "speakers" in str(deviceName).lower():
                    print("Device " + str(number) + ": " + deviceName)
            else:
                continue
    exit()

def tempo(data):
    print("In development")
    exit()
    import numpy as np
    import scipy.io.wavfile as scpiow
    import scipy.signal as scps
    import matplotlib.pyplot as plt
    import os

    #plt.style.use('style/elegant.mplstyle')
    os.chdir('..')
    sr,aud=scpiow.read(data)
    aud = np.mean(aud, axis=1)
    N = aud.shape[0]
    L = N / sr
    M = 2096
    R = ("{0:.2f}".format(L))
    print('Audio length: %s Seconds' % R)
    spectrum = np.fft.fft(aud, axis=0)[:M // 2 + 1:-1]
    # spectrum = np.abs(spectrum)
    # freqs, times, Sx = scps.spectrogram(aud, fs=sr, window='hanning',
    #                                     nperseg=2096, noverlap=M - 100,
    #                                     detrend=False, scaling='spectrum')
    # f, ax = plt.subplots(figsize=(4.8, 2.4))
    # ax.pcolormesh(times, freqs / 1000, 10 * np.log10(Sx), cmap='viridis')
    # ax.set_ylabel('Frequency [kHz]')
    # ax.set_xlabel('Time [s]');
    plt.show()
    exit()

def toMono(data):
    print("In development.")
    exit()
    import numpy as np
    import scipy.io.wavfile as scpiow
    import scipy.signal as scps
    import os
    try:
        sr,aud=scpiow.read(data)
    except FileNotFoundError:
        print("File not found!")
        exit()
    aud = np.mean(aud, axis=1) 
    scpiow.write(str(data + '_mono.wav'), sr, aud)   
    exit()
