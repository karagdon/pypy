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

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        #for children classes inheriting parent class things, you need to use the super(Class,arg).method(arg)
        return super(ElectricCar, self).__init__(model, color, mpg)

my_car = ElectricCar("BMW", "Black", 2008 , "molten salt")