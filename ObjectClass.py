class Item():
	#items are all the things like potions or weapons that can be wield by humans
	#mass is the amount of space it will take in the inventory
	#the owner has to be specified but to make it ownerless name it : "--nobody--"
	def __init__(self, numberId, name, mass, owner):
		self.numberId = int(numberId)
		self.name = str(name)
		self.mass = int(mass)
		self.owner = str(owner)


	#getters
	def get_numberId(self):
		return self.numberId

	def get_name(self):
		return self.name

	def get_mass(self):
		return self.mass

	def get_owner(self):
		return self.owner

	#setters
	def set_name(self, name):
		self.name = name

	def set_numberId(self, numberId):
		self.numberId = numberId

	def set_mass(self, mass):
		self.mass = mass

	def set_owner(self, owner):
		self.owner = owner

	#classFunction
	def isPicked(self):
		if get_owner() != "--nobody--":
			return True

		return False

class Consumable(Item):
	#uses are here to limit the number of time you can use the object it decrease by one each use
	#to set effects use a dictionnary with the stat name as key and the value to add to the entity's stat
	def __init__(self, numberId, name, mass, owner, uses, effects):
		super().__init__(numberId, name, mass, owner)
		self.uses = int(uses)
		self.effects = effects

	#getters
	def get_uses(self):
		return self.uses

	def get_effects(self):
		return self.effects

	#setters
	def set_uses(self, uses):
		self.uses = uses

	def set_effects(self, effects):
		self.effects = effects

	def __repr__(self):
		return string(self.name)

	#classFunction
	def showUsesLeft(self): #show the number of uses left
		if self.get_owner() != "--nobody--":
			print(self.get_name() + " of " + str(self.get_owner()) + " has " + str(self.get_uses()) + " uses left")
		else:
			print(self.get_name() + " has " + str(self.get_uses()) + " uses left")

	def isUsable(self): #return true if the object has more than one uses left else false
		if self.get_uses() < 1:
			return False

		return True

	def useItem(self): #decrement the number of uses by one
		if self.isUsable():
			self.set_uses(self.get_uses() - 1)


class Equipement(Item):
	def __init__(self, numberId, name, mass, bodyParts, durability, effects):
		super().__init__(numberId, name, mass)
		self.bodyParts = bodyParts
		self.durability = int(durability)
		self.effects = effects

	#getters
	def get_bodyParts(self):
			return self.bodyParts

	def get_effects(self):
		return self.effects

	def get_durability(self):
		return self.durability

	#setters
	def set_bodyParts(self, bodyParts):
			self.bodyParts = bodyParts

	def set_effects(self, effects):
		self.effects = effects

	def get_durability(self):
		return self.durability

	def set_durability(self, durability):
		self.durability = durability

	#classFunction
	def isBroken():
		if uses < 1:
			return True

		return False

