import cv2 #importing the opencv module
cascPath = "haarcascade_frontalface_default.xml" #there is an xml file named this, which have predefined how a human face looks like
faceCascade = cv2.CascadeClassifier(cascPath) #used cascade classifier 
import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5)

video_capture = cv2.VideoCapture(0) #videocapture for starting to capture video
Fx=240
Fy=320
while True:
    # Capture frame-by-frame
    #video_capture.read()
    video_capture.grab()
    retrival, frame = video_capture.retrieve(0)
    
    
    '''
    2 parameters returned,a ret,which is in boolean which says the capture is true or not
    and a frame ,which is actually an array of numbers containing different RGB colours
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#conversion to greyscale

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )#this function and its parameters specify the way face detection is done

    # Draw a rectangle around the faces
    dutycycle=7.5
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cX=(x+(w/2))
        
        print(Fx-cX)
        if Fx-cX>0:
            dutycycle-=1 
            p.ChangeDutyCycle(dutycycle)
            time.sleep(0.5)
            #negative rotation of servoX
           
        if Fx-cX<0:
            #postive rotation of servoX
            dutycycle+=1
            p.ChangeDutyCycle(dutycycle)
            time.sleep(0.5)
            
       
            
        '''
        Drawing a rectangle using x,y as initial coordinates and then using width and height.
        '''

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit the capture mode
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

            
       
    
