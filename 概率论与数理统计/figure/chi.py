import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n):
    return (pow(x, (n / 2 -1)) * math.exp(-x / 2)) / (pow(2, (n / 2)) * math.gamma(n / 2))
n = 4
x = np.linspace(0, 10, 1001)
y1 = np.array([])
for i in range(1001):
    y1 = np.append(y1, f(x[i], n))
n = 6
y2 = np.array([])
for i in range(1001):
    y2 = np.append(y2, f(x[i], n))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 10)
plt.ylim(0, 0.2)
plt.plot(x, y1, label = "n=4")
plt.plot(x, y2, label = "n=6")
plt.legend()
plt.savefig("./chi.pdf")
plt.show()