import pickle as saver
from powerSpot import powerSpot

FILENAME = 'consumptionplaces.power' 

consumptionPlaces = {}
choosenPlace = None


def save():
    fd = open(FILENAME, 'w')
    saver.dump(consumptionPlaces, fd)
    fd.close()
    return True

def load():
    try:
        fd = open(FILENAME, 'r')
        consumptionPlaces = saver.load(fd)
        fd.close()
    except OSError:
        print('No consumption places file found!')

def createNewPowerPlace(name, cpe, nif, type): 
    consumptionPlaces[name] = powerSpot(name, cpe, nif, type)


def resetChoosenPlace():
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
        choosenPlace = consumptionPlaces[name]
    except KeyError:
        return False

def getAllPowerSpotsName():
    return list(consumptionPlaces.keys())

def deletePowerSpot(name):
    del consumptionPlaces[name]





