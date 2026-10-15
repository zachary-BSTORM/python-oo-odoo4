from animal import Animal

class Giraffe(Animal):
    def __init__(self,nom : str,appetit : int,satisfaction : int,en_vie : bool,soigneur : Soigneur,longueur_cou):
        super().__init__(nom, appetit,satisfaction,en_vie,soigneur)
        self.longueur_cou = longueur_cou
        
        
    def manger_feuilles(self):
        self.__appetit += 30
        
    def boire_eau(self):
        self.__appetit += 30
        
    def observer_environnement(self,value):
        return super().observer_environnement() + value