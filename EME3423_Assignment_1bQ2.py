import cv2

img = cv2.imread('Resources/BTS.jpg')

img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(img, 100, 100)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Lena',img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('HSV Image', imgHSV)
cv2.imshow('Canny Image', imgCanny)

cv2.waitKey(0)