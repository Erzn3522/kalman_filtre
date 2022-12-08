
import cv2
class DirectionAssign:
   def __init__(self,actualx, actualy, predx, predy):
       self.actualx = actualx
       self.actualy = actualy
       self.predx = predx
       self.predy = predy
    

   def assign(self):
       
       difX = self.actualx - self.predx
       dify = self.actualy - self.predy
       
       self.directX = 1 if difX > 0 else -1
       self.dirextY = 1   if dify > 0 else -1
       
       return [difX, dify]