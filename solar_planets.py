import cv2
from cv2 import imwrite
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mercury",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (280,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (390,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (590,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Saturn",
            (790,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Uranus",
            (960,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Neptune",
            (1140,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)