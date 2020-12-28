import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# parameters for user
color = [0, 0, 0]
thick = 5

num_iter = 4
curr_iter = 0

# white image aspect 1:1
img_size = 2000
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# constants
h = len(img)
w = len(img[0])

koch_angle = -60
koch_edges = []
sides = 3
radius = 1000
step_angle = 360.0 / sides
fig_pts = []

def rotate_pt3D(pt, angle_deg):
    rads = angle_deg * (3.1416 / 180.0)
    rotMatrixZ = [[math.cos(rads), -1*math.sin(rads), 0], [math.sin(rads), math.cos(rads), 0], [0, 0, 1]]
    r_pt = [0, 0, 0]
    for r in range(3):
        r_pt[r] = 0;
        for c in range(3):
            r_pt[r] += rotMatrixZ[r][c] * pt[c]
    return [r_pt[0], r_pt[1]]

def koch_curve(pt1, pt2, curr_iter):
    curr_iter += 1
    if curr_iter <= num_iter:
        pointing_vec = [pt2[0] - pt1[0], pt2[1] - pt1[1]]
        distance = math.sqrt((pointing_vec[0])**2 + (pointing_vec[1])**2)

        dir = [pointing_vec[0] / distance, pointing_vec[1] / distance]
        a = distance / 3.0
        third1 = [a * dir[0] + pt1[0], a * dir[1] + pt1[1]]
        third2 = [2 * a * dir[0] + pt1[0], 2 * a * dir[1] + pt1[1]]

        pt = [dir[0] * a, dir[1] * a, 0]
        top_point = rotate_pt3D(pt, koch_angle)
        top_point = [third1[0] + top_point[0], third1[1] + top_point[1]]

        koch_curve(pt1, third1, curr_iter)
        koch_curve(third1, top_point, curr_iter)
        koch_curve(top_point, third2, curr_iter)
        koch_curve(third2, pt2, curr_iter)

        if curr_iter == num_iter:
            koch_edges.append([pt1, third1])
            koch_edges.append([third1, top_point])
            koch_edges.append([top_point, third2])
            koch_edges.append([third2, pt2])
    else:
        return

#curr_iter = 0
#koch_curve([int(-w/2.0), int(h/2.0)], [0, int(-h/2.0)], curr_iter)

for i in range(sides):
    angle = (i * step_angle) + (step_angle / 2.0) + 90.0
    x = radius * math.cos(angle * (3.1416 / 180.0))
    y = radius * math.sin(angle * (3.1416 / 180.0))
    fig_pts.append([int(x), int(y)])

for i in range(sides):
    curr_iter = 0
    koch_curve(fig_pts[i], fig_pts[(i + 1) % sides], curr_iter)

for i in range(len(koch_edges)):
    ln.line(koch_edges[i][0], koch_edges[i][1], thick, color, img)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Iterations = {}, Thick = {}'.format(num_iter, thick)), plt.xticks([]), plt.yticks([])
plt.show()
