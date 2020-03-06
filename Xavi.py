'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 030620.1x0020
Release Version:: 0.0.2

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

# wav_file = wave.open(onm, "w")
# wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
# wav_file.writeframes(filtered.tobytes('C'))
# wav_file.close()

//
'''
def processorCheck():
    import platform
    if "amd" in (str(platform.processor())).lower():
        print("Caution! Your processor may not work as intended.")
        print("Refer to the README for info on how to fix this.")
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
        raise
        exit()
    except FileNotFoundError:
        print("File not found!")
        exit()
    try:
        waveArray = np.asarray(file[1],dtype=dtype)
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
    timer(minswait)
    sd.stop()

def get_sec(tf,mw):
    import datetime
    if tf == 'hms':
        h, m, s = mw.split(':')
        return int(m) * 60 + int(s)
    elif tf == 's':
        return str(datetime.timedelta(seconds=float(mw)))

def timer(tl):
    import time, msvcrt
    timeout = get_sec('hms', tl)
    start_time = time.time()
    print("Press any key to stop")
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                break
        if (time.time() - start_time) > timeout:
            break
    return

def wireWaitForInput(stream,ck):
    while True:
        data = stream.read(ck)
        stream.write(data, ck)

def threaded_wire(device,indevice):
    import pyaudio,threading
    ck,rt = 1024,44100
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=rt,
                    output_device_index=int(device),
                    input_device_index=int(indevice),
                    input=True,
                    output=True,
                    frames_per_buffer=ck)

    waiter = threading.Thread(target=wireWaitForInput, args=(stream,ck))
    waiter.start()
    input()
    stream.stop_stream()
    stream.close()
    p.terminate()

def dpMic(inputDevice, device1, device2):
    import os, threading, sounddevice, pyaudio
    if device1 == 'blank':
        print("Fallback to default device...")
        player = threading.Thread(target=threaded_wire, args=((sounddevice.default.device),inputDevice))
        player.start()
    else:
        if device2 == 'blank':
            print("Using first device...")
            player = threading.Thread(target=threaded_wire, args=(device1, inputDevice))
            player.start()
        else:
            print("Using both devices...")
            player = threading.Thread(target=threaded_wire, args=(device1, inputDevice))
            player2 = threading.Thread(target=threaded_wire, args=(device2, inputDevice))
            player.start()
            player2.start()
    exit()

def dpFile(device1,device2,filename,dtype):
    import os, threading, sys, sounddevice, pyaudio
    ar, sl = convNumPy(filename, dtype)
    if device1 == 'blank':
        print("Fallback to default device...")
        player = threading.Thread(target=threaded_player, args=(ar,filename,(sounddevice.default.device),sl))
        player.start()
    else:
        if device2 == 'blank':
            print("Using first device...")
            player = threading.Thread(target=threaded_player, args=(ar,filename,device1,sl))
            player.start()
        else:
            print("Using both devices...")
            player = threading.Thread(target=threaded_player, args=(ar,filename,device1,sl))
            player2 = threading.Thread(target=threaded_player, args=(ar,filename,device2,sl))
            player.start()
            player2.start()
    exit()

def livebridge(filename, inputDevice, dtype, device1, device2):
    processorCheck()
    import os, threading, sys, sounddevice, pyaudio
    if ("xavi" in os.getcwd()):
        os.chdir('..')
    if filename == 'livebridge' and inputDevice == 'blank':
        print("When selecting a device, use the device number.")
        print("Xavi thinks the following devices will work best:")
        print("")
        dvs = liveDeviceCheck('')
        for n,l in enumerate(dvs):
            print(l)
    # Microphone Input #
    elif filename == 'livebridge' and not inputDevice == 'blank':
        dpMic(inputDevice,device1,device2)
    # File Input #
    elif inputDevice == 'blank':
        dpFile(device1,device2,filename,dtype)
    else:
        print("There's been an error. Ensure you're not passing -f and -i together.")

def liveDeviceCheck(lType):
    processorCheck()
    import sounddevice as sd
    recList = []
    if lType == "all":
        print(sd.query_devices())
    else:
    
        for number,letter in enumerate(sd.query_devices()):
            lVals = [k for k in letter.values() ]
            if number < 10:
                deviceName = lVals[0]
                if "head" in str(deviceName).lower():
                    recList.append("Device " + str(number) + ": " + deviceName)
                if "speakers" in str(deviceName).lower():
                    recList.append("Device " + str(number) + ": " + deviceName)
                if "microphone" in str(deviceName).lower():
                    recList.append("Input Device " + str(number) + ": " + deviceName)
                if "input" in str(deviceName).lower():
                    recList.append("Input Device " + str(number) + ": " + deviceName)
            else:
                continue
    return recList

def createCache(splist, thld, nm):
    stringf = ("<begin:threshold=%s:name=%s:end>" %(thld,nm))
    with open((createCacheName(thld, nm)), 'w') as ch: 
        ch.write(stringf)
        for item in splist:
            ch.write("%s," % item)
        ch.close()
    print('Cached data')

def cacheload(nm,th,spacesList):
    import glob
    hit = False
    cachelist = glob.glob("*.cachefile")
    for item in cachelist:
        if str(item) == (createCacheName(th,nm)):
            hit = True
            with open (item, 'r') as chO:
                xData = chO.read()
                cachenotes = ((xData.split('begin:'))[1].split(':end')[0])
                fileTH = int(cachenotes.split('threshold=')[1].split(':')[0])
                if fileTH == th:
                    print("Using cached data")
                    usingCache = True
                    cachedata = ((xData.split('>'))[1].split(' ')[0]).split(',')
                    for item in cachedata[:-1]:
                        spacesList.append(float(item))
    if hit == False:
        for key, val in threshold_dict.items():
            if int(val) == th:
                tempo(nm,key,'False')
    return spacesList

def createCacheName(thld, nm):
    import hashlib
    stringformat = (str(thld) + nm).encode('utf-8')
    name = hashlib.sha224(stringformat).hexdigest()
    name = (name + '.cachefile')
    return str(name)

def readData(dti,sr,th,spacesList):
    thresholdDetectFlag = False
    print("Reading song...")
    time = float((len(dti)/sr))/6
    print("This will take about %d seconds" % time)
    for n,l in enumerate(dti):
        if l > th and not thresholdDetectFlag:
            spacesList.append(n / sr)
            thresholdDetectFlag = True
        if l < th:
            thresholdDetectFlag = False
            continue
        else:
            continue
    return spacesList

def tempo(data, threshold, usingCache):
    print("Getting things ready...")
    import os, time, wave, itertools, contextlib, threading, numpy as np
    from scipy.signal import argrelextrema 
    import matplotlib.pyplot as plt
    cff = 100.0 #cutoff
    try:
        dti = filter(cff,data)
    except FileNotFoundError:
        print("No such file.")
        exit()
    spacesList = []
    with contextlib.closing(wave.open(data,'rb')) as getsr:
        sr = getsr.getframerate()
    try:
        th = int(threshold_dict[threshold])
    except:
        print("Invalid threshold option: %s" % threshold)
        print("Use h, mh, m, ml, or l")
        exit()
    if usingCache == 'False': usingCache = False 
    else: usingCache = True
    if usingCache: spacesList = cacheload(data,th,spacesList)
    else: spacesList = readData(dti,sr,th,spacesList)
    print("Calculating tempo...")
    diffs = [abs(e[1] - e[0]) for e in itertools.permutations(spacesList, 2)]
    try:
        sumd = (sum(diffs)/len(diffs) / 100)
    except ValueError:
        print("Failed to calculate. Try a different threshold.")
        exit()
    except ZeroDivisionError:
        print("Threshold / Cache error. Retry without caching or with a lower threshold.")
        exit()
    avg = (((sumd * 3) + (sumd * 4) + (sumd * 2) + (sumd * 3.5)) /4) * 60
    if not usingCache:
        cacheCr = threading.Thread(target=createCache, args=(spacesList, th, data))
        cacheCr.start()
    print("Estimated tempo: %sbpm" % int(avg))
    print("If this seems incorrect, try a different threshold.")

    exit()

def filter(cff,data):
    import numpy as np,wave,sys,math,contextlib

    ### https://github.com/piercus
    with contextlib.closing(wave.open(data,'rb')) as spf:
        sampleRate = spf.getframerate()
        ampWidth = spf.getsampwidth()
        nChannels = spf.getnchannels()
        nFrames = spf.getnframes()
        signal = spf.readframes(nFrames*nChannels)
        spf.close()
        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)
        freqRatio = (cff/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)
        filtered = running_mean(channels[0], N).astype(channels.dtype)
        return filtered

def running_mean(x, windowSize):
    import numpy as np
    cs = np.cumsum(np.insert(x, 0, 0)) 
    return (cs[windowSize:] - cs[:-windowSize]) / windowSize

def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):
    import numpy as np
    if sample_width == 1:
        dtype = np.uint8
    elif sample_width == 2:
        dtype = np.int16
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")
    channels = np.fromstring(raw_bytes, dtype=dtype)
    if interleaved:
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        channels.shape = (n_channels, n_frames)
    return channels

def getSamples(data):
    print("Loading...")
    import os
    if not os.path.exists(data):
        print("File not found!")
        return
    import numpy as np
    import scipy.io.wavfile as scpiow
    import scipy.signal as scps
    dt, sr = convNumPy(data, np.int16)
    scs = (len(dt)/sr)
    print()
    print("Sample Rate: %s" % str(sr))
    print("Total Samples: %s" % str(len(dt)))
    print("Seconds: %s" % str(scs))
    print("Real time: %s" % get_sec('s', int(round(scs))))
    print()
    return

threshold_dict = {
    'h': '9790',
    'mh': '8000',
    'm': '7150',
    'ml': '6900',
    'l': '4000'
}

if __name__ == "__main__":
    print("Pass commands to Xavi using XaviSNS or XaviShell")
    timer('00:00:03')
    exit()

