#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
from colorDetector import ColorDetector
from kalmanfilter import KalmanFilter

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# Load detector
od = ColorDetector()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()
out = cv2.VideoWriter('video/out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while True:
    ret, frame = cap.read()
    if ret is False:
        break

    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    predicted = kf.predict(cx, cy)
    cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)
    out.write(frame)
    cv2.imshow("Frame", frame)
    
    
    key = cv2.waitKey(150)
    if key == 27:
        break
    # out.release()
    # cap.release()
    # cv2.destroyAllWindows()