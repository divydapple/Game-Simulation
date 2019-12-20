# Hunter is derived from both the Mobile_Simulton and Pulsator classes;
#   each updates like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    distConstant = 200
    
    def __init__(self, x,y):
        Pulsator.__init__(self, x, y)
        self.randomize_angle()
        self.set_speed(5)
        self._dist = Hunter.distConstant

        
    def update(self, model):
        self.move()
        rVal = set()
        minObjDist = 1000000000 
        obj2chase = None
        for o in list(model.find(lambda x:isinstance(x,Prey))):
            if(self.contains(o.get_location())):
                rVal.add(o)
                model.remove(o)
                self.change_dimension(1,1)
                self._counter = Pulsator.constant_counter
                obj2chase = None
            objDist = self.distance(o.get_location())
            if objDist <= Hunter.distConstant and objDist < minObjDist: 
                minObjDist = objDist
                obj2chase = o
        if obj2chase != None:
            tmp1 = obj2chase.get_location()
            tmp2 = self.get_location()
            self.set_angle(atan2(tmp1[1]-tmp2[1],tmp1[0]-tmp2[0]))
        if(len(rVal) == 0): 
            self._counter -= 1 
        if(self._counter == 0):
            self.change_dimension(-1,-1) 
            if(self.get_dimension() == (0,0)): 
                model.remove(self)
            self._counter = Pulsator.constant_counter
        return rVal

