'''

Xavi Standard Audio Service
Installer

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 042419.4x0001

/NOTES/



'''
import sys
import os
import urllib.request
import re
import glob
import zipfile
def unpack(branch,files,rep,trees):
    for number,letter in enumerate(files):
        if (((letter.split('/')[-1])).lower()) == "license":
            continue
        if (((letter.split('/')[-1])).lower()) == ".gitignore":
            continue
        print("Downloading " + (letter.split('/')[-1]) + "...")
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
        print("Installed Xavi.")
        exit()
    if "xavi_filetype_mod" in os.getcwd():
        os.mkdir("types")
        os.chdir("types")
        runTotal("https://github.com/SimLoads/xavi/tree/filetype-mod/types")
    if not os.path.exists("xavi_filetype_mod"):
        os.mkdir("xavi_filetype_mod")
        os.chdir("xavi_filetype_mod")
        runTotal("https://github.com/SimLoads/xavi/tree/filetype-mod")
    #exit()
try:
    from bs4 import *
except:
    print("Downloading BeautifulSoup4 locally...")
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
            print("Download failed. Please download bs4 manually and try again.")
            exit()
    except:
        print("Unexpected error.")
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
runTotal("https://github.com/SimLoads/xavi")