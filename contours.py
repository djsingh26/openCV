import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edges', canny)

contours, heirarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)