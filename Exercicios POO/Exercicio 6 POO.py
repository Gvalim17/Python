class TV:
    def __init__(self):
        self.mcanal (0)
        self.volume = 0
    
    def mcanal(self, canal):
        if canal > 0  and canal <= 100:
            self.canal = canal
    
    def aumentar_volume(self):
        if self.volume < 50:
            self.volume += 1
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
    
    

tv = TV()
print(vars(tv))
tv.mcanal(20)
print(vars(tv))
tv.aumentar_volume()
print(vars(tv))
tv.diminuir_volume()
print(vars(tv))