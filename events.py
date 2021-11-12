from random import *

def randomBoolean():
    boole = randint(0,1)
    if boole == 0:
        return False
    if boole == 1:
        return True

# Ici sont toutes les classes reliées aux évênements

# Un évênement a un ID comme tous les autres élements, un nom, une condition d'apparition, une probabilité d'apparition, et une description
class Events():
    def __init__(self, numberId, requierement, description):
        self.numberId = numberId
        self.description = description
        self.plage = [0 ,0]

        #Getters
    def get_numberId(self):
        return self.numberId

    def get_plage(self):
        return self.plage

    def get_requirement(self):
        return self.requirement

    def get_probability(self):
        return self.requirement

    def set_plage(self, plage):
        self.plage = plage

    def get_requirement(self):
        return self.requirement

    def IsTriggerd(self):
        print(self.description, "  ", str(self.numberId))

# Classe d'évênements 1 : Les découvertes
class ObjectDiscover(Events):
    def __init__(self, numberId, requierement, probability, description, nombreObjets):
        super().__init__(numberId, requierement, probability, description)
        self.nombreObjets = nombreObjets

class VillageDiscover(Events):
    def __init__(self, numberId, requierement, probability, description, villageSize):
        super().__init__(numberId, requierement, probability, description)
        self.villageSize = villageSize

class SpecialPlaceDiscover(Events):
    def __init__(self, numberId, requierement, probability, description):
        super().__init__(numberId, requierement, probability, description)


# Classe d'évênements 2 : Les rencontres
class Encouters(Events):
    def __init__(self, numberId, requierement, probability, description, numberEntity):
        super().__init__(numberId, requierement, probability, description)
        self.numberEntity = numberEntity

class HumanEncounter(Encouters):
    def __init__(self, numberId, requierement, probability, description, numberEntity, interactionType):
        super().__init__(numberId, requierement, probability, description, numberEntity)
        self.interactionType = interactionType

class InteractionType():
    def __init__(self, isFriendly):
        self.isFriendly = isFriendly
    
    def getFriendshipOrNot(self):
        return (self.isFriendly)

class MonsterEncounter(Encouters):
    def __init__(self, numberId, requierement, probability, description, numberEntity, isFriendly):
        super().__init__(numberId, requierement, probability, description, numberEntity)
        self.isFriendly = isFriendly
        self.interactionType = InteractionType(self.isFriendly)

    def get_interactionType(self):
        return self.interactionType.getFriendshipOrNot()

class StrangeThing(Encouters):
    def __init__(self, numberId, requierement, probability, description, numberEntity, interactionType):
        super().__init__(numberId, requierement, probability, description, numberEntity)
        self.interactionType = interactionType

# Classe d'évênements 3 : Les pièges
class ItsATrap(Events):
    def __init__(self, numberId, requierement, probability, description):
        super().__init__(numberId, requierement, probability, description)

"""
Le personnage est dans une clairière, il voyage pour trouver son destin, comme dans un RPG sur table classique.
Sur sa route, il rencontrera des évênements qui le pousseront à prendre des choix.
Il pourra également posséder des objets.


Situations : Elements qui modifient les conditions dans lequel le personnage évolue.
Exemple : Pluie, Chaleur, Stress, ...
Impact un element du joueur ?
"""
