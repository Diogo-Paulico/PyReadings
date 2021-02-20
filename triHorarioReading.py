class triHorarioReading:
    def __init__(self, cheias, vazio, ponta):
        self.cheias = cheias
        self.vazio = vazio
        self.ponta = ponta

    def updateReading(self, cheias, vazio, ponta):
        if self.cheias <= cheias and self.vazio <= ponta:
            self.cheias = cheias
            self.vazio = vazio
            self.ponta = ponta
        else:
            raise ValueError

    def getLastReading(self):
        return {
            "cheias": self.cheias,
            "vazio": self.vazio,
            "ponta": self.ponta
        }


