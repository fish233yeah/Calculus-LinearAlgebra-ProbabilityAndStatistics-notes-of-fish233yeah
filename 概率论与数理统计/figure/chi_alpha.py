import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n):
    return (pow(x, (n / 2 - 1)) * math.exp(-x / 2)) / (pow(2, (n / 2)) * math.gamma(n / 2))
n = 4
x = np.linspace(0, 10, 1001)
y = np.array([])
for i in range(1001):
    y = np.append(y, f(x[i], n))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 10)
plt.ylim(0, 0.2)
plt.plot(x, y)
plt.fill(np.append(np.array([5.4]), np.append(x, 10)[540:1002]), np.append(np.array([0]), np.append(y, 0)[540:1002]))
def line(x, k, b):
    return k * x + b
lx = np.linspace(6.5, 7.5, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], 0.2 / 10, -0.075))
plt.plot(lx, l)
plt.text(7.5, 0.075, "概率为" + chr(0x03B1), fontproperties = "SimSun")
lx = np.linspace(4.9, 5.4, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], -0.2 / 10, 0.108))
plt.plot(lx, l)
plt.text(4, 0.012, "上" + chr(0x03B1) + "分位点", fontproperties = "SimSun")
plt.savefig("./chi_alpha.pdf")
plt.show()