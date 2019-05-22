# Xavi
Read the ongoing notes [here](http://bit.do/xavinotes)  
[![codebeat badge](https://codebeat.co/badges/1d581795-499a-4b58-9ba4-f51ab8f48f31)](https://codebeat.co/projects/github-com-simloads-xavi-master)

### If you encounter the error "ImportError: DLL Load Failed..."

If you hit     
```
from ._ufuncs import *
  File "_ufuncs.pyx", line 1, in init scipy.special._ufuncs
ImportError: DLL load failed: The specified module could not be found.
```
Please let me know. As far as I'm aware this is an issue out of my control, caused by, get this, the make of your CPU. Intel machines shouldn't have this problem and I'm working on a fix for AMD based PCs. Raise an issue if you get this, I need to know if it's just me.


## Xavi is currently in development. Some features probably won't work!
Welcome to Xavi!
Please ensure you use the installer (ScriptSetup.py) to install Xavi properly.  
That tool will ensure all the required files are downloaded and put in the right place.  

## What can Xavi do?
Xavi is designed with simplicity in mind, and will do its best to automate as many processes as possible. Here's a small feature list that you can use right now: 
+ NO DEPENDENCIES LEFT BEHIND - Automatic install of packages needed by Xavi (handled by installer) 
+ Sending an input file to dual outputs of choice (working on live microphone dual outputs and more than 2 outputs at a time)
+ Generate test tones of a certain length and frequency
+ Identify if a file is supported or not
+ Powerful command line input processing with parameters and non order-specific delimiters
+ Can just play music regularly too.
+ Simple updating of code

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


