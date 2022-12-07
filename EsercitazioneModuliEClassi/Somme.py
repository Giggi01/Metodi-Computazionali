import math

class Somme:

    def __init__(self, n):
        self.n = n

    def sommeint(self):
        somme = 0
        for i in range((self.n)+1):
            somme = somme + i
        print('La somma dei primi',self.n,'numeri è', somme)

    def sommeradicinint(self):
        sommerad = 0
        for i in range((self.n)+1):
            sommerad = sommerad + math.sqrt(self.n)
        print('La radice dei primi',self.n,'numeri è:',sommerad)
