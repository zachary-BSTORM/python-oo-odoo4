class Person:
    def __init__(self,name : str,email : str,password:str,age:int):
        self.name = name
        self._email = email
        self.__password = password
        self.age = age
        
    def get_password(self):
        return self.__password
    
    def set_password(self,value):
        self.__password = value