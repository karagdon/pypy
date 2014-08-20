class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        return

    def drive_car(self):
        #adding self. to condition accesses the membervariable inside a class method
        self.condition = "used"
        return

    def display_car(self):
        print str("This is a %s %s with %d MPG." % (self.color,self.model,self.mpg))
        return

my_car = Car("DeLorean", "silver", 88)

print my_car.model
print my_car.color
print my_car.mpg
print my_car.condition
print my_car.drive_car()
print my_car.condition