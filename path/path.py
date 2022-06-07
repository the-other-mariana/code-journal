import numpy as np
import seaborn as sns
import random
import matplotlib.pyplot as plt

def mat2line(x, y, dim):
	return (y * dim) + x

def line2mat(s, dim):
	return (s // dim, s % dim)

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
print(g2)

#ax = sns.heatmap(g2)


punish = -1.0 * g2
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

print('fr:',list(fr))

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

print(fmt)
print(dim)

names_s = [f'({line2mat(i, dim)[0]}, {line2mat(i, dim)[1]})' for i in range(states)]
names_a = ['up', 'down', '->', '<-', 'up right', 'up left', 'down right', 'down left']

qsa = np.zeros((actions, states), dtype=float)
delta = 1000000 * np.ones((actions, states), dtype=float)
done = np.zeros((actions, states), dtype=bool)
iter = 1
gamma = 0.8
eps = 0.01

while(True):

	# stop condition
	for i in range(actions):
		for j in range(states):
			if delta[i, j] < eps:
				done[i, j] = True
	if all(list(done.reshape(actions * states))):
		break

	# print head and current qsa
	#print_head(iter, fr, names_s)
	#print_qsa(qsa, 'current')

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
	# print new vs
	# print_qsa(qsa, 'new')
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
curr = (random.randrange(dim), random.randrange(dim))
trayectory = [curr]

done = False
while(True):
	if done:
		break
	state = mat2line(curr[1], curr[0], dim)
	sf = fmt[state, politic[state]]

	curr = line2mat(sf, dim)
	trayectory.append(curr)
	if fr[sf] >= 0.0:
		done = True

ti = [t[0] for t in trayectory]
tj = [t[1] for t in trayectory]
#ax.scatter(tj, ti, marker='x')
#plt.show()
plt.imshow(g2, cmap='terrain')
plt.scatter(tj, ti, marker='x', color='red')
plt.show()
