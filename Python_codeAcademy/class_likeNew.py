class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def drive_car(self):
                #adding self. to condition accesses the membervariable inside a class method
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
                #for children classes inheriting parent class things, you need to use the super(Class,arg).method(arg)
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type
    def drive_car(self):
     #adding self. to condition accesses the membervariable inside a class method
        self.condition = "like new"

my_car = ElectricCar("bus", "blue", 40, "molten salt")

print my_car.condition
my_car.drive_car()
print my_car.condition