# NONE

"""
* Special constant
* Null value
* NOT the same as false
* NOT 0
* NOT an empty string
* comparing NONE to anything else will always return FALSE

	
"""

type(None)
None == False # False
None == 0 # 0


# in a boolean context None is false and not None is true.
def is_it_true(anything)
	if anything:
		print("yes, it's true")
	else:
		print("no, it's false")

is_it_true(None) #no, it's false
is_it_true(not None) #yes, it's true