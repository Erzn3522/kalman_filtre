import cv2 

class DrawArrow:
    def __init__(self, image, start_point, end_point, color, thickness):
        self.image = image
        self.start_point =start_point
        self.end_point = end_point
        self.color = color
        self.thickness = thickness
        
    def drawArrow(self):
        window_name = "Direction Arrow"
        image = cv2.arrowedLine(self.image, self.start_point, self.end_point,
                                     self.color, self.thickness, tipLength = 0.5)
        
        cv2.imshow(window_name, image)