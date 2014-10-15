
# Game idea
print "Welcome to the PETSHOP OF HORRORS, what kind of pet would you be interested in?\n * [A]mphibians \n * [B]ird\n * [C]at\n * [D]og\n * [E]lephant"
#class Type():
type =  {
  'A' : "Amphibian",
  'B' : "Bird",
  'C' : "Cat",
  'D' : "Dog",
  'E' : "Elephant"
}
choosePetType = raw_input("> ")
choosePetType = choosePetType.upper()
choosePetType = choosePetType.strip()


if choosePetType in type:
  print "%ss, great choice... one second... *cackle*" % (type[choosePetType])
else:
  print "You're dumb. We don't have that."

print type[choosePetType]

class Pet(object):
    def __init__(self):
        pass

#Available selection for each of the attributes
colorArr = ['pink','yellow','white']
nameArr = ['fluffy', 'cuddles', 'cupcake']
scareArr = ['bloody horns', 'glowy-green skin', 'creepy sounds']

#I want a random selection
import random
color = random.choice(colorArr)
name = random.choice(nameArr)
scare = random.choice(scareArr)
       

"""
Goal:
pet.type = petType
pet.name = name
pet.color = color
pet.scare = scare
"""