import cv2
import numpy
#import matplotlib

img = cv2.imread('locks/padlock001.jpg', 0)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF


if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows() 