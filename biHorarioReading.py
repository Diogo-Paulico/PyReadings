class biHorarioReading:
    def __init__(self, vazio, foraVazio):
         self.vazio = vazio
         self.foraVazio = foraVazio
        
def updateReading(self, vazio, foraVazio):
    if self.vazio <= vazio and self.foraVazio <= foraVazio:
        self.vazio = vazio
        self.foraVazio = foraVazio
    else:
        raise ValueError

def makeBiHorarioReading(vazio, foraVazio):
        bi = biHorarioReading(vazio, foraVazio)
        return bi

def getLastReading(self):
        return {
            "foraVazio": self.foraVazio,
            "vazio": self.vazio
            }