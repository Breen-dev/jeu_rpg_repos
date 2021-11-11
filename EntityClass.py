#Entity class where everything "alive" should be
class Entity():
	def __init__(self, numberId, name):
		self.numberId = int(numberId)
		self.name = str(name)
		self.healthPoints = int(healthPoints)
		self.family = str(family)

	#getters
	def set_numberId(self, numberId):
		 self.numberId = numberId

	def set_name(self, name):
		self.name = name

	#setters
	def get_numberId(self):
		return self.numberId

	def get_name(self, name):
		return self.name

	#representation
	def __repr__(self):
		return str(self.numberId)

class Caracter(Entity):
	def __init__(self, numberId, name, health, attack):
		super().__init__(numberId, name, health)
		self.attack = attack

	#getters
	def get_attack(self):
		return self.attack

	def set_health(self, health):
		self.health = health

	#setters
	def set_attack(self, attack):
		self.attack = attack

	def get_health(self):
		return self.health

	#classFunctions	
	def isDead(self):
		if healthPoints < 1:
			return True

		return False



