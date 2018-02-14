from flask import Flask, send_file
from imutils.video import VideoStream

import cv2

cam = VideoStream().start()

app = Flask(__name__)

@app.route('/')
def index():
    im = cam.read()
    _, jpg = cv2.imencode('.jpg', im)
    return jpg

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
