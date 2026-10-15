from typing import override


class Animal:
    def __init__(self,name : str,color : str , age : int,**kwargs):
        self.name = name
        self.color = color
        self.age = age
        
    
    def make_noise(self):
        return "The animal make noise "
        
class Breed:
    def __init__(self,breed_name : str , price : int,**kwargs):
        self.breed_name = breed_name
        self.price = price
        
    def get_information(self):
        return f"Breed : {self.breed_name} - price : {self.price}"
    
    def make_noise(self):
        return "this breed is noisy "
    
class Chien(Animal,Breed):
    def __init__(self,toy : str,hungry : bool,**kwargs):
        self.toy = toy
        self.hungry = hungry
        Breed.__init__(self,**kwargs)
        Animal.__init__(self,**kwargs)
        

    def make_noise(self):
        return "The dog make noise" + Animal.make_noise(self) + Breed.make_noise(self)
        
        
    
if __name__ == "__main__":

    rex = Chien("bones",True,name="rex",color="brun",age=5,breed_name="berger allemand",price=500)
    
    print(rex.name)
    print(rex.color)
    print(rex.age)
    print(rex.toy)
    print(rex.hungry)
    print(rex.breed_name)
    print(rex.price)
    print(rex.__dict__)
    
    print("-----------------")
    print(rex.make_noise())
    
    
    print("-----------------")
    
    print("issubClass")
    print(issubclass(Chien,Animal))
    
    print("isInstance")
    print(isinstance(rex,Chien))
    print(isinstance(rex,Animal))
    
    print("mro")
    print(Chien.__mro__)
    
    print([cls.__name__ for cls in Chien.mro()])
    