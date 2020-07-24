import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# white image
img_size = 400
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

color = [0, 0, 0]
gridGap = 20
thick = 2

#ln.grid(gridGap, img) # paints grid

num_sides = 4
fig_center = [0.0, 0.0]
size = 60
num_iter = 12

# constants
PI = 3.1416
h = len(img)
w = len(img[0])
angle_dist = 2
delta_angle = (angle_dist * 180.0 / (num_sides)) / num_iter
# or custom
# delta_angle = 15.0
# or custom
# delta_size = 5.0
acc_angle = 0.0
acc_size = size
verts = []
step_angle = 360.0 / num_sides
ca1 = 0.0
# for angle visualization
'''
for r in range(300):
	for i in range(int(360.0/delta_angle)):
		angle = i * delta_angle
		x = r * math.cos(angle * PI / 180.0)
		y = r * math.sin(angle * PI / 180.0)

		x += w / 2.0
		y = h / 2.0 - y

		x = int(x)
		y = int(y)

		# validate if point is inside image
		if x >= w or y >= h or x < 0 or y < 0:
			continue

		img[y, x] = [255, 0, 0]
'''
for j in range(num_iter):
	last_point = [0.0, 0.0]
	first_point = [0.0, 0.0]

	for i in range(num_sides):

		angle = i * step_angle - (step_angle / 2.0) - acc_angle
		x = fig_center[0] + (acc_size) * math.cos(angle * PI / 180.0)
		y = fig_center[1] + (acc_size) * math.sin(angle * PI / 180.0)

		if i == 0:
			first_point = [x, y]
		if i > 0:
			ln.line([x, y], last_point, thick, color, img)
		if i == num_sides - 1:
			ln.line([x, y], first_point, thick, color, img)

		last_point = [x, y]
		verts.append([x, y])
		x += w / 2.0
		y = h / 2.0 - y

		x = int(x)
		y = int(y)

		# validate if point is inside image
		if x >= w or y >= h or x < 0 or y < 0:
			continue

	adj1 = (acc_size * math.sin(delta_angle * PI / 180.0)) / (math.tan((step_angle / 2.0) * PI / 180.0))
	#print("ca1 1:", adj1)
	adj2 = acc_size * math.cos(delta_angle * PI / 180.0)
	delta_L = abs(acc_size - adj2)
	#print(delta_L)
	acc_angle += delta_angle
	delta_size = abs(adj1 - delta_L)
	acc_size += delta_size

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
