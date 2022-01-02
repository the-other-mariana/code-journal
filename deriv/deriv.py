from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot(1,1,1)

h = 0.001
PI = 3.1416
cycles = 3

xs = [i for i in list(np.arange(0,PI*2 * cycles, 0.1))]
ys = [sin(x) for x in xs]
test = [cos(x) for x in xs]
dy = []
dx = []

for i in list(np.arange(0, PI*2 * cycles, h)):
    x = i - h
    x_plus_h = i
    #
    lim = (sin(x_plus_h) - sin(x)) / h
    dy.append(lim)
    dx.append(i)

x_ticks = [0.0] + [x for x in xs if (x/PI) % 1 < 0.03 and (x/PI) > 1]


ax.plot(xs, ys, label=r"$sin(x)$")
ax.scatter(dx, dy, marker='o', color='black')
ax.plot(xs, test, label=r"$cos(x)$", color="red")



ax.set_xticks(x_ticks)
ax.set_yticks([-1, 0, 1])
ax.set_xticklabels(['0'] + [f"{int(t / PI)}" + r"$\pi$" for t in x_ticks[1:]])
ax.grid(True)
ax.legend()
plt.show()