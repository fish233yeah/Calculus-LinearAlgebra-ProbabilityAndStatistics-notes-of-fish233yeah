import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, n):
    return (math.gamma((n + 1) / 2) * pow((1 + pow(x, 2) / n), ((n+1) / (-2)))) / (math.sqrt(math.pi * n) * math.gamma(n / 2))
n = 2
x = np.linspace(-5, 5, 1001)
y = np.array([])
for i in range(1001):
    y = np.append(y, f(x[i], n))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-5, 5)
plt.ylim(0, 0.5)
plt.plot(x, y)
plt.fill(np.append(np.array([1]), np.append(x, 5)[600:1002]), np.append(np.array([0]), np.append(y, 0)[600:1002]))
def line(x, k, b):
    return k * x + b
lx = np.linspace(2, 2.5, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], 0.5 / 5, -0.15))
plt.plot(lx, l)
plt.text(2.5, 0.1, "概率为" + chr(0x03B1), fontproperties = "SimSun")
lx = np.linspace(0.5, 1, 1001)
l = np.array([])
for i in range(1001):
    l = np.append(l, line(lx[i], -0.5 / 10, 0.05))
plt.plot(lx, l)
plt.text(-0.2, 0.03, "上" + chr(0x03B1) + "分位点", fontproperties = "SimSun")
plt.savefig("./t_alpha.pdf")
plt.show()