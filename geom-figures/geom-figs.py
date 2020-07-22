import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img_size = 400

# white image
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# painting a red line
color = [0, 0, 0]
gridGap = 20
thick = 2


#ln.grid(gridGap, img) # paints grid
#ln.line(p1, p2, thickness, color, img)
#ln.line([0, 30], [-100, 60], 7, [255, 0, 0], img)

# for guidance
h = len(img)
w = len(img[0])

num_sides = 4
fig_center = [0.0, 0.0]
step_angle = 360.0 / num_sides
size = 60
PI = 3.1416
num_iter = 12

angle_dist = 2
delta_angle = (angle_dist * 180.0 / (num_sides)) / num_iter
#delta_angle = 15.0
print(delta_angle)
delta_size = 5.0
acc_angle = 0.0
acc_size = size
dist = 0.0
verts = []
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
		if x > w or y > h or x < 0 or y < 0:
			continue
		'''
		if j > 0 and i == num_sides - 1:
			dist = math.sqrt((verts[i + (j*num_sides)][0] - verts[i + (j*num_sides) - num_sides][0])**2 + (verts[i + (j*num_sides)][1] - verts[i + (j*num_sides) - num_sides][1])**2)
			print(str(i + (j*num_sides)), str(i + (j*num_sides) - num_sides))
			ln.line(verts[i + (j*num_sides)], verts[i + (j*num_sides) - num_sides], thick, [0, 0, 255], img)
			print(dist)
		'''
		ca = (acc_size * math.sin(delta_angle * PI / 180.0)) / (math.tan((step_angle / 2.0) * PI / 180.0))
		ca = abs(acc_size - ca)
		print(ca)
	acc_angle += delta_angle
	#acc_size += delta_size
	#acc_size += dist * math.cos((step_angle/2.0) * PI / 180.0)

	acc_size += abs(acc_size - ca)


# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
