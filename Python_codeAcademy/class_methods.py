class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        return

    def display_car(self):
        print str("This is a %s %s with %d MPG." % (self.color,self.model,self.mpg))
        return
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.display_car()