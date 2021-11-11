from EntityClass import *
from ObjectClass import *

#main program
def main():
	testobjet = Consumable(1, "Health potion", 2, 1, {"health" : 10})
	test = Human(0, "ROGER", 100, 10, [testobjet])
	test.showEverything()

	test.useObject(testobjet)

	test.showEverything()

if __name__ == "__main__":
	main()