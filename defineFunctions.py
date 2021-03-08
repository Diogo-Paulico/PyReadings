import pickle, json
from powerSpot import powerSpot

FILENAME = 'power.info' 

consumptionPlaces = {}
choosenPlace = None

defaultLanguage = "en"
choosenLanguage = None

lang = None


def initLang():
    global choosenLanguage
    if not choosenLanguage:
        choosenLanguage = defaultLanguage
    

def toggleLanguage():
    global choosenLanguage
    if choosenLanguage == "en":
        choosenLanguage = "pt"
    elif choosenLanguage == "pt":
        choosenLanguage = "en"


def getString(id):
    return lang[choosenLanguage][id]

def save():
    global choosenLanguage

    saveFile = {"1": consumptionPlaces,
                    "0": choosenLanguage}    
    fd = open(FILENAME, 'wb')
    pickle.dump(saveFile, fd)
    fd.close()
    return True


def load():
    global lang
    with open('languages.json') as json_file:
        lang = json.load(json_file)
    try:
        global consumptionPlaces, choosenLanguage
        fd = open(FILENAME, 'rb')
        saveFile = pickle.load(fd)
        choosenLanguage = saveFile["0"]
        consumptionPlaces = saveFile["1"]
        #consumptionPlaces = pickle.load(fd)
        fd.close()
    except OSError:
        initLang()
        print('No consumption places file found!')


def createNewPowerPlace(name, cpe, nif, type): 
    consumptionPlaces[name] = powerSpot(name, cpe, nif, type)


def resetChoosenPlace():
    global choosenPlace
    choosenPlace = None


def anyPlace():
    return len(consumptionPlaces) != 0


def getReadingArgs():
    return choosenPlace.getReadingArgs()


def getChoosenPlaceCPE():
    return str(choosenPlace.cpe)


def getChoosenPlaceNIF():
    return str(choosenPlace.nif)


def updateReading(*argv):
    return choosenPlace.updateReading(*argv)


def getLastReading():
    return choosenPlace.getLastReading()


def choosePowerSpot(name):
    try:
        global choosenPlace
        choosenPlace = consumptionPlaces.get(name)
    except KeyError:
        return False


def getAllPowerSpotsName():
    lista = list(consumptionPlaces.keys()) 
    lista.sort()
    return lista


def deletePowerSpot(name):
    del consumptionPlaces[name]


def checkIfPlaceDoesNotExist(key):
    return not anyPlace() or  key not in consumptionPlaces






