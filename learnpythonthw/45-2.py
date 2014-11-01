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

class Dog(object):
	def __init__(self,color,drool)
		self.color = color
		self.drool = droolAmt
		
	def dogColor(self)
		print self.color

	def droolAmount(self)
		print self.drool

my_dog = Dog("blue", "a lot")
my_dog.dogColor()
my_dog.droolAmount()