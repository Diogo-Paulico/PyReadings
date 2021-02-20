class simpleReading:
    def __init__(self, simples):
        self.simples = simples

    def updateReading(self, simples):
        if simples >= self.simples:
            self.simples = simples
        else:
            raise ValueError

    def getLastReading(self):
             return {
                "simples": self.simples
                }

def makeSimpleReading(simples):
    simple = simpleReading(simples)
    return simple
    
    