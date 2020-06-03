import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
from random import randrange

# global variables for user
img_size = 400
num_lines = 100
radius = 100 # in pixels
dh = 5
iterations = 5
translation_speed = 2
color = [0, 0, 0]

# create white image
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# for guidance
h = len(img)
w = len(img[0])

# initializing basics
angle_step = 360.0 / num_lines
last_r = radius
last_point = (0, 0)

for i in range(num_lines * iterations):
	# center angle and get random between 0 and 1
	curr_angle = i * angle_step - (angle_step / 2.0)
	rand = randrange(2)

	# if rand = 0 it adds a small height, else subract it from radius
	last_r += dh if rand == 0 else -dh

	for r in range(last_r):
		# convert to radians and calculate
		rads = curr_angle * (3.1416 / 180.0)
		x = r * math.cos(rads) + translation_speed * rads
		y = r * math.sin(rads)

		# center coordinates
		x += w / 2.0
		y = h / 2.0 - y

		# validate if point is inside image
		if x > w or y > h or x < 0 or y < 0:
			continue

		# get coordinates and color
		x = int(x)
		y = int(y)
		img[y, x] = color

		# draw a line from current line tip to last line tip
		if i > 0 and i < (num_lines * iterations) and r == (last_r -1):
			img = cv2.line(img, (x, y), last_point, (0, 0, 0), 1)

		# save the last line tip
		if r == (last_r - 1):
			last_point = (x, y)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
