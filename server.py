from flask_opencv_streamer.streamer import Streamer
import cv2
import numpy as np

MASK = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

port = 3030
require_login = False
streamer = Streamer(port, require_login)

video_capture = cv2.VideoCapture('http://149.43.156.105/mjpg/video.mjpg')

while True:
    _, frame = video_capture.read()

    frame = cv2.medianBlur(frame, 3)
    frame = cv2.filter2D(frame, -1, MASK)
    _, frame = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY_INV)
    streamer.update_frame(frame)

    if not streamer.is_streaming:
        streamer.start_streaming()
    # было в примере, но вроде и без этого работает
    # cv2.waitKey(30)