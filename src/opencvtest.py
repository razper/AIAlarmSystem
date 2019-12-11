import cv2
import os

from src.Parser import Parser
from src.TelegramAPI import BotHandler
import threading


class ImageRecognition:
    def __init__(self):
        self.bot = None

    def main(self, args):
        cap = cv2.VideoCapture(args.camera_type)
        casc_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(casc_path)
        image_counter = 0  # glob.glob("photos/*")
        self.bot = BotHandler(args.token, args.proxy)
        rects_value_by_frame = 0
        faces_iter = 0
        while True:
            rects = []
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                rect = (x, y, w, h)
                rects.append(rect)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)
            if len(rects) > rects_value_by_frame:
                print("New face detected" + str(faces_iter))
                faces_iter += 1
                t = threading.Thread(target=self.take_an_image, args=[image_counter, frame])
                t.start()
                image_counter += 1
            rects_value_by_frame = len(rects)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                self.take_an_image(image_counter, frame)
                image_counter += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def take_an_image(self, image_counter, frame, send_image=True):
        img_name = os.path.realpath("photos/opencv_frame_{}.png".format(image_counter))
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        try:
            self.bot.send_message("Person detected")
            if send_image:
                self.bot.send_photo(img_name)
        except Exception as e:
            raise Exception(str(e))


if __name__ == '__main__':
    parser = Parser()
    runner = ImageRecognition()
    runner.main(parser.args)
