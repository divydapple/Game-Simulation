from prey import Prey
from ball import Ball
import math,random



class Special(Ball): 
    distConstant = 50
    
    def __init__(self,x,y):
        Ball.__init__(self,x,y)
        self._color = 'green'

    def display(self, canvas):
        canvas.create_oval(self._x-Ball.radius, self._y-Ball.radius, self._x+Ball.radius, self._y+Ball.radius, fill=self._color)
    
    def update(self, model):
        self.move()
        for o in list(model.find(lambda x:not isinstance(x,Prey))):
            if self.distance(o.get_location()) <= Special.distConstant:
                tmp1 = o.get_location()
                tmp2 = self.get_location()
                self.set_angle(math.pi + math.atan2(tmp1[1]-tmp2[1],tmp1[0]-tmp2[0]))


        
