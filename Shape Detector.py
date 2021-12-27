#!/usr/bin/env python
# coding: utf-8


#Importing required libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image and set thresholds
img = cv2.imread('picture.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# Storing toring names of shapes
for contour in contours:

	# Ignore first count as function detects entire image 
	if i == 0:
		i = 1
		continue

	# cv2.approxPloyDP() function to approximate the shape
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
    
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

	# finding center
	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	# Inserting name at center
	if len(approx) == 3:
		cv2.putText(img, 'Triangle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

	elif len(approx) == 4:
		cv2.putText(img, 'Quadrilateral', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

	elif len(approx) == 5:
		cv2.putText(img, 'Pentagon', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

	elif len(approx) == 6:
		cv2.putText(img, 'Hexagon', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

	else:
		cv2.putText(img, 'circle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# displaying the image with labeled names
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

