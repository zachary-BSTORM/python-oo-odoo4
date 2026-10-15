from animal import Animal

class Elephant(Animal):
    """
    informations
    """
    
    def __init__(self,nom : str,appetit : int,satisfaction : int,en_vie : bool,soigneur : Soigneur,longueur_defense):
        super().__init__(nom, appetit,satisfaction,en_vie,soigneur)
        self.longueur_defense = longueur_defense
        
        
    def prendre_bain_boue(self):
        return f" {self.nom} prend un bain de boue "
    
    def aspirer_eau(self):
        return f" {self.nom} aspire de l'eau "
        
