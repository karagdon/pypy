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
    
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry