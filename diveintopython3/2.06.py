# A Set is an unordered 'bag' of unique values, and can contain any immutable data type
# Standard set operations (union, intersection, set difference)

a_set = {1}
a_set # {1}
type(a_set) # <class 'set'>
a_set = {1, 2}
a_set # {1, 2}


# a set out of a list
a_list = ['a','b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
a_set 	#{'a','b', 'mpilgrim', True, False, 42}
a_list	#['a','b', 'mpilgrim', True, False, 42]


k_list = ['python', 'chocolate', 'videogames']
k_set = set(k_list)


# an empty set
a_set = set()
a_set

type(a_set) # <class 'set'>

# modifying an empty set
a_set.add(4) # adds any value of any type to the set
a_set.update({2, 4, 6})
a_set.discard(4)
a_set.pop()
a_set.clear

a_set = {4,7,10,11,13}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)
a_set.difference(b_set)
a_set.symmetric_difference(b_set)

