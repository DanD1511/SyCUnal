import numpy as np
import matplotlib.pyplot as plt
import scipy; from scipy import signal
import control

# Transfer Function (tf)

def tf(num, den):
    G = control.TransferFunction(num,den)
    return G

# Step Response

def step(G):
    t = np.linspace(0, 10, 1000)
    t, y = control.step_response(G, t)
    plt.plot(t, y)
    return plt.show()

