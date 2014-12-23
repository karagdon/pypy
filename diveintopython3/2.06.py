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
