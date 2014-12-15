'''
# BASIC MATH OPS

import fractions
x = fractions.Fraction(1,3)
x
x * 2
fractions.Fraction(6,4)
fractions.Fraction(0,0)

# TRIG

import math
math.pi
math.sin(math.pi / 2)
math.tan(math.pi / 4)

'''
# Numbers in a boolean contezxt

def is_it_true(anything):
	if anything:
		print("yes, it's true")
	else:
		print("no, its false")
is_it_true(1)
is_it_true(-1)
is_it_true(0)
is_it_true(0.1)
is_it_true(0.0)
import fractions
is_it_true(fractions.Fraction(1, 2))
is_it_true(fractions.Fraction(0, 1))
# In boolean context, non-zero integers are true; 0 is false,
# Non-zero floating point numbers are true (eg: 0.0)
# Fractions can also be used in a boolean context. eg, Fraction (0, n) is false for all values of n, all other fractions are true.

