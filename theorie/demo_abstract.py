from abc import ABC, abstractmethod


class Vehicule(ABC):
    
    @property
    @abstractmethod
    def serial_number(self):
        pass
    
    @abstractmethod
    def show_infos():    
        pass
    
class Moto(Vehicule):
   
   @property
   def serial_number(self):
       return "bdfqs4d56sfd465sd from moto"
   
   def show_infos(self):
       return "informations from moto"
    
class Voiture(Vehicule):
    @property
    def serial_number(self):
       return "bdfqs4d56sfd465sd from moto"
   
    def show_infos(self):
       return "informations from moto"
        
# vehicule_1 = Vehicule()
moto_1 = Moto()

print(moto_1.show_infos())
print(moto_1.serial_number)


voiture_1 = Voiture()


        
        
