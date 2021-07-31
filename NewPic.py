import cv2
import numpy as np

img3 = np.random.random((600, 800, 3))

while 1:
    img3 = np.random.random((600, 800, 3))
    img3 *= 50
    img3 = img3.round()
    cv2.imshow('img', img3)
    print(cv2.waitKey(1000))
    if 0:
        break

cv2.destroyAllWindows()
