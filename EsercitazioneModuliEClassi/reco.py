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

    def __sub__(self, other):
        return self.tsriv - other.tsriv

    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.idmod, self.idsens, self.tsriv)

class Evento():

    def __init__(self):
        self.nhit = 0
        self.tstart = 0
        self.tstop = 0
        self.tspan = 0
        self.hits = 0

    def __gt __(self, tstart):
        return self.tstart > other.tstart

    def AggHit (self, hit):
        self.nhit += 1
        self.hits = np.append(hits, hit)
        self.tstop = hit.tsriv
        if nhit == 1:
            tstart = hit.tsriv
        self.tspan = tstop - tstart
        
    
