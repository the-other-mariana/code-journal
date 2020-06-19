import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

PI = 3.1416

# calculates distance between two points (tuples)
def distance(p1, p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# loops around main pixel for given thickness
def roundPixel(i, j, thickness, color, img):
	# for guidance
	h = len(img)
	w = len(img[0])

	for r in range(int(i - thickness / 2.0), int(i + thickness / 2.0)):
		for c in range(int(j - thickness / 2.0), int(j + thickness / 2.0)):
			if c > w or r > h or c < 0 or r < 0:
				continue
			img[r, c] = color

# paints a grid on the image
def grid(gap, img):
	# for guidance
	h = len(img)
	w = len(img[0])

	for i in range(h):
		for j in range(w):
			if i == int(h / 2.0) or j == int(w / 2.0) :
				img[i, j] = [0, 0, 0]
			if (i % gap == 0 or j % gap == 0) and (i % 2 == 0 and j % 2 == 0):
				img[i, j] = [0, 0, 0]

# paints a line between two points using polar coordinates
def line(p1, p2, thickness, color, img):
	# for guidance
	h = len(img)
	w = len(img[0])
	rads = 0

	# case of division by zero
	if p2[0] == p1[0]:
		rads += PI / 2.0
		if (p2[1] - p1[1]) < 0:
			rads += PI
	else:
		rads += math.atan((p2[1] - p1[1] * 1.0) / (p2[0] - p1[0] * 1.0))
		if (p2[0] - p1[0]) < 0:
			rads += PI
	# prints the degrees between the two points
	# print(rads*180/PI)

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
		roundPixel(y, x, thickness, color, img)


# EXAMPLE
img_size = 400

# white image
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# painting a red line
p1 = tuple([20, 20])
p2 = tuple([40, -40])
thickness = 3
color = [0, 0, 255]
gridGap = 20

grid(gridGap, img) # paints grid
line(p1, p2, thickness, color, img)
line([0, 30], [-100, 60], 7, [255, 0, 0], img)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
