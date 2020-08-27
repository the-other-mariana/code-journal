import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# custom class branch
class Branch:
    father = 0
    angle = 0.0
    size = 1.0
    thick = 1.0
    begin = [0.0, 0.0]
    end = [0.0, 0.0]
    def __init__(self, f):
        self.father = f

# user parameters
color = [0, 0, 0]
thick = 50
size = 275
angle = 30.0

# white image aspect 16:9
img_w = 1920
img_h = 1080
img = np.zeros([img_h, img_w,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# constants
center = [0.0, -len(img)/2.0]
PI = 3.1416
ds = 0.75
dt = 0.75
offspring = 2

# initial branch
b1 = Branch(0)
b1.angle = 90
b1.size = size
b1.thick = thick
b1.begin = [center[0] + 0.0, center[1] + 0.0]
b1.end = [center[0] + b1.size * math.cos((b1.angle) * PI / 180.0), center[1] + b1.size * math.sin((b1.angle) * PI / 180.0)]
branches = []
branches.append(b1)
ln.line(branches[0].begin, branches[0].end, thick, color, img)

i = 0
fr = 0
drawing = True

while(True):
    length = len(branches)
    for b in range(offspring):
        son = Branch(length - (i + 1))
        son.angle = branches[son.father].angle + (angle) * (-1)**(b)
        son.size = branches[son.father].size * ds
        son.thick = branches[son.father].thick * dt
        x = son.size * math.cos((son.angle) * PI / 180.0) + branches[son.father].end[0]
        y = son.size * math.sin((son.angle) * PI / 180.0) + branches[son.father].end[1]
        son.begin = branches[son.father].end
        son.end = [x, y]

        branches.append(son)
        if (son.thick < 2):
            drawing = False
        if drawing == True:
            ln.line(son.begin, son.end, son.thick, color, img)
        fr+=1
    if drawing == False:
        break
    i+=1

print(len(branches))

plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Branches = {}, \u0394Angle = {}°, Thickness = {}'.format(len(branches), angle, thick)), plt.xticks([]), plt.yticks([])
#plt.savefig("test9.png",bbox_inches='tight')
plt.show()
