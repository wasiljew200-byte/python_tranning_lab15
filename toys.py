class Toys:
    def __init__(self, name, owner):
        self.__name = name
        self.__owner = owner

    def createToys(self):
        raise NotADirectoryError("Ошибка")
    
    def info(self):
        return f"Игрушка {self.__name} принадлежит {self.__owner}"
    
    def play(self):
        return f"{self.__owner} играет с игрушкой {self.__name}"
    
    def getName(self):
        return self.__name
    
    def getOwner(self):
        return self.__owner