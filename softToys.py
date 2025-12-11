from toys import Toys

class SoftToys(Toys):
    def __init__(self, name, owner, packing):
        super().__init__(name, owner)
        self.__packing = packing

    def createToys(self):
        return f"При создании игрушки {self.getName()} было использовано {self.__packing} набивки"
    
    def getPacking(self):
        return self.__packing