###PASSO 2###

class Hit():

    def __init__(self, idmod, idsens, tsriv):
        self.idmod = idmod
        self.idsens = idsens
        self.tsriv = tsriv

    def __lt__(self, other):
        return self.tsriv < other.tsriv

    def __gt__(self, other):
        return self.tsriv > other.tsriv

    def __eq__(self, other):
        return self.tsriv == other.tsriv

