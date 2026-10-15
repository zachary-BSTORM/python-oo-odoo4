from abc import ABC, abstractmethod


class login(ABC):
    
    @abstractmethod
    def login(self,email,password):
        pass
    
class Crud(ABC):
    @abstractmethod
    def get_items(self):
        pass
    
    @abstractmethod
    def get_items_by_id(self,id):
        pass
    
    @abstractmethod
    def remove_item(self):
        pass
        
class User(login,Crud):
        
    def get_items(self):
        pass
    

    def get_items_by_id(self,id):
        pass
    

    def remove_item(self):
        pass
    
    def login(self,email,password):
        pass
    
    
new_user = User()

if isinstance(new_user,Crud):
    
        
        
