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
sides = 5

# white image aspect 1:1
img_size = 2000
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# constants
h = len(img)
w = len(img[0])

koch_edges = []

radius = 800
step_angle = 360.0 / sides
koch_angle = -1 * abs(step_angle - 180.0)

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
        a = distance / (sides * 1.0)

        segs = []
        for i in range(0, sides - 1):
            seg = [(i + 1) * a * dir[0] + pt1[0], (i + 1) * a * dir[1] + pt1[1]]
            segs.append(seg)

        mid = int(sides / 2.0)
        pt = [a * dir[0], a * dir[1], 0]

        top_point = []
        start = segs[mid - 1]
        last = [0, 0]
        #ln.circle(start, 20, [0, 0, 255], img)

        # create point of new polygon
        for i in range(1, sides):
            if i > 1:
                pt = [last[0] - start[0], last[1] - start[1], 0]
            pt = rotate_pt3D(pt, koch_angle)
            last = start
            start = [start[0] + pt[0], start[1] + pt[1]]
            #ln.circle(start, 20, [0, 0, 255], img)
            top_point.append(start)

        # recursive from parent vertex to start
        koch_curve(pt1, segs[mid - 1], curr_iter)
        # recursive for each side of the new polygon
        for i in range(1, sides):
            if i == 1:
                p = segs[mid - 1]
            if i > 1:
                p = top_point[i - 2]
            koch_curve(p, top_point[i - 1], curr_iter)

        # recursive for the last polygon vertex until end parent vertex
        koch_curve(top_point[len(top_point) - 1], pt2, curr_iter)

        # last iteration saves the edges for drawing
        if curr_iter == num_iter:
            koch_edges.append([pt1, segs[mid - 1]])
            for i in range(1, sides):
                if i == 1:
                    p = segs[mid - 1]
                if i > 1:
                    p = top_point[i - 2]
                koch_edges.append([p, top_point[i - 1]])
            koch_edges.append([top_point[len(top_point) - 1], segs[len(segs) - 1]])
            koch_edges.append([segs[len(segs) - 1], pt2])
    else:
        return

# create the first polygon sides
for i in range(sides):
    angle = (i * step_angle) + (step_angle / 2.0) + 90.0
    x = radius * math.cos(angle * (3.1416 / 180.0))
    y = radius * math.sin(angle * (3.1416 / 180.0))
    fig_pts.append([int(x), int(y)])

# call function for each edge
for i in range(sides):
    curr_iter = 0
    koch_curve(fig_pts[i], fig_pts[(i + 1) % sides], curr_iter)

# draw the fractal
for i in range(len(koch_edges)):
    ln.line(koch_edges[i][0], koch_edges[i][1], thick, color, img)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Iterations = {}, Thick = {}'.format(num_iter, thick)), plt.xticks([]), plt.yticks([])
plt.show()
