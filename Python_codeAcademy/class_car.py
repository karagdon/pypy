
class Car(object):
#This is a member variable, which stores information that belongs to the class object
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        return
#my_car = Car("DeLorean", "silver", 88)
#print my_car.condition
mycar = Car('DeLorean','silver',88)
print mycar.condition, mycar.model, mycar.color, mycar.mpg
