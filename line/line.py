import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
from random import randrange

img_size = 400
# create white image
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# for guidance
h = len(img)
w = len(img[0])

def distance(p1, p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def grid(gap, img):
	for i in range(h):
		for j in range(w):
			if i == int(h / 2.0) or j == int(w / 2.0) :
				img[i, j] = [0, 0, 0]
			if (i % gap == 0 or j % gap == 0) and (i % 2 == 0 and j % 2 == 0):
				img[i, j] = [0, 0, 0]

def line(p1, p2, color, img):
	rads = math.atan((p2[1] - p1[1] * 1.0) / (p2[0] - p1[0] * 1.0))
	if rads < 0:
		rads += 3.1416
	# prints the degrees between the two points
	print(rads*180/3.1416)

	dist = int(distance(p1, p2))
	for r in range(dist):
		x = p1[0] + r * math.cos(rads)
		y = p1[1] + r * math.sin(rads)

		# center coordinates
		x += w / 2.0
		y = h / 2.0 - y

		# validate if point is inside image
		if x > w or y > h or x < 0 or y < 0:
			continue

		x = int(x)
		y = int(y)
		img[y, x] = color


p1 = tuple([20, 20])
p2 = tuple([0, -40])
grid(20, img)
line(p1, p2, [0, 0, 255], img)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
