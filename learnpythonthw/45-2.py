#practice with classes

class Cat(object):
	def __init__(self,name,sound):
		## cats have a name
		self.name = name
		self.sound = sound
		
	def description(self):
		print self.name
	
	def animalSound(self):
		print self.sound
	
my_cat = Cat("whiskers", "meow!")
my_cat.description()
my_cat.animalSound()