#Entity class where everything "alive" should be
class Entity(All):
	def __init__(self, numberId, name, healthPoints, family):
		super().__init__(numberId, name)
		self.healthPoints = int(healthPoints)
		self.family = str(family)

	#getters
	def get_healthPoints(self):
		return self.healthPoints

	def get_family(self):
		return self.family

	#setters
	def set_healthPoints(self, healthPoints):
		self.healthPoints = healthPoints

	def set_family(self, family):
		self.family = family

	#classFucntions
	def isDead(self):
		if healthPoints < 1:
			return True

		return False
