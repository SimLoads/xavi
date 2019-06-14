# Xavi
Read the ongoing notes [here](http://bit.do/xavinotes)  
[![codebeat badge](https://codebeat.co/badges/1d581795-499a-4b58-9ba4-f51ab8f48f31)](https://codebeat.co/projects/github-com-simloads-xavi-master)

### Welcome, Git Cloners!
If you're cloning this repo, ensure you use
```
git clone https://github.com/SimLoads/xavi/ --branch setup --single-branch
```
to prevent cloning of random things that you don't need.

### If you encounter the error "ImportError: DLL Load Failed..."

If you hit     
```
from ._ufuncs import *
  File "_ufuncs.pyx", line 1, in init scipy.special._ufuncs
ImportError: DLL load failed: The specified module could not be found.
```
Please let me know. As far as I'm aware this is an issue out of my control, caused by, get this, the make of your CPU. Intel machines shouldn't have this problem and I'm working on a fix for AMD based PCs. Raise an issue if you get this, I need to know if it's just me.


### Xavi is currently in development. Some features probably won't work!
#### Currently, Xavi.exe doesn't do anything. Don't rely on it for actual usage.


## What can Xavi do?
Xavi is designed with simplicity in mind, and will do its best to automate as many processes as possible. Here's a small feature list that you can use right now: 
+ NO DEPENDENCIES LEFT BEHIND - Automatic install of packages needed by Xavi (handled by installer) 
+ Sending an input file to dual outputs of choice (working on live microphone dual outputs and more than 2 outputs at a time)
+ Generate test tones of a certain length and frequency
+ Identify if a file is supported or not
+ Powerful command line input processing with parameters and non order-specific delimiters
+ Can just play music regularly too.
+ Simple updating of code

## Getting started with Xavi
To start, download either 'ScriptSetup.py' or 'XaviInstaller.exe'. They both do the same thing, but sometimes a GUI is nice to look at.  
You're going to need > Python 3.5 installed on your PATH to use XaviInstaller.exe, else you can just point Python to ScriptSetup and it should install just fine.  


When the install is complete, you can use Xavi by running Xavi.exe or by sending it commands directly. To make things easier for external programs, Xavi is never accessed directly. You'll need to send scripts to the _Stop 'N' Swap System_, which you'll find under XaviSNS.py  

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


