import math

PI = 3.1416

# calculates distance between two points (tuples)
def distance(p1, p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# loops around main pixel for given thickness
def roundPixel(i, j, thickness, color, img):
	# for guidance
	h = len(img)
	w = len(img[0])

	for r in range(int(i - thickness / 2.0), int(i + thickness / 2.0)):
		for c in range(int(j - thickness / 2.0), int(j + thickness / 2.0)):
			if c >= w or r >= h or c < 0 or r < 0:
				continue
			img[r, c] = color

# paints a grid on the image
def grid(gap, img):
	# for guidance
	h = len(img)
	w = len(img[0])

	for i in range(h):
		for j in range(w):
			if i == int(h / 2.0) or j == int(w / 2.0) :
				img[i, j] = [0, 0, 0]
			if (i % gap == 0 or j % gap == 0) and (i % 2 == 0 and j % 2 == 0):
				img[i, j] = [0, 0, 0]
				
def circle(center, thickness, color, img):
	# for guidance
	h = len(img)
	w = len(img[0])

	for r in range(thickness):
		for a in range(360):
			rads = a * (PI / 180.0)
			x = r * math.cos(rads) + center[0]
			y = r * math.sin(rads) + center[1]

			# center coordinates
			x += w / 2.0
			y = h / 2.0 - y
			if x >= w or y >= h or x < 0 or y < 0:
				continue

			x = int(x)
			y = int(y)
			img[y, x] = color


# paints a line between two points using polar coordinates
def line(p1, p2, thickness, color, img):
	# for guidance
	h = len(img)
	w = len(img[0])
	rads = 0

	# case of division by zero
	if p2[0] == p1[0]:
		rads += PI / 2.0
		if (p2[1] - p1[1]) < 0:
			rads += PI
	else:
		rads += math.atan((p2[1] - p1[1] * 1.0) / (p2[0] - p1[0] * 1.0))
		if (p2[0] - p1[0]) < 0:
			rads += PI
	# prints the degrees between the two points
	# print(rads*180/PI)

	dist = int(distance(p1, p2))
	for r in range(dist):
		x = p1[0] + r * math.cos(rads)
		y = p1[1] + r * math.sin(rads)

		# center coordinates
		x += w / 2.0
		y = h / 2.0 - y

		# validate if point is inside image
		if x >= w or y >= h or x < 0 or y < 0:
			continue

		x = int(x)
		y = int(y)
		img[y, x] = color
		roundPixel(y, x, thickness, color, img)
