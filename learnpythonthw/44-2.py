
class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"
        
    def altered(self):
        print "PARENT altered()"
        

class Child(object):
    def override(self):
        print "CHILD override()"

    def implicit(self):
        print "CHILD implicit()"
        
    def altered(self):
        print "CHILD altered()"
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()