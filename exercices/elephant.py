class Elephant:
    """
    informations
    """
    
    def __init__(self,nom : str,appetit : int,satisfaction : int,en_vie : bool,soigneur : Soigneur):
        self.nom = nom
        self.__appetit = appetit
        self.__satisfaction = satisfaction
        self.__en_vie = en_vie
        self.soigneur = soigneur
        
    @property
    def appetit(self):
        return self.__appetit
    

    @property
    def satisfaction(self):
        return self.__satisfaction
    
    @property
    def en_vie(self):
        return self.__en_vie
            
    @property
    def state(self):
        return (self.appetit + self.satisfaction) / 2

        
    def manger(self):
        self.__appetit = 100
        
    def soigner(self):
        self.__satisfaction = 100
        
    def fatigue(self):
        self.__satisfaction -= 30
        self.__appetit -= 30
        
