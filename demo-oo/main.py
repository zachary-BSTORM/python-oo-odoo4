from animal import Animal
from car import Car
from person import Person
from computer import Computer


if __name__ == "__main__":
    c_1 = Computer("dell")
    
    print(c_1.brand)
    
    c_1.brand = "nouvelle marque"
    
    print(c_1.brand)
    
    del c_1.brand
    
    print(c_1.brand)

    
