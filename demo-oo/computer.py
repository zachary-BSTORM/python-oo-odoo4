class Computer:
    def __init__(self,brand):
        self.__brand = brand
        
    # accès à l'attribut pour lecture
    @property
    def brand(self):
        return self.__brand
    
    # modification de l'attribut
    @brand.setter
    def brand(self,value):
        if len(value) < 3:
            raise Exception("La marque doit faire au moins 3 caractères")
        else:
            self.__brand = value
    
    # suppression de l'attribut      
    @brand.deleter
    def brand(self):
        del self.__brand