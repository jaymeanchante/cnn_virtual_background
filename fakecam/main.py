import cv2
import requests
import numpy as np
import pyfakewebcam

def get_mask(frame, bodypix_url='http://api:9000'):
    _, data = cv2.imencode(".jpg", frame)
    r = requests.post(
        url=bodypix_url,
        data=data.tobytes(),
        headers={"Content-Type": "application/octet-stream"})
    # convert raw bytes to a numpy array
    # raw data is uint8[width * height] with value 0 or 1
    mask = np.frombuffer(r.content, dtype=np.uint8)
    mask = mask.reshape((frame.shape[0], frame.shape[1]))
    return mask

def replace_mask(frame, mask):
    # combine the background and foreground, using the mask and its inverse
    inv_mask = 1-mask
    for c in range(frame.shape[2]):
        frame[:,:,c] = frame[:,:,c]*mask + replacement_bg[:,:,c]*inv_mask
    return frame

# capture
cap = cv2.VideoCapture("/dev/video1")

# configure camera for 720p @ 60 FPS
# height, width = 720, 1280
width, height = 640, 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH ,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS, 60)

# read in a "virtual background" (should be in 16:9 ratio)
replacement_bg_raw = cv2.imread("background.jpg")
replacement_bg = cv2.resize(replacement_bg_raw, (width, height))

fake = pyfakewebcam.FakeWebcam("/dev/video20", width, height)

while True:
    success, frame = cap.read()
    mask = get_mask(frame)
    frame = replace_mask(frame, mask)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fake.schedule_frame(frame)