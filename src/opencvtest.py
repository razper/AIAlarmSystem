import cv2
import os
from src.UriDictionary import *

if __name__ == '__main__':
    cap = cv2.VideoCapture(EXTERNAL_CAMERA)
    cascPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(cascPath)
    rects_value_by_frame=0
    faces_iter = 0
    while True:
        rects=[]

        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            rect=(x,y,w,h)
            rects.append(rect)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if (len(rects)>rects_value_by_frame):
            print("new face "+str(faces_iter))
            """
            In here we should print out/send to bot the diff from the end.
            e.g. if rects_value_by_frame = 2 
            len(rects) =5
            then we should send a pic of the last 3, index 2,3,4
            those are the new faces there were added
            """
            faces_iter+=1
        rects_value_by_frame=len(rects)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
