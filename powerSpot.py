from os import read
import simpleReading as sr
import biHorarioReading as br
import triHorarioReading as tr
from datetime import date

class powerSpot:
    def __init__(self, name, cpe, nif, typeOfMeter):
        self.name = name
        self.cpe = cpe
        self.nif = nif
        self.typeOfMeter = typeOfMeter

        readingObject = None
        
        if typeOfMeter == 1:
                readingObject = sr.makeSimpleReading(0)
        elif typeOfMeter == 2:
                readingObject = br.makeBiHorarioReading(0,0)
        elif typeOfMeter == 3:
                readingObject = tr.makeTriHorarioReading(0,0,0)
  
        
        # if typeOfMeter == 1:
        #     if(len(argv) == 0):
        #         readingObject = simpleReading(0)
        #     elif (len(argv) == 1):
        #         readingObject = simpleReading(argv[0])
        # elif typeOfMeter == 2:
        #     if(len(argv) == 0):
        #         readingObject = biHorarioReading(0,0)
        #     elif (len(argv) == 2):
        #         readingObject = biHorarioReading(argv[0], argv[1])
        # elif typeOfMeter == 3:
        #     if(len(argv) == 0):
        #         readingObject = triHorarioReading(0,0,0)
        #     elif (len(argv) == 3):
        #         readingObject = triHorarioReading(argv[0], argv[1], argv[2])
       
        self.lastReading = readingObject
        self.lastReadingDate = date.today().strftime("%d/%m/%Y")

    def updateReading(self, *argv):
        try:
            self.lastReading.updateReading(*argv)
            self.lastReadingDate = date.today().strftime("%d/%m/%Y")
        except ValueError:
            return False


    def getLastReading(self):
        reading = self.lastReading.getLastReading()
        reading["data"] = self.lastReadingDate
        return reading

    def getReadingArgs(self):
        if type(self.lastReading) is sr:
            return ["Simples"]
        elif type(self.lastReading) is br:
            return ["Vazio", "Fora Vazio"]
        elif type(self.lastReading) is tr:
            return [ "Cheias", "Vazio", "Ponta"]
