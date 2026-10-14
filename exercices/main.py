from elephant import Elephant
from soigneur import Soigneur
from enclos import Enclos


if __name__ == "__main__":
    
    continue_loop = True
      
    bob = Soigneur("bob",2000,10,10,"elephant",1)
    john = Soigneur("John",2000,10,10,"elephant",1)

    djumbo = Elephant("djumbo",100,100,True,bob)
    babar = Elephant("babar",100,100,True,bob)

    enclos_1 = Enclos("enclos éléphant",20,200)
    print("------ ajout ----------")
    enclos_1.add_animal(djumbo)
    enclos_1.add_animal(babar)
    
    # print("------ remove ----------")
    # enclos_1.remove_animal(djumbo)
    
    # print("------ entretenir ----------")
    # bob.nourir(djumbo)
    # bob.entretenir(babar)
    

    

    while continue_loop:
        print("shows animals - 1")
        print("add animal - 2")
        print("remove animal - 3")
        print("pass day - 4")
        
        choice = input("Entrez votre choix : ")
        
        match choice:
            case "1":
                enclos_1.show_animals()
                
            case "2":
                print("Ajout d'un elepant")
                
                name = input("Nom de l'éléphant : ")
                appetit = int(input("appetit de l'éléphant : "))
                satisfaction = int(input("satisfaction de l'éléphant : "))
                
                soigneur = input("Quel est le soigneur de l'animal : 1 = bob - 2 = john")
                
                new_animal = Elephant(name,appetit,satisfaction,True,bob if soigneur =="1" else john)
                
                enclos_1.add_animal(new_animal)
                
            case "3":
                enclos_1.show_animals()
                name_to_delete = input("Entrez le nom de l'animal à retirer : ")
            
            case "4":
                enclos_1.pass_day()        
                        
            case _:
                print("Aucune action prévu")