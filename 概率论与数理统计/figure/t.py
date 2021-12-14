import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n):
    return (math.gamma((n + 1) / 2) * pow((1 + pow(x, 2) / n), ((n+1) / (-2)))) / (math.sqrt(math.pi * n) * math.gamma(n / 2))
n = 2
x = np.linspace(-5, 5, 1001)
y1 = np.array([])
for i in range(1001):
    y1 = np.append(y1, f(x[i], n))
n = 50
y2 = np.array([])
for i in range(1001):
    y2 = np.append(y2, f(x[i], n))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-5, 5)
plt.ylim(0, 0.5)
plt.plot(x, y1, label = "n=2")
plt.plot(x, y2, label = "n=50")
plt.legend()
plt.savefig("./t.pdf")
plt.show()