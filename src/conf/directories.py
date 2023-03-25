import os

verbose : bool = False

PATH_HOME   = "music-box"
PATH_DB     = "db/"
PATH_AUDIO  = PATH_DB + "audio/"
PATH_PDF    = PATH_DB + "music_sheets_pdf/"
PATH_UNFILTERED = PATH_DB + "no_filter/"
PATH_WEB    = "html/"
PATH_SCRIPTS= "scripts/"
PATH_SRC    = "src/"
PATH_CONV   = PATH_SRC + "convert/"
PATH_EVAL   = PATH_SRC + "evaluation/"
PATH_MUSIC  = PATH_SRC + "music/"
PATH_CONF   = PATH_SRC + "conf/"

def __gohome():
    if verbose: print("___GOHOME___")
    current = os.getcwd()
    if verbose: print(current)
    if current.find(PATH_HOME) == -1:
        raise FileNotFoundError("Executant desde fora del directori de la aplicació")
    list = current.split(PATH_HOME)
    if list[len(list) - 1] == '':
        return
    if verbose: print("Len: " + str(len(list)))
    local = list[len(list) - 1]
    if verbose: print(PATH_HOME + local)
    command = local.count("/") * "../"
    os.chdir(command)


def goto(path=None):
    if verbose: print("___GOTO___")
    __gohome()
    if verbose: print(os.getcwd())
    if path == None:
        return
    os.chdir(path)
    if verbose: print(os.getcwd())


def musical_properties() -> list :
    goto(PATH_MUSIC)
    return os.listdir()


'''
Testing
goto()
print("\n\n")
goto(PATH_PDF)

'''
#print(musical_properties())