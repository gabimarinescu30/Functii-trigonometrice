import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01,1000)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
y_ctg = 1 / np.tan(x)

plt.figure(figsize=(10,7))
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.plot(x, y_tan, label='tan(x)')
plt.plot(x, y_ctg, label='ctg(x)')

plt.axhline(0, color="black", linewidth = 0.75)
plt.axvline(0, color="black", linewidth = 0.75)
plt.title("Functii trigonometrice")
plt.xlabel(x)
plt.ylabel("sin(x),cos(x),ctg(x),cot(x)")
plt.grid(True)
plt.ylim(-10, 10)
plt.legend()
plt.show()