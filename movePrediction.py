#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
import numpy as np
from colorDetector import ColorDetector
from kalmanfilter import KalmanFilter
from directionAssign import DirectionAssign
from drawArrow import DrawArrow

cap = cv2.VideoCapture(0)
background = cv2.imread("img/background.png")

frame_height, frame_width = background.shape[:2]
# Load detector
od = ColorDetector()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()


# out = cv2.VideoWriter('video/out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while True:
    ret, frame = cap.read()
    if ret is False:
        break

    obj_bbox = od.detect(frame)
    x, y, x2, y2 = obj_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)
    
    
    #region PREDICT
    predicted = kf.predict(cx, cy)
    predicted1 = kf.predict(predicted[0], predicted[1])    
    #endregion
    
    #region DIRECTION
    direction = DirectionAssign(cx,cy,predicted[0], predicted[1])
    direction.assign()    
    #endregion
    
    #region ARROW
    start_point = (int(frame_height/2), int(frame_height/2))
    end_point = (int(frame_width/2 +(direction.actualx)) , int(frame_height/2 + (direction.actualy)))
    # end_point = (0, 50)
    arrow = DrawArrow(background, start_point, end_point, (0,0,0), 3)
    arrow.drawArrow()
    #endregion
    
    #region EKRANA RIGHT-LEFT BASMA
    # if(predicted[0] != 0):
    #     print(direction.assign())

    #endregion
    
    cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)
    cv2.circle(frame, (predicted1[0], predicted1[1]), 20, (0, 255, 0), 4)
    # out.write(frame)
    cv2.imshow("Frame", frame)
    # txtOnDisplay = "predicted pos: {} - {}"
    
    # print(txtOnDisplay.format(cy, predicted[1]))
    
    
    
    
    key = cv2.waitKey(150)
    if key == 27:
        break
