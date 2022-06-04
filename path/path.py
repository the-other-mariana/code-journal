import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

ax = sns.heatmap(g2)
plt.show()
