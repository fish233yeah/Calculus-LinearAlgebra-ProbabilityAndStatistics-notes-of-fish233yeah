import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n1, n2):
    return ((math.gamma((n1 + n2) / 2) * pow(n1 / n2, n1 / 2) * pow(x, (n1 / 2) - 1)) / (math.gamma(n1 / 2) * math.gamma(n2 / 2) * pow(1 + (n1 * x / n2), (n1 + n2) / 2)))
n1 = 15
n2 = 20
x = np.linspace(0, 5, 1001)
y1 = np.array([])
for i in range(1001):
    y1 = np.append(y1, f(x[i], n1, n2))
n1 = 20
n2 = 2
y2 = np.array([])
for i in range(1001):
    y2 = np.append(y2, f(x[i], n1, n2))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 5)
plt.ylim(0, 1)
plt.plot(x, y1, label = "n1=15, n2=20")
plt.plot(x, y2, label = "n1=20, n2=2")
plt.legend()
plt.savefig("./F.pdf")
plt.show()