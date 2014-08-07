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

#I'm really good at
# Flipping Bits

#Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

a = 0b11101110
b = 0b11111111 # tip: "1" = marks as wrong
print bin(a^b)



# SLIP AND SLIDE

#   a = 0b101
#   #Tenth bit mask
#   mask = (0b1 << 9)  # One less than ten
#   desired = a ^ mask

# 1.Define a function called flip_bit that takes the inputs (number, n).

#2. Flip the nth bit (with the ones bit being the first bit) and store it in result.

#3.Return the result of calling bin(result).


def flip_bit(number,n):
    mask = 0b1 << n-1
    result = number ^ mask
    return bin(result)
