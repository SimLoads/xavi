'''

Xavi Standard Audio Service
Installer

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 042919.4x0005

/NOTES/



'''
import sys
import os
import urllib.request
import re
import glob
import zipfile
import time
import shutil
def unpack(branch,files,rep,trees):
    for number,letter in enumerate(files):
        fileName = (((letter.split('/')[-1])).lower())
        if fileName in [".gitignore","license","readme.md", "scriptsetup.py"]:
            continue
        if not os.path.exists(fileName):
            print("Downloading " + (letter.split('/')[-1]) + "...")
        else:
            print("Updating " + (letter.split('/')[-1]) + "...")
        letterfix = (letter.split('/'))
        del letterfix[3]
        letterfix = '/'.join(letterfix)
        try:
            data = ((urllib.request.urlopen(urllib.request.Request("https://raw.githubusercontent.com" + letterfix))).read()).decode()
        except:
            try:
                downfile = ("https://raw.githubusercontent.com" + letterfix)
                filenm = ((letter.split('/')[-1]))
                urllib.request.urlretrieve(downfile, filenm)
            except:
                print("Failed to download: " + ((letter.split('/')[-1])))
        try:
            with open(((letter.split('/')[-1])), 'w', newline='') as backupwrite:
                backupwrite.write(str(data))
                backupwrite.close()
        except:
            print("Failed to download: " + ((letter.split('/')[-1])))
    if "types" in os.getcwd():
        os.chdir('..')
        os.chdir('..')
        if tImport == False:
            print("Cleaning up...")
            try:
                bs4l = glob.glob("b*/")
                for number,letter in enumerate(bs4l):
                    shutil.rmtree(letter, ignore_errors=True)
            except:
                pass
        try:
            import numpy
        except:
            if not os.path.exists("numpy"):
                print("Fetching required packages...")
                getNumpy()
            else:
                print("No need to redownload packages.")
                print("Xavi updated successfully.")
                time.sleep(2)
                exit()
        try:
            import matplotlib.pyplot
        except:
            if not os.path.exists("matplotlib"):
                print("Fetching required packages...")
                getNumpy()
            else:
                print("No need to redownload packages.")
                print("Xavi updated successfully.")
                time.sleep(2)
                exit()
        print("Xavi installed successfully.")
        time.sleep(2)
        exit()
    if "xavi_filetype_mod" in os.getcwd():
        try:
            os.mkdir("types")
        except:
            pass
        os.chdir("types")
        runTotal("https://github.com/SimLoads/xavi/tree/filetype-mod/types")
    if not os.path.exists("xavi_filetype_mod"):
        os.mkdir("xavi_filetype_mod")
        os.chdir("xavi_filetype_mod")
        runTotal("https://github.com/SimLoads/xavi/tree/filetype-mod")
    else:
        os.chdir("xavi_filetype_mod")
        runTotal("https://github.com/SimLoads/xavi/tree/filetype-mod")
    #exit()
global tImport
try:
    from bs4 import *
    tImport = True
except:
    print("Downloading BeautifulSoup4 locally...")
    tImport = False
    try:
        url = 'https://files.pythonhosted.org/packages/1d/5d/3260694a59df0ec52f8b4883f5d23b130bc237602a1411fa670eae12351e/beautifulsoup4-4.7.1-py3-none-any.whl'  
        urllib.request.urlretrieve(url, 'bs4.whl')
        os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
        zipx = zipfile.ZipFile(((glob.glob("*.zip"))[0]), 'r')
        zipx.extractall(os.getcwd())
        zipx.close()
        try:
            os.remove("bs4.whl.zip")
        except:
            pass
        try:
            from bs4 import *
        except:
            print("There was an error during download.")
            print("Check your connection, or try and install bs4 manually using")
            print("pip install bs4")
            input()
            exit()
    except:
        print("There was an error during download.")
        print("Check your connection, or try and install bs4 manually using")
        print("pip install bs4")
        input()
        exit()
def runTotal(rep):
    html_page = urllib.request.urlopen(rep)
    linksplit = rep.split('/')
    username = linksplit[3]
    repnm = linksplit[4]
    soup = BeautifulSoup(html_page, features="html.parser")
    files = []
    trees = []
    for link in soup.findAll('a', attrs={'href': re.compile("^/" + username + "/" + repnm + "/blob")}):
        files.append(link.get('href'))
    for link in soup.findAll('a', attrs={'href': re.compile("^/" + username + "/" + repnm + "/tree")}):
        trees.append(link.get('href'))
    branch = ((files[0]).split('/'))[-2]
    unpack(branch,files,rep,trees)
def getNumpy():
    url = "https://files.pythonhosted.org/packages/4e/9d/c129d78e6b942303b762ccfdf1f8339de80c5e6021b14ef0c99ec5bdc6aa/numpy-1.16.3-cp37-cp37m-win_amd64.whl"
    print("Got Numpy URL...")
    urllib.request.urlretrieve(url, 'numpy.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile(((glob.glob("*.zip"))[0]), 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    getMatlib()
def getMatlib():
    url = "https://files.pythonhosted.org/packages/13/ca/8ae32601c1ebe482b140981eedadf8a927de719ca4cecc550b12a4b78f2d/matplotlib-3.0.3-cp37-cp37m-win_amd64.whl"
    print("Got Matplotlib URL...")
    urllib.request.urlretrieve(url, 'matlib.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile(((glob.glob("*.zip"))[0]), 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    print("Fetching matplotlib dependancies")
    os.chdir('matplotlib')
    getMatlibDeps()
def getMatlibDeps():
    depurls = [
    #Pyparsing Works
    "https://files.pythonhosted.org/packages/dd/d9/3ec19e966301a6e25769976999bd7bbe552016f0d32b577dc9d63d2e0c49/pyparsing-2.4.0-py2.py3-none-any.whl", 
    #libpng
    "https://downloads.sourceforge.net/project/libpng/libpng16/1.6.37/lpng1637.zip", 
    #Freetype
    "https://downloads.sourceforge.net/project/freetype/freetype2/2.10.0/ft2100.zip", 
    #Kiwisolver Works
    "https://files.pythonhosted.org/packages/c6/ea/e5474014a13ab2dcb5056608e0716c600c3d8a8bcffb10ed55ccd6a42eb0/kiwisolver-1.1.0-cp37-none-win_amd64.whl", 
    #Dateutil Works
    "https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl", 
    #Cycler works
    "https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl"]
    for number, letter in enumerate(depurls):
        urlSplit = letter.split('/')
        if ".zip" in letter[5:]:
            nameStr = (urlSplit[-1])
            needWheel = False
        else:
            nameStr = (urlSplit[-1] + ".whl")
            needWheel = True
        urllib.request.urlretrieve(letter, nameStr)
        if needWheel == True:
            os.rename(nameStr, (nameStr + ".zip"))
        if needWheel == True:
            zipx = zipfile.ZipFile((nameStr + ".zip"), 'r')
        else:
            zipx = zipfile.ZipFile((nameStr), 'r')
        print("Extracting " + nameStr + "...")
        zipx.extractall(os.getcwd())
    zipx.close()
    packageCleanup()
def packageCleanup():
    for x in range (2):
        zips, whls, pth, dsti = glob.glob("*.whl.zip"), glob.glob("*.whl"), glob.glob("*.pth"), glob.glob("*dist-info/")
        for number,letter in enumerate(zips):
            print("Removing " + letter + "...")
            try:
                os.remove(letter)
            except:
                pass
        for number,letter in enumerate(whls):
            print("Removing " + letter + "...")
            try:
                os.remove(letter)
            except:
                pass
        for number,letter in enumerate(pth):
            print("Removing " + letter + "...")
            try:
                os.remove(letter)
            except:
                pass
        for number,letter in enumerate(dsti):
            print("Removing " + letter + "...")
            shutil.rmtree(letter, ignore_errors=True)
        os.chdir('..')
    print("Installed Xavi.")
    time.sleep(2)
    exit()

runTotal("https://github.com/SimLoads/xavi")