import cv2
import numpy
#from vision import Vision
#import matplotlib


lock_cascade = cv2.CascadeClassifier('locks_cascade/cascade.xml')

#vision_lock = vision(None)

#cap = cv2.VideoCapture(0)


for i in range(5):
    # for each of 5 lock images I test on
    img = cv2.imread('locks_test/lock0' + str(i) + '.jpg')


    rect = lock_cascade.detectMultiScale(img)

    for (x,y,w,h) in rect:
        # loop taken from https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w]
        lock = lock_cascade.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in lock:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    cv2.imshow('lock', img)
    cv2.waitKey(0) # Wait til a button is pressed
    cv2.destroyAllWindows() # discard window and move on