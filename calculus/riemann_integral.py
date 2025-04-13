import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math 

x = np.arange(0, 3.1415, 0.0001)

Func = np.sin

y= Func(x)

fig, ax = plt.subplots()

Sin = ax.plot(x, y)

ax.set_xticks([0, math.pi/4, math.pi/2, math.pi * 3 / 4, math.pi])

squares = []


n = 50


for i in range(1, n + 1):
    ax.add_patch(
        patches.Rectangle(
            (0 + (i - 1)*math.pi/n, 0),
            math.pi/n, Func(0+(i)*math.pi/n),
            edgecolor = 'deeppink',
            facecolor = 'lightgray',
            fill = True
        )
    )

    squares.append(math.pi/n * Func(0 + i*math.pi/n))


plt.title(f"sum of squares : {sum(squares)}, number of squares : {n}")


plt.savefig(f"calculus/plots/n_is_{n}.png", format = 'png', dpi = 200)

plt.show()
