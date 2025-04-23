import numpy as np
from matplotlib import pyplot as plt

arrayA = np.random.randint(1, 100, 30)

print(arrayA)

plt.hist(arrayA, 5, rwidth=0.5)
plt.show()
