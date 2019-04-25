'''

Xavi Standard Audio Service
Main Tools

Author:: Sam F // PyGoose // https://github.com/SimLoads
Version:: 042419.1x0002

/NOTES/



'''
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
    if "audio" in fType:
        print(filename + " is a supported format.")
        return()
    else:
        print("Unsupported format.")