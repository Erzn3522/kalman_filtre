
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
       
       directX = "right" if difX > 0 else "left"
       dirextY = "up"   if dify > 0 else "down"
       
       return [directX, dirextY]