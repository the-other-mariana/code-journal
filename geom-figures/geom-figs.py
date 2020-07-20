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

num_sides = 6
step_angle = 360.0 / num_sides
size = 60
PI = 3.1416
delta_angle = 5.0
num_iter = 10


last_point = [0.0, 0.0]
first_point = [0.0, 0.0]
for i in range(num_sides):
	angle = i * step_angle - (step_angle / 2.0)
	x = size * math.cos(angle * PI / 180.0)
	y = size * math.sin(angle * PI / 180.0)

	if i == 0:
		first_point = [x, y]
	if i > 0:
		ln.line([x, y], last_point, thick, color, img)
	if i == num_sides - 1:
		ln.line([x, y], first_point, thick, color, img)

	last_point = [x, y]

	x += w / 2.0
	y = h / 2.0 - y

	x = int(x)
	y = int(y)

	# validate if point is inside image
	if x > w or y > h or x < 0 or y < 0:
		continue

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
