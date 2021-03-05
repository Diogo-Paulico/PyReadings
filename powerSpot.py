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

        self.lastReading = readingObject
        self.lastReadingDate = date.today().strftime("%d/%m/%Y")

    def updateReading(self, *argv):
        try:
            self.lastReading.updateReading(*argv)
            self.lastReadingDate = date.today().strftime("%d/%m/%Y")
            return True
        except ValueError:
            return False


    def getLastReading(self):
        reading = self.lastReading.getLastReading()
        reading["data"] = self.lastReadingDate
        return reading

    def getReadingArgs(self):
        if type(self.lastReading) is sr.simpleReading:
            return ["Simples"]
        elif type(self.lastReading) is br.biHorarioReading:
            return ["Fora Vazio", "Vazio"]
        elif type(self.lastReading) is tr.triHorarioReading:
            return ["Ponta", "Vazio", "Cheias"]