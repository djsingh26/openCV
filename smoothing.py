import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)


cv.waitKey(0)