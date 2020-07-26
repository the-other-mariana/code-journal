import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


class Branch:
    angle = 0.0
    size = 1.0
    father = 0
    thick = 1.0
    begin = [0.0, 0.0]
    end = [0.0, 0.0]

# white image
img_size = 800
img = np.zeros([int(img_size * 0.75), img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)
h = len(img)
w = len(img[0])

color = [0, 0, 0]
gridGap = 20
thick = 20

#ln.grid(gridGap, img) # paints grid

size = 100
center = [0.0, -h/2.0]
ds = 0.75
dt = 0.75
branches = 1
limit = 31
curr_branch = 0
points = []
PI = 3.1416
angle = 30.0
acc_angle = 0.0


b1 = Branch()
b1.angle = 90.0
b1.size = size
b1.thick = thick
b1.begin = [center[0] + 0.0, center[1] + 0.0]
b1.end = [center[0] + 0.0, center[1] + size]
branches = []
branches.append(b1)
ln.line(branches[0].begin, branches[0].end, thick, color, img)

i = 0
#for i in range(limit):
while(True):
    son1 = Branch()
    son2 = Branch()
    son1.father = len(branches) - (i + 1)
    son2.father = len(branches) - (i + 1)
    son1.angle = branches[son1.father].angle + (angle)
    son2.angle = branches[son2.father].angle - (angle)

    son1.size = branches[son1.father].size * ds
    son2.size = branches[son2.father].size * ds
    son1.thick = branches[son1.father].thick * dt
    son2.thick = branches[son2.father].thick * dt
    x1_1 = son1.size * math.cos((son1.angle) * PI / 180.0) + branches[son1.father].end[0]
    y1_1 = son1.size * math.sin((son1.angle) * PI / 180.0) + branches[son1.father].end[1]

    x2_2 = son2.size * math.cos((son2.angle) * PI / 180.0) + branches[son2.father].end[0]
    y2_2 = son2.size * math.sin((son2.angle) * PI / 180.0) + branches[son2.father].end[1]
    son1.begin = branches[son1.father].end
    son1.end = [x1_1, y1_1]
    son2.begin = branches[son2.father].end
    son2.end = [x2_2, y2_2]
    #print(son1.angle)
    #print(son2.angle)
    branches.append(son1)
    branches.append(son2)
    if (son1.thick <= 2):
        break
    ln.line(son1.begin, son1.end, son1.thick, color, img)
    ln.line(son2.begin, son2.end, son1.thick, color, img)
    i+=1

    #ln.line(points[len(points) - 2], points[len(points) - 1], thick, color, img)
    #branches += 2 * branches
    #size = size * ds

print(len(branches))

plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
#plt.savefig("test9.png",bbox_inches='tight')
plt.show()
