# Xavi
Read the ongoing notes [here](http://bit.do/xavinotes)  
[![codebeat badge](https://codebeat.co/badges/b60dea8d-cf99-481e-9af5-9b87d22dd4a2)](https://codebeat.co/projects/github-com-simloads-xavi-master)

## If you encounter the error "ImportError: DLL Load Failed..."

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


Xavi makes use of and can download [Numpy](https://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) by itself, as well as the following packages: 

[Filetype](https://pypi.org/project/filetype)  
[Six](https://pypi.org/project/six/)  
[Pyparsing](https://pypi.org/project/pyparsing/)  
[Libpng](http://www.libpng.org/pub/png/libpng.html)  
[Freetype](https://www.freetype.org/)  
[Kiwisolver](https://pypi.org/project/kiwisolver/)  
[Dateutil](https://pypi.org/project/python-dateutil/)  
[Cycler](https://pypi.org/project/Cycler/)  


