import line as ln
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# parameters for user
color = [0, 0, 0]
thick = 20
num_iter = 3

# white image aspect 1:1
img_size = 400
img = np.zeros([img_size, img_size,3],dtype=np.uint8)
img[:] = (255, 255, 255)

# constants
h = len(img)
w = len(img[0])


# show image
plt.plot(), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Iterations = {}'.format(num_iter)), plt.xticks([]), plt.yticks([])
plt.show()
