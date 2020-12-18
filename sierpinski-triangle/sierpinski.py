import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# parameters for user
color = [0, 0, 0]
thick = 7
dt = 0.8
num_iter = 6
curr_iter = 0

# white image aspect 1:1
img_size = 1000
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# constants
h = len(img)
w = len(img[0])

def iterate(tri_pts, curr_thick, curr_iter):
    curr_iter += 1
    if curr_iter <= num_iter:
        for i in range(len(tri_pts)):
            ln.line(tri_pts[i], tri_pts[(i + 1) % len(tri_pts)], curr_thick, color, img)

        new0 = [int((tri_pts[0][0] + tri_pts[1][0]) / 2.0), int((tri_pts[0][1] + tri_pts[1][1]) / 2.0)]
        new1 = [int((tri_pts[1][0] + tri_pts[2][0]) / 2.0), int((tri_pts[1][1] + tri_pts[2][1]) / 2.0)]
        new2 = [int((tri_pts[2][0] + tri_pts[0][0]) / 2.0), int((tri_pts[2][1] + tri_pts[0][1]) / 2.0)]

        new_tri = [new0, new1, new2]
        for i in range(len(new_tri)):
            ln.line(new_tri[i], new_tri[(i + 1) % len(new_tri)], curr_thick, color, img)
        curr_thick *= dt

        sub_tri0 = [tri_pts[0], new_tri[0], new_tri[2]]
        iterate(sub_tri0, curr_thick, curr_iter)

        sub_tri1 = [new_tri[0], tri_pts[1], new_tri[1]]
        iterate(sub_tri1, curr_thick, curr_iter)

        sub_tri2 = [new_tri[2], new_tri[1], tri_pts[2]]
        iterate(sub_tri2, curr_thick, curr_iter)
    else:
        return

base_triangle = [[0, int(h/2.0 - thick/2.0)], [int(w/2.0 - thick/2.0), -1*int(h/2.0 - thick/2.0)], [-1*int(w/2.0 - thick/2.0), -1*int(h/2.0 - thick/2.0)]]
print(base_triangle)
iterate(base_triangle, thick, curr_iter)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Iterations = {}, Thick = {}, \u0394Thick = {}'.format(num_iter, thick, dt)), plt.xticks([]), plt.yticks([])
plt.show()
