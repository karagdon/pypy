print 'this is a list'

things = ['a', 'b', 'c', 'd']
print things [1]
things[1] = 'z'
print things[1]
print things


print 'this is a dict'
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print stuff['name']
print stuff['height']
print stuff['age']
stuff['city'] = 'San Francisco'
print stuff['city']

print 'adding stuff'
stuff[1] = "Wow"
stuff[2] = 'Neato'
print stuff[1]
print stuff[2]
stuff

print 'deleting stuff'
del stuff['city']
del stuff[1]
del stuff[2]
stuff

#tbd: a dictionary example