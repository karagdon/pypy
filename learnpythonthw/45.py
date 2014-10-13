# TODO: Make a class for amphibians

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
# Amphibians: Snakes, Lizards, Frogs
# Snakes: Poisonous?
# Lizards: Spikey?
# Frogs: Mutant?


#classes for each pet
class Amphibian(AmpType)
    def frog(self)
        
        pass
    def snake(self)
        
        pass
    def lizard(self)
        
        pass

#buy a pet
#take it home
#pet does something
