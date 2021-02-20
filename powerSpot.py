from os import read
import simpleReading as sr, biHorarioReading as br, triHorarioReading as tr, datetime

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
        self.lastReadingDate = None


    def updateReading(self, *argv):
        try:
            self.lastReading.updateReading(*argv)
            self.lastReadingDate = datetime.today().strftime("%d/%m/%Y")
        except ValueError:
            return False


    def getLastReading(self):
        reading = self.lastReading.getLastReading()
        reading["date"] = str(self.lastReadingDate())
        return reading

    def getReadingArgs(self):
        if type(self.lastReading) is simpleReading:
            return ["Simples"]
        elif type(self.lastReading) is biHorarioReading:
            return ["Vazio", "Fora Vazio"]
        elif type(self.lastReading) is triHorarioReading:
            return [ "Cheias", "Vazio", "Ponta"]

    def __str__(self):
        return self.name