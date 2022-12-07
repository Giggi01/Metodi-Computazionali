class Hit():

    def __init__(self, idmod, idsens, tsriv):
        self.idmod = idmod
        self.idsens = idsens
        self.tsriv = tsriv

    def __lt__(self, other):
        retunr self.tsriv < other.tsriv

    def __gt__(self, other):
        retunr self.tsriv > other.tsriv

        
class Event():

    def __init__(self, hit):
        self.hit = hit

    def arrhit(self,hit):
        arrhit = np.arr([])
        arrhit = np.append(arrhit, self.hit)
        dt = arrhit[len(arrhit)].tsriv - arrhit[0].tsriv
        return arrhit, arrhit[0].tsriv, arrhit[len(arrhit)].tsriv, len(arrhit), 
        
        
        

    
    
