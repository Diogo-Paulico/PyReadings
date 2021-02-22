class triHorarioReading:
    def __init__(self, ponta, vazio, cheias):
        self.cheias = cheias
        self.vazio = vazio
        self.ponta = ponta

    def updateReading(self, ponta, vazio, cheias):
        if self.cheias <= cheias and self.vazio <= vazio and self.ponta <= ponta:
                self.cheias = cheias
                self.vazio = vazio
                self.ponta = ponta
        else:
                raise ValueError

    def getLastReading(self):
        return {
            "Cheias": self.cheias,
            "Vazio": self.vazio,
            "Ponta": self.ponta
        }

def makeTriHorarioReading(cheias, vazio, ponta):
    tri = triHorarioReading(cheias, vazio, ponta)
    return tri




