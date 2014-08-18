class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        return
    
    def check_angles(self):
        Anglesum = self.angle1+self.angle2+self.angle3
        if Anglesum == 180:
            return True
        else:
            return False
my_triangle = Triangle(90,30,60)
print my_triangle.check_angles()
print my_triangle.number_of_sides

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1, self.angle2, self.angle3 = self.angle, self.angle, self.angle
        return

# INTRO TO CLASSES

# # # # # # # # # # # # # # # # # # # # # # #

#class Triangle(object):
#    def __init__(self, angle1, angle2, angle3):
#        
#        return

#class Triangle(object):
#    number_of_sides = 3
#    def __init__(self, angle1, angle2, angle3):
#        self.angle1 = angle1
#        self.angle2 = angle2
#        self.angle3 = angle3
#        return
#    
#    def check_angles(self):
#    Anglesum = self.angle1+self.angle2+self.angle3
#       if Anglesum == 180:
#           return True
#       else:
#            return False

#class Triangle(object):
#    number_of_sides = 3
#    def __init__(self, angle1, angle2, angle3):
#        self.angle1 = angle1
#        self.angle2 = angle2
#        self.angle3 = angle3
#        return
#    
#    def check_angles(self):
#        Anglesum = self.angle1+self.angle2+self.angle3
#        if Anglesum == 180:
#            return True
#        else:
#            return False
#my_triangle = Triangle(90,30,60)
#print my_triangle.check_angles()
#print my_triangle.number_of_sides
