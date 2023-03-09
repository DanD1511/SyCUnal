import numpy as np
import matplotlib.pyplot as plt
import scipy; from scipy import signal
import control
import numpy as np
import bokeh
from bokeh.io import output_notebook, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.plotting import figure
import IPython

# Transfer Function (tf)

def tf(num, den):
    G = control.TransferFunction(num,den)
    return G

# Step Response

def step(num, den):

    output_notebook()
    tf1 = signal.TransferFunction(num, den)
    t, y = signal.step(tf1)
    source = ColumnDataSource(data=dict(x=t, y=y))

    p = figure(title='Step Response', x_axis_label='Time', y_axis_label='Amplitud', width=1000, height=400)

    p.line(t, y, line_width=2)

    hover = HoverTool(tooltips=[("Tiempo", "@x"), ("Amplitud", "@y")])
    p.add_tools(hover)

    show(p)

