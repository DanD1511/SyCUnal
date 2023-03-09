import numpy as np
import matplotlib.pyplot as plt
import scipy; from scipy import signal
import control
import bokeh
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.plotting import figure, show

# Transfer Function (tf)

def tf(num, den):
    G = control.TransferFunction(num,den)
    return G

# Step Response

def step(num, den):

    tf1 = signal.TransferFunction(num, den)
    t, y = signal.step(tf1)
    source = ColumnDataSource(data=dict(x=t, y=y))

    p = figure(title='Step Response', x_axis_label='Time', y_axis_label='Amplitud', width=1000, height=400)

    p.line(t, y, line_width=2)

    show(p)






step([1, 2], [1, 2, 3])
