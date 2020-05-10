import cv2 as cv2
from PIL import Image, ImageTk
import numpy as np




class VideoStream:
    def _init__(self,video_source=0 ):
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            cv2.waitKey(10)
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                (ret,None)
        else:
            return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
