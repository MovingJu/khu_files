import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math 

Func = np.sin

n = 50

squares = []
result = []
for n in range(2, 5000, 5):
    for i in range(1, n + 1):

        squares.append(math.pi/n * Func(0 + i*math.pi/n))
    
    result.append(sum(squares))

x = np.arange(2, 5000, 5)
y = result

fig, ax = plt.subplots()

Sin = ax.plot(x, y)

plt.title(f"sum of squares by n")

plt.savefig(f"calculus/plots/sums", format = 'png', dpi = 200)

plt.show()
