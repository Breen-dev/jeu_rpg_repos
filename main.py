from EntityClass import *
from ObjectClass import *

#main program
def main():
	hpPotion = Consumable(1, "Health potion", 2, "--nobody--", 1, {"health" : 10})
	roger = Human(0, "ROGER", 100, 10)
	roger.showEverything()

	roger.pickUpObject(hpPotion)

	roger.showEverything()

if __name__ == "__main__":
	main()

"""
last error:
Traceback (most recent call last):
  File "E:\Perso\python\JeuPython\main.py", line 15, in <module>
    main()
  File "E:\Perso\python\JeuPython\main.py", line 12, in main
    roger.showEverything()
  File "E:\Perso\python\JeuPython\EntityClass.py", line 80, in showEverything
    self.showMyItems()
  File "E:\Perso\python\JeuPython\EntityClass.py", line 69, in showMyItems
    for i in self.items:
TypeError: 'NoneType' object is not iterable
"""