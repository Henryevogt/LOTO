import cv2
import numpy
#from vision import Vision
#import matplotlib


tag_cascade = cv2.CascadeClassifier('tags_cascade/cascade.xml')


#cap = cv2.VideoCapture(0)



for i in range(5):
    img = cv2.imread('tags_test/tag' + str(i) + '.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    rect = tag_cascade.detectMultiScale(img)
    rect2 = tag_cascade.detectMultiScale(gray)

    for (x,y,w,h) in rect:
        # loop taken from https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in rect2:
        # loop taken from https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('tag', img)
    cv2.waitKey(0) # Wait til a button is pressed
    cv2.destroyAllWindows() # discard window and move on
