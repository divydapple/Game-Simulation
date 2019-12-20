# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey

class Pulsator(Black_Hole): 
    constant_counter = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._counter = Pulsator.constant_counter
    
    def update(self, model):
        ans = set()
        obj = model.find(lambda x:isinstance(x,Prey))
        for i in obj:
            if self.contains(i.get_location()):
                ans.add(i)
                model.remove(i)
                self.change_dimension(1,1)
                self._counter = Pulsator.constant_counter
        if len(ans) == 0:
            self._counter -= 1
        if self._counter == 0:
            self.change_dimension(-1,-1)
            self._counter = Pulsator.constant_counter
            if(self.get_dimension() == (0,0)):
                model.remove(self)
        return ans
