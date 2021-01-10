import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)   #frame.shape[1] is width
    height = int(frame.shape[0] * scale)  #frame.shape[0] is height
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
# For Live Video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
# Reading/Opening a video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)