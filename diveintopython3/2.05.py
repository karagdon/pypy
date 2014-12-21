## 2.5 - Tuples
## * immutable list, can not be changed in any way once it is created


a_tuple = ("a", "b", "mpilgrim","z", "example")
print (a_tuple)
a_tuple[0]
a_tuple[-1]
a_tuple[1:3]

#  append(), extend(), insert(), remove(), and pop() dont exists as methonds for tuples
"""
Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.

It makes your code safer if you “write-protect” data that doesn’t need to be changed. Using a tuple instead of a list is like having an implied assert statement that shows this data is constant, and that special thought (and a specific function) is required to override that.

Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.
"""