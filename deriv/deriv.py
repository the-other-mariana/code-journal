from math import sin
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot(1,1,1)

h = 0.00001
PI = 3.1416
amp = 2.0
freq = 1.0
cycles = 3

xs = [i for i in list(np.arange(0,PI*2 * cycles, 0.1))]
ys = [sin(freq * x) for x in xs]
x_ticks = [0.0] + [x for x in xs if (x/PI) % 1 < 0.03 and (x/PI) > 1]

print(xs, x_ticks)
ax.plot(xs, ys, label=r"f(x)")
ax.set_xticks(x_ticks)
ax.set_yticks([-1, 0, 1])
ax.set_xticklabels(['0'] + [f"{int(t / PI)}" + r"$\pi$" for t in x_ticks[1:]])
ax.grid(True)
ax.legend()
plt.show()