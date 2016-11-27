'''
Created on 22-Nov-2016

@author: trinadhkoya
'''
class Triangle(object):
    no_of_sides=3
    
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        
        
class Equilateral(Triangle):
    angle = 60
    
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

    def print(self):
        #print(self.angle1)
        super(Equilateral,self).__init__(self.angle1, self.angle2, self.angle3)
        print(self.angle1)
    
    
    
    
my_traingele=Triangle(10,20,30)
eq=Equilateral()
eq.print()
