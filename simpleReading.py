class simpleReading:
    def __init__(self, simples):
        self.simples = simples

    def updateReading(self, simples):
        if simples >= self.simples:
            self.simples = simples
        else:
            raise ValueError

def makeSimpleReading(simples):
    simple = simpleReading(simples)
    return simple
    
def getLastReading(self):
     return {
      "simples": self.simples
        }