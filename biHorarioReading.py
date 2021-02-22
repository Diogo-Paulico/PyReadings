class biHorarioReading:
    def __init__(self, vazio, foraVazio):
         self.vazio = vazio
         self.foraVazio = foraVazio
        
    def updateReading(self, foraVazio, vazio):
        if self.vazio <= vazio and self.foraVazio <= foraVazio:
            self.vazio = vazio
            self.foraVazio = foraVazio
        else:
            raise ValueError
        
    def getLastReading(self):
        return {
            "Fora Vazio": self.foraVazio,
            "Vazio": self.vazio
            }


def makeBiHorarioReading(vazio, foraVazio):
        bi = biHorarioReading(vazio, foraVazio)
        return bi

