# Black_Hole is derived from only Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)
        
    def update(self, model):
        ans = set()
        obj = model.find(lambda x:isinstance(x,Prey))
        for i in obj:
            if self.contains(i.get_location()):
                ans.add(i)
                model.remove(i)
        return ans
    
    def display(self, canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2, self._x+self._width/2, self._y+self._height/2, fill = "black")
    
    def contains(self,xy):
        return self.distance(xy) <= Black_Hole.radius
