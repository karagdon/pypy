# TODO: test classes and call them

# Game idea
print "Welcome to the PETSHOP OF HORRORS, what kind of pet would you be interested in?\n * [A]mphibians \n * [B]ird\n * [C]at\n * [D]og\n * [E]lephant"

class Pet(object):
    def __init__(self):
		description = "cute"
		self.current = 0
		
		return Pet.self
	
	def Types(self):
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
		raise SystemExit
	types = choosePetType
	return pet.types
"""
def Color(self):
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
	print "Shop owner: We have %ss in these colors today:" % petType[choosePetType]
	
	for i in haveColors:
	    print " * ["+colorHash[i]
	    colorHash[i] = colorHash[i].replace("]", "")
	
	chooseColor = raw_input("> ")
	chooseColor = chooseColor.lower()
	chooseColor = chooseColor.strip()
	
	if chooseColor in haveColors:
		print "Shop owner: You want that %s %s? There are *NO* returns. \n * [Y]es\n * [N]o" % (colorHash[chooseColor], (petType[choosePetType]))
	 	purchased = raw_input("> ")
		purchased = purchased.lower()
		purchased = purchased.strip()
	else:
		print "Shop owner: We don't have that, maybe tomorrow."
		raise SystemExit


def name(self):
	if purchased == 'y':
		print "You spend all your money to buy the pet. You are now broke. The shop owner cackles as you exit the store. Meanwhile, you decide on your new pet's name..."
		name = raw_input("> ")
		print "Shop owner: Interesting choice for a name.."
	else:
		print "Shop owner: Quit wasting my time, Halloween is coming!"
		raise SystemExit
	
#def scare():
# Add scareScore for pet type
scareScore = colorHash[chooseColor] + (petType[choosePetType])
points = 0
scareScore = scareScore.lower()
scareScore = scareScore.strip()
scareScore += scareScore.upper()
for s in name:
	if s in scareScore:
		points += 1

randDeath = [
	"set fire to your hair",
	"poke a stick at a grizzly bear",
	"eat medicine that's out of date",
	"use your private parts as piranha bait",
	"teach yourself how to fly",
	"eat a two week old unrefrigerated pie",
	"invite a psycho killer inside",
	"scratch a drug dealer's brand new ride",
	"eat a tube of superglue",
	"disturb a nest of wasps for no good reason",
	"stand on the edge of a train station platform"
	]
randDeath = random.sample(randDeath, 1)

if points >= (len(name)):
	print "%s does not kill you as you approach it" % name
else:
	print "%s hates you, and terrorizes the city. You also %s and die. GG." % (name, randDeath)


#print "Your scare score is: %s" % scareScore


Goal:
pet.type = petType
pet.name = name
pet.color = color
pet.scare = scare
"""
print pet.types