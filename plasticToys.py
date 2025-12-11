from toys import Toys

class PlasticToys(Toys):
    def __init__(self, name, owner, plastic):
        super().__init__(name, owner)
        self.__plastic = plastic

    def createToys(self):
        return f"При создании игрушки {self.getName()} было использовано {self.__plastic} пластика"
    
    def getPacking(self):
        return self.__plastic