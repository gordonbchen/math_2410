import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")
from matplotlib.widgets import Slider

A = 1
B = 1
delta = np.pi / 2
a = 5
b = 4

def x(t, A, a, delta):
    return A * np.sin(a*t + delta)

def y(t, B, b):
    return B * np.sin(b*t)

ts = np.linspace(0, 2*np.pi, 500)
xs = x(ts, A, a, delta)
ys = y(ts, B, b)

fig, ax = plt.subplots(figsize=(12, 12), )
plot = ax.plot(xs, ys)[0]

plt.subplots_adjust(bottom=0.25)

axA = plt.axes([0.25, 0.18, 0.55, 0.02])
axB = plt.axes([0.25, 0.16, 0.55, 0.02])
axdelta = plt.axes([0.25, 0.14, 0.55, 0.02])
axa = plt.axes([0.25, 0.12, 0.55, 0.02])
axb = plt.axes([0.25, 0.1, 0.55, 0.02])

sA = Slider(axA, "A", 0, 10, valinit=A)
sB = Slider(axB, "B", 0, 10, valinit=B)
sdelta = Slider(axdelta, "delta", 0, 10, valinit=delta)
sa = Slider(axa, "a", 0, 10, valinit=a)
sb = Slider(axb, "b", 0, 10, valinit=b)

def update(val):
    xs = x(ts, sA.val, sa.val, sdelta.val)
    ys = y(ts, sB.val, sb.val)
    plot.set_xdata(xs)
    plot.set_ydata(ys)

sA.on_changed(update)
sB.on_changed(update)
sdelta.on_changed(update)
sa.on_changed(update)
sb.on_changed(update)

plt.show()
