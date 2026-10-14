   
class Enclos:
    def __init__(self,name,capacity,size):
        self.name = name
        self.capacity = capacity
        self.__size = size
        self.__animals = []

    @property
    def size(self):
        return self.__size
    
    @property
    def animals(self):
        return self.__animals
        
    def add_animal(self,animal):
        self.animals.append(animal)
        
    def remove_animal(self,animal):
        self.animals.remove(animal)
        
    def show_animals(self):
        for a in self.animals:
            print(f"animal : {a.nom} - {a.appetit} hungry - {a.satisfaction} happy")
        
    def pass_day(self):
        for a in self.animals:
            a.fatigue()