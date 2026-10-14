class Animal:
    """
    représente un animal 
    name : str
    color : str
    age : int
    """
    def __init__(self,name : str,color : str, age : int):
            self.name = name
            self.color = color
            self.age = age
        
    def make_noise(self):
        print(f"l'animal {self.name} fait du bruit")
        
    def get_infos(self):
        print(f"L'animal {self.name} de coleur : {self.color} est agé de {self.age}ans")
