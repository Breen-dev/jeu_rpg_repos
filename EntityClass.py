#Entity class where everything "alive" should be
class Entity():
	def __init__(self, numberId, name):
		self.numberId = int(numberId)
		self.name = str(name)

	#getters
	def set_numberId(self, numberId):
		 self.numberId = numberId

	def set_name(self, name):
		self.name = name

	#setters
	def get_numberId(self):
		return self.numberId

	def get_name(self):
		return self.name

	#representation
	def __repr__(self):
		return str(self.numberId)

class Character(Entity):
	def __init__(self, numberId, name, health, attack):
		super().__init__(numberId, name)
		self.attack = attack

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
		if healthPoints < 1:
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
	def showMyItems(self):
		finalList = self.get_name() + " own : "
		for i in self.items:
			finalList += i + ", "
		print(finalList[:-2])

	def doAFlip(self):
		print(self.get_name() + " did a flip")

class Monster(Character):
	def __init__(self, numberId, name, health, attack, items = []):
		super().__init__(numberId, name, health, attack)
		self.items = items

#def roulette(range, lot):
#	res = randint(range[0], range[1])
#	for i in lot:
#		if res > i[0] and res < i[1]:
#			event
