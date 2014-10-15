
# Game idea
print "Welcome to the PETSHOP OF HORRORS, what kind of pet would you be interested in?\n * [A]mphibians \n * [B]ird\n * [C]at\n * [D]og\n * [E]lephant"
#class Type():
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
  print "%ss, great choice... one second... *cackle*" % (petType[choosePetType])
else:
  print "We don't have that. Try again tomorrow."

#class Pet(object):
#    def __init__(self):
#        self.bought = false
#
#    def Color(self):
        #colors available
        # TODO: Shuffle
            # Choose random 1-5
            # Player can choose one from up to 5.
        
colorHash = {
            'r' : 'R]ed',
            'o' : 'O]range',
            'y' : 'Y]ellow',
            'g' : 'G]reen',
            'b' : 'B]lue',
            'i' : 'I]ndigo',
            'v' : 'V]iolet',
            'w' : 'W]hite',
            'gr' : 'Gr]ay',
            'bl' : 'Bl]ack',
            'br' : 'Br]own'
        }
import random
haveColors = random.sample(colorHash, 5)
print "We have %ss in these colors today:\n" % petType[choosePetType]

for i in haveColors:
    print " * ["+colorHash[i]
    colorHash[i] = colorHash[i].replace("]", "")

chooseColor = raw_input("> ")
chooseColor = chooseColor.lower()
chooseColor = chooseColor.strip()

if chooseColor in haveColors:
  print "%s, great choice...  Would you like to purchase?" % (colorHash[chooseColor])
  # Y/N
  
else:
  print "We don't have that, maybe tomorrow."

#class Interact():
      #create a sequence from a set of actions, this particular sequence will trigger the scare
          #3 actions, each with either a 'scareTrigger' value of 1 or 0, once this value accumulates to 3, the the scare is trigger.
#class Scare():
#    def __init__(self,...)
        
#        pass
      
"""
Goal:
pet.type = petType
pet.name = name
pet.color = color
pet.scare = scare
"""