import cv2
import os
from src.UriDictionary import *

if __name__ == '__main__':
    cap = cv2.VideoCapture(EXTERNAL_CAMERA)
    cascPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(cascPath)

    while True:
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
