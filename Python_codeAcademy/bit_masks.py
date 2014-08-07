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

#Turn It On
# * with a mask

#You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on.

a = 0b10111011
#Turn the 3rd bit on!
b = 0b00000100

print bin(a|b)