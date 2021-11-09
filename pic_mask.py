# HSV --> Hue(renk) Saturation(doygunluk) Value(parlaklık)

import cv2
import numpy as np

img = cv2.imread("1.jpg")

img = img[80:420,250:420]

def bos(x):
    pass

cv2.namedWindow("WEBCAM")
cv2.resizeWindow("WEBCAM",500,500)

cv2.createTrackbar("LOWER - H","WEBCAM",0,180,bos)
cv2.createTrackbar("LOWER - S","WEBCAM",0,255,bos)
cv2.createTrackbar("LOWER - V","WEBCAM",0,255,bos)

cv2.createTrackbar("UPPER - H","WEBCAM",0,180,bos)
cv2.createTrackbar("UPPER - S","WEBCAM",0,255,bos)
cv2.createTrackbar("UPPER - V","WEBCAM",0,255,bos)

cv2.setTrackbarPos("UPPER - H","WEBCAM",180)
cv2.setTrackbarPos("UPPER - S","WEBCAM",255)
cv2.setTrackbarPos("UPPER - V","WEBCAM",255)

while True:

    frame_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("LOWER - H","WEBCAM")
    ls = cv2.getTrackbarPos("LOWER - S", "WEBCAM")
    lv = cv2.getTrackbarPos("LOWER - V", "WEBCAM")

    uh = cv2.getTrackbarPos("UPPER - H", "WEBCAM")
    us = cv2.getTrackbarPos("UPPER - S", "WEBCAM")
    uv = cv2.getTrackbarPos("UPPER - V", "WEBCAM")

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])


    mask = cv2.inRange(frame_hsv,lower_color,upper_color)


    cv2.imshow("Orjinal",img)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




cap.release()
cv2.destroyAllWindows()