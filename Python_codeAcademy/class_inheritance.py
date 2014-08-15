class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship.

#In Python, inheritance works like this:

#class DerivedClass(BaseClass):
#   # code goes here
#where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
#
#class Shape(object):
#    """Makes shapes!"""
#    def __init__(self, number_of_sides):
#       self.number_of_sides = number_of_sides

# Add your Triangle class below!

class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3