import numpy as np
import random
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import seaborn as sns

gamma = 0.9
eps = 0.01
N = 37

def mat2line(x, y, dim):
	return (y * dim) + x

def line2mat(s, dim):
	return (s // dim, s % dim)

def rescale(a, x, min, max):
	highest = np.amax(a)
	lowest = np.amin(a)
	x_std = (x - lowest) / (highest - lowest)
	x_scaled = x_std * (max - min) + min
	f = lambda x: int(x)
	return f(x_scaled)

def build_cycle_checker(cycle_tolerance):
	cycle_check = []
	for c in range(cycle_tolerance):
		cycle_check += [None]
	return cycle_check

def print_head(iter, fr, names_s):
	print("==========================")
	print(f"Iteration {iter}:")
	print("fr:", fr)
	for i in range(len(list(fr))):
		print(names_s[i], end='\t')
	print()

def print_qsa(qsa, msg):
	print("Q(s,a)", msg)
	for a in range(len(qsa)):
		for s in range(len(qsa[0])):
			val = qsa[a][s]
			print("{:.2f}".format(val), end='\t')
		print()

'''
with open('cost.txt') as f:
	lines = f.readlines()
g1 = [[] for l in range(len(lines))]
for l in range(len(lines)):
	parts = lines[l].split(' ')
	for p in parts:
		if p == '\n':
			continue
		g1[l].append(int(p))

g2 =np.array([np.array(xi) for xi in g1])
'''

noise = PerlinNoise(octaves=2, seed=1)
xpix, ypix = N, N
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
pic = np.array(pic)
pic2 = np.ones((N, N), dtype=int)

for i in range(len(pic)):
	for j in range(len(pic)):
		pic2[i, j] = rescale(pic, pic[i, j], 1, 255)
mins = list(np.where(pic2 == np.amin(pic2)))
if len(mins) > 1:
	pic2[mins[0][0], mins[1][0]] = 0
	print("[ERROR] world generation went wrong, please try again")

frame = np.ones((N+2, N+2), dtype=int)
frame = frame * 1000
frame[1:-1, 1:-1] = pic2
print('frame', frame)

punish = -1 * frame
# states
states = len(punish) * len(punish[0])
# actions: 0 up 1 down 2 right 3 left
# 4: diag up right 5: diag up left 6: diag down right 7: diag down left
a = [[0, -1], [0, 1], [1, 0], [-1, 0], [1, -1], [-1, -1], [1, 1], [-1, 1]]
actions = len(a)


fr = np.zeros(states, dtype=float)
fmt = np.zeros((states, actions), dtype=int)
dim = len(punish)

# build reward func based on costs
for i in range(len(punish)):
	for j in range(len(punish[0])):
		fr[(i * dim) + j] = punish[i, j]

print('fr:', list(fr))

# build transition func for a states, actions matrix
for s in range(states):
	# current state coords
	x = s % dim
	y = s // dim

	for i in range(len(a)):
		sfx = x + a[i][0]
		sfy = y + a[i][1]
		if sfx < 0 or sfx >= dim or sfy < 0 or sfy >= dim:
			# if action a[i] goes beyond bounds, stay in current state
			fmt[s, i] = mat2line(x, y, dim)
		else:
			# store the final state
			fmt[s, i] = mat2line(sfx, sfy, dim)

print(dim)

names_s = [f'({line2mat(i, dim)[0]}, {line2mat(i, dim)[1]})' for i in range(states)]
names_a = ['up', 'down', '->', '<-', 'up right', 'up left', 'down right', 'down left']

qsa = np.zeros((actions, states), dtype=float)
delta = 1000000 * np.ones((actions, states), dtype=float)
done = np.zeros((actions, states), dtype=bool)
iter = 1


while(True):
	# stop condition
	for i in range(actions):
		for j in range(states):
			if delta[i, j] < eps:
				done[i, j] = True
	if all(list(done.reshape(actions * states))):
		break

	# calculate q(s,a) for each s
	for ai in range(actions):
		for si in range(states):
			sf = fmt[si, ai]
			r = 0
			if len(np.array(fr).shape) == 1:
				# simple fr
				r = fr[int(sf)]
			elif len(np.array(fr).shape) > 1:
				# complex fr
				r = fr[int(sf)][si][ai]
			terms = []
			# for each q(s,a) cell, we need maximum taking every action a
			for a in range(actions):
				term = qsa[a, sf]
				terms.append(term)
			# take the maximum to complete q(s,a) new value
			q = r + gamma * max(terms)
			# difference
			delta[ai][si] = abs(q - qsa[ai][si])
			# update v for next iteration
			qsa[ai][si] = q
	iter += 1

politic = np.zeros(states, dtype=int)
politic = list(politic)
print("Optimal Politic:")
for i in range(states):
	# take max of the column in state s
	action = max(list(qsa[:, i]))
	politic[i] = list(qsa[:, i]).index(action)
	print(f"{names_s[i]} = {names_a[list(qsa[:, i]).index(action)]},", end='\t')
print(politic)

# start in random coord i, j
curr = (random.randrange(dim-1), random.randrange(dim-1))
trajectory = [curr]

cycle_tolerance = 2
cycle_check = build_cycle_checker(cycle_tolerance)

steps = 0

done = False
cycled = False
while(True):
	if done or cycled:
		break
	for c in cycle_check:
		if curr == c:
			cycled = True
			break
	state = mat2line(curr[1], curr[0], dim)
	sf = fmt[state, politic[state]]

	for i in range(1, len(cycle_check)):
		cycle_check[i] = cycle_check[i - 1]
	cycle_check[0] = curr

	curr = line2mat(sf, dim)
	trajectory.append(curr)
	print(fr[sf], curr)
	if fr[sf] >= 0:
		print('done walking')
		done = True
	steps += 1

# if we show only the field w/o bounds, we substract 1 to the frame coordinates in trajectory
ti = [t[0]-1 for t in trajectory]
tj = [t[1]-1 for t in trajectory]

# plot to see full terrain and trajectory
plt.imshow(frame[1:-1, 1:-1], cmap='terrain')
plt.scatter(tj, ti, marker='x', color='red')
plt.show()

# plot to save a part of punish mtx
ax = sns.heatmap(punish[10:20, 0:10], annot=True, fmt='d')
ax.set_yticklabels(list(np.arange(10, 20)))
#plt.savefig('punish-pt2', dpi=500)
plt.show()

fig = plt.figure()
# add axes
ax3d = fig.add_subplot(111,projection='3d')
xx, yy = np.meshgrid(range(N), range(N))
ax3d.plot_surface(yy, xx, frame[1:-1, 1:-1], alpha=0.5, cmap='terrain', edgecolor='black')
plt.show()

# plot to see qsa: make rows thicker
row_size = 200
q_square = np.zeros((actions * row_size, states), dtype=float)

for a in range(actions):
	piece = np.zeros((row_size, states), dtype=float)
	for r in range(row_size):
		for s in range(states):
			piece[r, s] = qsa[a, s]
	q_square[(a*row_size): (a*row_size) + row_size, :] = piece

fig, ax = plt.subplots(1, 1)
img = ax.imshow(q_square)
y_label_list = [names_a[x] for x in range(actions)]
y_ticks_pos = [(x*row_size) + int(row_size*0.5) for x in range(actions)]

ax.set_yticks(y_ticks_pos)
ax.set_yticklabels(y_label_list)

fig.colorbar(img)
plt.show()

# plot to see q column and max when cycled
#plt.rcParams['text.usetex'] = True
f = plt.figure(figsize=(4,3))
ax = f.add_subplot(111)
x = 33
y = 34
s = mat2line(x, y, dim)
print(f'{s} punish: {punish[y, x]} -> fr = {fr[s]}')
y_vals = qsa[:, s]
x_vals = [i for i in range(len(y_vals))]
chosen = max(y_vals)
ax.plot(x_vals, y_vals, marker='o')
ax.scatter([x_vals[list(y_vals).index(chosen)]], [chosen], marker='x', color='red', zorder=10, s=50)
ax.set_xticks([i for i in range(len(names_a))])
ax.set_xticklabels([f'a{i}' for i in range(len(names_a))])
ax.set_title(r"$max_a(Q(mat2line(33,34), a))$")
plt.show()
