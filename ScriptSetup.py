'''

Xavi Standard Audio Service
Installer

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 052219.4x0009

/NOTES/

Fix timeout function



'''
import sys,os,urllib.request,re,glob,zipfile,time,shutil,platform,threading
global timeoutTimer 
timeoutTimer = False
def timeout():
    print("..")
    if timeoutTimer == False:
        print("This seems to be taking a long time.")
        print("Please try again later.")
        time.sleep(1)
        exit()
def unpack(branch,files,rep,trees):
    for number,letter in enumerate(files):
        fileName = (((letter.split('/')[-1])).lower())
        if fileName == ["xavisns.py","xavi.exe"]:
            os.chdir('..')
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
        if fileName == ["xavisns.py","xavi.exe"]:
            os.chdir('xavi')
    nextStep()
def nextStep():
    if "matplotlib" in os.getcwd():
        packageCleanup()
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
    t = threading.Timer(12.0, timeout)
    try:
        html_page = urllib.request.urlopen(rep)
    except:
        print("Connection error!")
        print("Ensure you're connected to the internet.")
        input()
        exit()
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
    timeoutTimer = True
    unpack(branch,files,rep,trees)
def getNumpy():
    url = "https://files.pythonhosted.org/packages/4e/9d/c129d78e6b942303b762ccfdf1f8339de80c5e6021b14ef0c99ec5bdc6aa/numpy-1.16.3-cp37-cp37m-win_amd64.whl"
    print("Got Numpy URL...")
    urllib.request.urlretrieve(url, 'numpy.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile("numpy.whl.zip", 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    getSciPy()
def getSciPy():
    url = "https://files.pythonhosted.org/packages/58/f0/d00c0e01e077da883f030af3ff5ce653a0e9e4786f83faa89a6e18c98612/scipy-1.2.1-cp37-cp37m-win_amd64.whl"
    print("Got SciPy URL...")
    urllib.request.urlretrieve(url, 'scipy.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile("scipy.whl.zip", 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    getSounddevice()
def getSounddevice():
    url = "https://files.pythonhosted.org/packages/7f/15/fd6d923adccc64d2d93fcffc245bb2471a2509bb2905a89c4fc772ce4e35/sounddevice-0.3.13-py2.py3.cp26.cp27.cp32.cp33.cp34.cp35.cp36.cp37.cp38.pp27.pp32.pp33.pp34.pp35.pp36-none-win_amd64.whl"
    print("Got SoundDevice URL...")
    urllib.request.urlretrieve(url, 'sndv.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile("sndv.whl.zip", 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    getCffi()
def getCffi():
    url = 'https://files.pythonhosted.org/packages/2f/ad/9722b7752fdd88c858be57b47f41d1049b5fb0ab79caf0ab11407945c1a7/cffi-1.12.3-cp37-cp37m-win_amd64.whl'
    print("Got Cffi URL...")
    urllib.request.urlretrieve(url, 'cffi.whl')
    print("Saved wheel in: " + os.getcwd())
    os.rename(((glob.glob("*.whl"))[0]), (((glob.glob("*.whl"))[0]) + ".zip"))
    zipx = zipfile.ZipFile("cffi.whl.zip", 'r')
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
    zipx = zipfile.ZipFile("matlib.whl.zip", 'r')
    print("Extracting...")
    zipx.extractall(os.getcwd())
    zipx.close()
    print("Fetching matplotlib dependancies")
    os.chdir('matplotlib')
    getMatlibDeps()
def getMatlibDeps():
    depurls = [
    #Six
    "https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl",
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
    print("Modifying required packages...")
    packageModify()
def packageModify():
    os.remove("fontconfig_pattern.py")
    runTotal("https://github.com/SimLoads/xavi/tree/matplotlib-mod")
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

print("Preparing setup...")
if not "windows" in (platform.platform()).lower():
    print("Xavi is currently only supported on Windows.")
    print("Linux support is in development :)")
    input()
    exit()
if not sys.version_info[0] < 3.4:
    print("Python 3.5 and above is required to use Xavi.")
    input()
    exit()
if not os.path.exists('xavi'):
    os.mkdir('xavi')
os.chdir('xavi')
print("Installing xavi in: " + os.getcwd())
print("This may take some time.")
total, used, free = shutil.disk_usage(os.getcwd())
if not (free > 314572800):
    print()
    print("Insufficient space to install Xavi!")
    print("Free up some space and try again.")
    input()
    exit()
runTotal("https://github.com/SimLoads/xavi")