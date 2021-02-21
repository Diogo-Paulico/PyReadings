import pickle as saver
from powerSpot import powerSpot

FILENAME = 'consumptionplaces.power' 

consumptionPlaces = {}
choosenPlace = None


def save():
    fd = open(FILENAME, 'wb')
    saver.dump(consumptionPlaces, fd)
    fd.close()
    return True

def load():
    try:
        global consumptionPlaces
        fd = open(FILENAME, 'rb')
        consumptionPlaces = saver.load(fd)
        fd.close()
    except OSError:
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


def updateReading(*argv):
    choosenPlace.updateReading(*argv)

def getLastReading():
    return choosenPlace.getLastReading()

def choosePowerSpot(name):
    try:
        global choosenPlace
        choosenPlace = consumptionPlaces.get(name)
    except KeyError:
        return False

def getAllPowerSpotsName():
    lista = list(consumptionPlaces.keys()) #THIS NEEDS TO BE DONE CAUSE THE LIST IS SORTED IN PLACE DOESNT RETURN SORTED LIST
    lista.sort()
    return lista

def deletePowerSpot(name):
    del consumptionPlaces[name]

def checkIfPlaceDoesNotExist(key):
    return not anyPlace() or  key not in consumptionPlaces






