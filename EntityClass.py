#Entity class where everything "alive" should be
class Entity():
	def __init__(self, numberId, name, healthPoints, family):
		self.numberId = int(numberId)
		self.name = str(name)
		self.healthPoints = int(healthPoints)
		self.family = str(family)

	#getters
	def get_healthPoints(self):
		return self.healthPoints

	def get_family(self):
		return self.family

	def set_numberId(self, numberId):
		 self.numberId = numberId

	def set_name(self, name):
		self.name = name

	#setters
	def set_healthPoints(self, healthPoints):
		self.healthPoints = healthPoints

	def set_family(self, family):
		self.family = family

	def get_numberId(self):
		return self.numberId

	def get_name(self, name):
		return self.name

	def __repr__(self):
		return str(self.numberId)

	#representation
	def __repr__(self):
		return str(self.numberId)


	#classFucntions
	def isDead(self):
		if healthPoints < 1:
			return True

		return False
