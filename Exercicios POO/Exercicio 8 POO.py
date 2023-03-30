class Macaco():
    
    def __init__(self, nome):
        self.nome = nome
        self.barriga = []

    def comer(self, comida):
        self.barriga.append(comida)

    def verbarriga(self):
        print("barriga: ", self.barriga)

    def digerir(self):
        if (len(self.barriga) > 0):
            self.barriga.pop(0)
    

m1 = Macaco("Macaco 1")
m2 = Macaco("Macaco 2")

m1.comer("Uva")
m1.verbarriga()
m1.comer("Banana")
m1.verbarriga()
m1.comer("Bananinha")
m1.verbarriga()
m1.digerir()
m1.verbarriga()
m1.comer(m2)
m1.verbarriga()

m2.comer("Uva")
m2.comer("Banana")
m2.comer(m1)
m2.verbarriga()
