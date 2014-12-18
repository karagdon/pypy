a_list = ['a', 'b' 'mpilgrim', 'z', 'example','1']
a_list

a_list[0]
a_list[4]
a_list[-1]
a_list[-3]

# Slicing a list
a_list[1:3]
a_list[1:-1]
a_list[0:3]
a_list[:3]
print (a_list[3:])
print (a_list[:])
a_list[1:3]
a_list[1:-1]
a_list[0:3]
a_list[:3]
a_list[3:]
a_list[3]

# adding items to a list
a_list = a_list + [2.0, 3]
a_list.append(True)
a_list.extend(['four','Ω'])
a_list.insert(0, 'Ω')

#searching for values in a list
a_list = ['a','b', 'new', 'mpilgrim', 'new']
a_list.count('new')
'new' in a_list

'c' in a_list
 
a_list.index('mpilgrim')
a_list.index('new')
a_list.index('c')

# removing itmes frmo a list
a_list = ['a','b', 'new', 'mpilgrim', 'new']
a_list[1]

del a_list[1]
a_list

a_list[1]

a_list.remove('new')
a_list
a_list.remove('new')
a_list
a_list.remove('new')
# >>> new is no longer in this list
