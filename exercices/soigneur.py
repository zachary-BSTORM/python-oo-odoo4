from datetime import date

class Soigneur:
    def __init__(self,nom,year,month,day,experience,nb_animaux_responsable):
        self.nom = nom
        self.__date_naissance = date(year,month,day)
        self.__experience = experience
        self.__nb_animaux_responsable = nb_animaux_responsable
        self.animaux = []
        
    @property
    def date_naissance(self):
        return self.__date_naissance
    
    @property
    def experience(self):
        return self.__experience
    
    @property
    def nb_animaux(self):
        return self.__nb_animaux_responsable
    
    @property
    def age_soigneur(self):
        return date.today().year - self.date_naissance.year
        
    def nourir(self,animal ):
        if animal.soigneur == self:
            animal.manger()
        else:
            print("Ce soigneur n'est pas responsable de cet animal")
        
    def entretenir(self,animal):
        if animal.soigneur == self:
            animal.soigner()
        else:
            print("Ce soigneur n'est pas responsable de cet animal")

        
        