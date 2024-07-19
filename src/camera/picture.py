from datetime import datetime
import cv2

def take_picture(quality = 80):
    """Take a pic with given quality and return binary representation"""
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    jpeg_quality = [cv2.IMWRITE_JPEG_QUALITY, quality]
    img_name = "opencv_frame_{}.jpg".format(datetime.now().timestamp())
    # write snap as gpg on root of the project. Uncomment to test
    #cv2.imwrite(img_name, frame, jpeg_quality)
    print("{} written!".format(img_name))
    cam.release()
    image_encode = cv2.imencode('.jpg', frame, jpeg_quality)[1]
    return image_encode
