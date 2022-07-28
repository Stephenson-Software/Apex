import random
from entity import Entity


# @author Daniel McCoy Stephenson
# @since June 7th, 2022
class Chicken(Entity):

    def __init__(self, name):
        Entity.__init__(self, name)
        self.energy = random.randrange(50, 100)
        self.color = (random.randrange(240, 255), random.randrange(240, 255), random.randrange(240, 255))
    
    def getEnergy(self):
        return self.energy

    def addEnergy(self, amount):
        self.energy += amount
    
    def removeEnergy(self, amount):
        self.energy -= amount

    def getColor(self):
        return self.color