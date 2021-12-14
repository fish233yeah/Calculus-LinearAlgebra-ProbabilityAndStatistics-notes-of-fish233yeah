import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n1, n2):
    return ((math.gamma((n1 + n2) / 2) * pow(n1 / n2, n1 / 2) * pow(x, (n1 / 2) - 1)) / (math.gamma(n1 / 2) * math.gamma(n2 / 2) * pow(1 + (n1 * x / n2), (n1 + n2) / 2)))
n1 = 15
n2 = 20
x = np.linspace(0, 5, 1001)
y = np.array([])
for i in range(1001):
    y = np.append(y, f(x[i], n1, n2))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 5)
plt.ylim(0, 1)
plt.plot(x, y)
plt.fill(np.append(np.array([1.5]), np.append(x, 5)[300:1002]), np.append(np.array([0]), np.append(y, 0)[300:1002]))
def line(x, k, b):
    return k * x + b
lx = np.linspace(2, 2.5, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], 1 / 5, -0.3))
plt.plot(lx, l)
plt.text(2.5, 0.2, "概率为" + chr(0x03B1), fontproperties = "SimSun")
lx = np.linspace(1.25, 1.5, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], -1 / 5, 0.3))
plt.plot(lx, l)
plt.text(0.7, 0.07, "上" + chr(0x03B1) + "分位点", fontproperties = "SimSun")
plt.savefig("./F_alpha.pdf")
plt.show()