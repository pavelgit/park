import numpy as np
import cv2 as cv
import math

class Model:

    def __init__():
        self.model_size = 100
        self.x = None
        self.y = None
        self.x0 = self.model_size / 2
        self.y0 = self.model_size / 2
        self.t = 0
        self.speed = 1
        self.move()

    def move():
        self.t += 1
        self.x = math.cos(self.t) * self.speed
        self.y = math.sin(self.t) * self.speed

    def get_image():
        pass



def extract_foreground(img, mask):
    return img * (mask[:, :, np.newaxis] == 255)

def play_with_background(capture, background_subtractor, resize_ratio=1, step=1):
    resized_size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH) * resize_ratio), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT) * resize_ratio))
    f = 0
    while (True):
        capture.set(1, f*step)
        ret, frame = capture.read()  
        if ret is None:
            break


        resized_frame = cv.resize(frame, resized_size)

        # resized_frame = cv.GaussianBlur(resized_frame, (5,5), 0)
        
        mask = background_subtractor.apply(resized_frame)
        
        yield (
            resized_frame, 
            mask, 
            background_subtractor.getBackgroundImage(),
            f
        )

        f += 1


def show_image(window_name, original_capture, image):
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.resizeWindow(window_name, int(original_capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(original_capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
    cv.imshow(window_name, image)

capture = cv.VideoCapture('data\\orangeville2.mp4')
background_subtractor = cv.createBackgroundSubtractorMOG2(history=int(capture.get(cv.CAP_PROP_FPS) * 60 * 10))
background_subtractor.setBackgroundRatio(10)

for (image, mask, background_image, f) in play_with_background(capture, background_subtractor, resize_ratio=0.25, step=1):

    if f % 10 == 0:
        # mask = (cv.GaussianBlur((mask==255).astype(float),(5,5),0) >= 0.1).astype(int)
        show_image('image', capture, image)    
        show_image('mask', capture, mask)
        if not (background_image is None):
            show_image('background_image', capture, background_image)
        show_image('foreground_image', capture, extract_foreground(image, mask))
        cv.waitKey(25)
        print(f)

capture.release()
cv.destroyAllWindows()