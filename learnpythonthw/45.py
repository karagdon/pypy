
# Game idea
print "Welcome to the PETSHOP OF HORRORS, what kind of pet would you be interested in?\n * [A]mphibians \n * [B]ird\n * [C]at\n * [D]og\n * [E]lephant"

petType =  {
  'A' : "Amphibian",
  'B' : "Bird",
  'C' : "Cat",
  'D' : "Dog",
  'E' : "Elephant"
}
choosePetType = raw_input("> ")
choosePetType = choosePetType.upper()
choosePetType = choosePetType.strip()

if choosePetType in petType:
  print "%ss, great choice... *cackle*" % (petType[choosePetType])
else:
  print "You're dumb. We don't have that."

# All Pets: Name, Age, Color

# TODO: multi-dimensional array for each petType

AmpType = Amphibians[i]
#classes for each pet
class Amphibian(AmpType)
    def frog(self)
        attributes = "just slimy"
        
    def snake(self)
        attributes = "kind of scary"
        
    def lizard(self)
        attributes = "really sneaky"
        pass


# TODO: randomGenerator
### random color
### random temperment

#buy a pet
class boughtpet(petType)
    pet.name = petsName
    pet.mood = randTemperment
    pet.color = randPetColor
    
    