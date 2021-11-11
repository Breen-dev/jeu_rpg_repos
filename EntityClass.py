#Entity class where everything "alive" should be
class Entity():
	def __init__(self, numberId, name):
		self.numberId = int(numberId)
		self.name = str(name)

	#getters
	def get_numberId(self):
		return self.numberId

	def get_name(self):
		return self.name

	#setters
	def set_numberId(self, numberId):
		 self.numberId = numberId

	def set_name(self, name):
		self.name = name

	#representation
	def __repr__(self):
		return str(self.numberId)

class Character(Entity):
	def __init__(self, numberId, name, health, attack):
		super().__init__(numberId, name)
		self.health = int(health)
		self.attack = int(attack)

	#getters
	def get_attack(self):
		return self.attack

	def get_health(self):
		return self.health

	#setters
	def set_attack(self, attack):
		self.attack = attack

	def set_health(self, health):
		self.health = health

	#classFunctions	
	def isDead(self):
		if self.get_health() < 1:
			return True

		return False

class Human(Character):
	def __init__(self, numberId, name, health, attack, items = []):
		super().__init__(numberId, name, health, attack)
		self.items = items

	#getters
	def get_items(self):
		return self.items

	#setters
	def set_items(self, items):
		self.items = items

	#classFunction
	#show informations
	def showMyItems(self):
		finalList = self.get_name() + " own :\n"
		for i in self.items:
			finalList += i.get_name() + "\n"
		print(finalList)

	def showMyStats(self):
		finalList = self.get_name() + " has :\n" + str(self.get_attack()) + " ATT\n" + str(self.get_health()) + " HP\n"
		print(finalList)

	def showEverything(self):
		print("My name is " + self.get_name() + "\n")
		self.showMyStats()
		self.showMyItems()

	#use things
	def useObject(self, item):
		if not self.isDead(): #only launch the script if alive
			listOfStats = ["health", "attack"] #Only for humans be careful
			
			if item.isUsable(): #only launch the script if the item is usable
				itemEffects = item.get_effects()
				
				try:
					self.set_health(self.get_health() + itemEffects[listOfStats[0]])
				except KeyError:
					pass

				try:
					self.set_attack(self.get_attack() + itemEffects[listOfStats[1]])
				except KeyError:
					pass



	def doAFlip(self):
		print(self.get_name() + " did a flip")

class Monster(Character):
	def __init__(self, numberId, name, health, attack, capacities = []):
		super().__init__(numberId, name, health, attack)
		self.capacities = capacities

	#getters
	def get_capacities(self):
		return self.capacities

	#setters
	def set_capacities(self, capacities):
		self.capacities = capacities

	#classFunction
	def showMyCapacities(self):
		finalList = self.get_name() + " can do : "
		for i in self.capacities:
			finalList += i + ", "
		print(finalList[:-2])

