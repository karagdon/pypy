#bitwise represention

#Base 2:
print bin(1)

#base8
print hex(7)

#base 16
print oct(11)


#BITWISE OPERATORS#


# AND FUNCTION, A&B

# 0b1110
# 0b0101
# 0b0100

print "AND FUNCTION, A&B"
print "======================\n"

print "bin(0b1110 & 0b101)"
print "= ",bin(0b1110&0b101)

# THIS OR THAT, A|B

#The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1.

# 0b1110
# 0b0101
# ======
# 0b1111

print "OR FUNCTION, A|B"
print "======================\n"
print "bin(0b1110|0b0101)"
print "= ",bin(0b1110|0b0101)


# XOR FUNCTION, A^B

#XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

# 1 1 1 0
# 0 1 0 1
# = = = =
# 1 0 1 1 thus 0b1011 should appear

print "XOR FUNCTION"
print "======================\n"
print "bin(0b1110 ^ 0b101)"
print "=", bin(0b1110 ^ 0b101)


# XOR FUNCTION, ~A

#The bitwise NOT operator (~) just flips all of the bits in a single number.This is equivalent to adding one to the number and then making it negative.

print "NOT FUNCTION, ~A"
print "======================\n"
print "~1 =", ~1
print "~2 =", ~2
print "~3 =", ~3
print "~42 =", ~42
print "~123 =", ~123

# BIT MASK #

# A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

# num  = 0b1100
# mask = 0b0100
# desired = num & mask
# if desired > 0:
#    print "Bit was on"

def check_bit4(input):
    mask = 0b1000
    num = input
    result ="on"
    desired = num & mask
    if desired < 1:
        result = "off"
    return result
