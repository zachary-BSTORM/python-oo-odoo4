from animal import Animal
from random import randint

class Elephant(Animal):
    """
    informations
    """
    
    def __init__(self,nom : str,appetit : int,satisfaction : int,en_vie : bool,soigneur ,longueur_defense):
        super().__init__(nom, appetit,satisfaction,en_vie,soigneur)
        self.longueur_defense = longueur_defense
        
        
    def prendre_bain_boue(self):
        return f" {self.nom} prend un bain de boue "
    
    def aspirer_eau(self):
        return f" {self.nom} aspire de l'eau "
    
    def hasard(self):
        print("hasard Elephant")
        
    def observer_environnement(self,value):
            print(f"{name} l'éléphant observe son environnement ")
            
    def ramasser_objet(self):
        print("l'éléphant ramasse quelque chose")
        
    def probabilite_deces(self):
         return randint(1,75)
