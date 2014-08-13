#By convention, user-defined Python class names start with a capital letter.
class Animal(object):
    #class magic here
    pass
  
  #By convention, user-defined Python class names start with a capital letter.
class Animal(object):
    #class magic here
    # this initializes the objects
    def __init__(self, name):
        #instantiate the object self with the parameter name
        self.name = name

#dot notation
zebra = Animal("Jeffrey")
print zebra.name


# Class definition
class Animal(object):
    """Makes cute animals."""
    # *** For initializing our instance objects
    
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        # *** added to function
        self.is_hungry = is_hungry
    
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry


##### SCOPE #####

pclass Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive



##### METHODS #####

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal('Adi',5)
hippo.description()


##### MEMBER VARIABLES #####

class Animal(object):
    """Makes cute animals."""
    
    #THESE ARE MEMBER VARIABLES, THEY BE COOL
    health = "good"
    is_alive = False
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        print self.health
        print self.is_alive

hippo = Animal('Adi',5)
hippo.description()

sloth = Animal('Bdi',6)
sloth.description()

ocelot = Animal('Cdi',7)
ocelot.description()

