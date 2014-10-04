## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ?? This creates a class DOG, that takes in an argument ANIMAL. This class creates a method that takes in a name
class Dog(Animal):

	def __init__(self, name):
		## giving the name method to Dog
		self.name = name

## Like the above, but in this case Cats.
class Cat(Animal):
	def __init__(self,name):
		## cats have a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

##?? This creates a class PERSON that takes in a arbitrary OBJECT as an argument, methosds include name and a pet
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

##?? Like the above, but Employees are PERSONS that have salaries. this is a SUPER class.
class Employee(Person):
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ?? nothing happens, this is a null operation. a 'placeholder'
class Fish(object):
	pass

## ?? nothing happens, this is a null operation. a 'placeholder'
class Salmon(Fish):
	pass

## ?? nothing happens, this is a null operation. a 'placeholder'Í
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")


## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## ?? Frank is an employee, whose name is frank and makes 120,000 a year
frank = Employee("Frank", 120000)

## ?? Frank's pet is rover!S
frank.pet = rover

## ?? flipper is a fish instance
flipper = Fish()

## ?? crouse is a Salmon instance
crouse = Salmon()

## ?? harry is an instance of Halibut
harry = Halibut

##?? Like the above, but Employees are PERSONS that have salaries. this is a SUPER class.
class Employee(Person):
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ?? nothing happens, this is a null operation. a 'placeholder'
class Fish(object):
	pass

## ?? nothing happens, this is a null operation. a 'placeholder'
class Salmon(Fish):
	pass

## ?? nothing happens, this is a null operation. a 'placeholder'Í
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")


## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## ?? Frank is an employee, whose name is frank and makes 120,000 a year
frank = Employee("Frank", 120000)

## ?? Frank's pet is rover!S
frank.pet = rover

## ?? flipper is a fish instance
flipper = Fish()

## ?? crouse is a Salmon instance
crouse = Salmon()

## ?? harry is an instance of Halibut
harry = Halibut