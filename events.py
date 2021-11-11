class Events(all):
    def __init__(self, numberId, name, requierement, probability, description):
        super().__init__(numberId, name)
        self.requirement = requierement
        self.probability = probability
        self.description = description


class Discovery(Events):
    def __init__(self, numberId, name, requierement, probability, description, typeOfDiscover):
        super().__init__(numberId, name, requierement, probability, description)
        self.typeOfDiscover = typeOfDiscover

class ObjectDiscover(Discovery):
    def __init__(self, numberId, name, requierement, probability, description, typeOfDiscover):
        super().__init__(numberId, name, requierement, probability, description, typeOfDiscover)


class Encouters(Events):
    def __init__(self, numberId, name, requierement, probability, description, numberEntity):
        super().__init__(numberId, name, requierement, probability, description)
        self.numberEntity = numberEntity
    
class HumanEncounter(Encouters):
    def __init__(self, numberId, name, requierement, probability, description, numberEntity, interactionType):
        super().__init__(numberId, name, requierement, probability, description, numberEntity)
        self.interactionType = interactionType
        self.
    


"""
Le personnage est dans une clairière, il voyage pour trouver son destin, comme dans un RPG sur table classique.
Sur sa route, il rencontrera des évênements qui le pousseront à prendre des choix.
Il pourra également posséder des objets.


Situations : Elements qui modifient les conditions dans lequel le personnage évolue.
Exemple : Pluie, Chaleur, Stress, ...
Impact un element du joueur ?
"""