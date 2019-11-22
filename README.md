# Xavi
Read the ongoing notes [here](http://bit.do/xavinotes)  
[![codebeat badge](https://codebeat.co/badges/1d581795-499a-4b58-9ba4-f51ab8f48f31)](https://codebeat.co/projects/github-com-simloads-xavi-master)

### Welcome, Git Cloners!
If you're cloning this repo, ensure you use
```
git clone https://github.com/SimLoads/xavi/ --branch setup --single-branch
```
to prevent the cloning of random things that you don't need.

### If you encounter the error "ImportError: DLL Load Failed..."

If you hit     
```
from ._ufuncs import *
  File "_ufuncs.pyx", line 1, in init scipy.special._ufuncs
ImportError: DLL load failed: The specified module could not be found.
```
There is now a fix for this! Re-run 'SetupScript' again and suspend execution on the prompt. Enter 'c' and let the installer finish. Once it exits, use
```
pip install -r requirements.txt
```
This will install the dependencies regularly and should fix this error. 

## What can Xavi do?
Xavi is designed with simplicity in mind and will do its best to automate as many processes as possible. Here's a small feature list that you can use right now: 
+ NO DEPENDENCIES LEFT BEHIND - Automatic install of packages needed by Xavi (handled by the installer) 
+ Send either a file or live microphone input to two output devices in real-time
+ Figure out tempos of songs, to the nearest 10 or so
+ Generate test tones of a certain length and frequency
+ Powerful command line input processing with parameters and non-order-specific delimiters
+ Can just play music regularly too.
+ Simple updating of code

## Getting started with Xavi
To start, download 'ScriptSetup.py' and run it in the target directory.


When the install is complete, you can use Xavi by using the _Stop 'N' Swap System_, XaviSNS.

Here's an example of a command:
```
XaviSNS.py -c testwave -f test1 -l 1 -r 1000
```
Here, we're calling the 'testwave' function which generates a tone. We're saving the output to a file called 'test1', with a 1 second length and frequency of 1000 Hz. If you need help with parameters, simply type:  
```
XaviSNS.py -h
```


Here's another example. If we want to send the sound of 'test1.wav' to both my headphones and my speakers, we can use Livebridge. To begin, let's take a look at my available devices.
```
XaviSNS.py -c livebridge
```
Passing the livebridge function with no arguments returns a list of recommended devices. In my case, my speakers are device '4' and my headphones are device '6'. I can then send these, along with the file, to livebridge.
```
XaviSNS.py -c livebridge -f test1.wav -fd 4 -sd 6
```
This plays the sound to both devices simultaneously. 


Xavi makes use of and can download the following packages: 

[This wonderful precompiled version of PyAudio](https://github.com/intxcc/pyaudio_portaudio) by [intxcc](https://github.com/intxcc)  
[This awesome low pass filter](https://gist.github.com/piercus/b005ed5fbc70761bde96) by [piercus](https://github.com/piercus)  
[BeautifulSoup4](https://www.pypi.org/project/beautifulsoup4/)  
[Sounddevice](https://www.pypi.org/project/sounddevice/)  
[SciPy](https://www.scipy.org/)  
[NumPy](https://www.numpy.org/)  
[Matplotlib](https://matplotlib.org/)  
[Filetype](https://pypi.org/project/filetype)  
[Six](https://pypi.org/project/six/)  
[Pyparsing](https://pypi.org/project/pyparsing/)  
[Libpng](http://www.libpng.org/pub/png/libpng.html)  
[Freetype](https://www.freetype.org/)  
[Kiwisolver](https://pypi.org/project/kiwisolver/)  
[Dateutil](https://pypi.org/project/python-dateutil/)  
[Cycler](https://pypi.org/project/Cycler/)  


