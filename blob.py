import cv2
import numpy as np

#______________________BLOBS DETECTION______________________
image = cv2.imread('sf.jpg', cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh1)
cv2.imshow('real', image)
detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(image)

blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("blobs", blobs)