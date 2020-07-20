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
p1 = tuple([20, 20])
p2 = tuple([40, -40])
thickness = 3
color = [0, 0, 255]
gridGap = 20

ln.grid(gridGap, img) # paints grid
ln.line(p1, p2, thickness, color, img)
ln.line([0, 30], [-100, 60], 7, [255, 0, 0], img)

# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Result Image'), plt.xticks([]), plt.yticks([])
plt.show()
