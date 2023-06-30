import datetime
import cv2 as cv
trans=cv.CascadeClassifier('jk.xml')
video=cv.VideoCapture(0)
while True:
 video.set(450,400)
 success,frame=video.read()
 date=str(datetime.datetime.now())
 font=cv.FONT_HERSHEY_DUPLEX
 frame=cv.putText(frame,date,(0,50),font,1,(255,0,0),2)
 if success==True:
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=trans.detectMultiScale(gray)
 for x,y,w,h in faces:
     cv.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
     cv.imshow('Face_Detect',frame)
     cv.waitKey(1)